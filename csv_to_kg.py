import csv_tools
from tools import lab3_lookup
from tools.isub import isub
import Levenshtein as lev

# to accelerate the search
dbpedia_cache = dict()


# map a keyword to a DPpedia entity
def keyword_to_DBpedia_entity(keyword: str,
                              type_filter_enabled: bool = False,
                              type_filter: list[str] = []) -> str:
    if keyword in dbpedia_cache:
        return dbpedia_cache[keyword]
    dbpedia = lab3_lookup.DBpediaLookup()
    entities = dbpedia.getKGEntities(keyword, 100)
    largest_similarity_idx = -1
    largest_similarity = -1.0
    print(f"'{keyword}' Entities from DBPedia:")
    for idx, ent in enumerate(entities):
        # apply the type filter
        if type_filter_enabled:
            # "len(type_filter) == 0 and type_filter_enabled == True" means the entity cannot have any types
            if len(type_filter) == 0 and len(ent.getTypes()) != 0:
                continue
            # each item in type_in_filter should be in eneity's types
            should_continue = False
            for type_in_filter in type_filter:
                if type(type_in_filter) is str:
                    if type_in_filter.lower() not in f"{ent.getTypes()}".lower(
                    ):
                        should_continue = True
                        break
                elif type(type_in_filter) is list:
                    can_pass = False
                    for one_option in type_in_filter:
                        if one_option.lower() in f"{ent.getTypes()}".lower():
                            can_pass = True
                            break
                    if not can_pass:
                        should_continue = True
                        break
                else:
                    raise Exception("Unsupported filter type")
            if should_continue:
                continue

        isub_similarity = isub(keyword, ent.getLabel())
        jaro_winkler_similarity = lev.jaro_winkler(keyword, ent.getLabel())
        # print("label:", ent.getLabel(), "id:", ent.getId(), "types:",
        #       ent.getTypes(), "isub_similarity:", isub_similarity,
        #       "lev.jaro_winkler:", jaro_winkler_similarity)
        # save the most similar entity
        if isub_similarity + jaro_winkler_similarity > largest_similarity:
            largest_similarity = isub_similarity + jaro_winkler_similarity
            largest_similarity_idx = idx

    most_similar_id = "None"
    if largest_similarity_idx >= 0:
        most_similar_id = entities[largest_similarity_idx].getId(
        )  # we only take the entity with the highest similarity value to the keyword
        print(
            f"Most similar entity to '{keyword}, id: {most_similar_id}'\n{entities[largest_similarity_idx]}, Similarity: {largest_similarity}."
        )
    else:
        print("No entry can map.")

    # save result in cache to save time for future search
    dbpedia_cache[keyword] = most_similar_id

    # For Task A.3: Extend your system to be able to automatically predict the type for the columns about cities and countries.
    if largest_similarity_idx >= 0:
        if "country" in f"{entities[largest_similarity_idx].getTypes()}".lower(
        ):
            print("This is a country.")
        if "city" in f"{entities[largest_similarity_idx].getTypes()}".lower(
        ) or "town" in f"{entities[largest_similarity_idx].getTypes()}".lower(
        ):
            print("This is a city.")

    print()

    return most_similar_id


def main():
    # read data from csv file
    data_name = "worldcities-free-100"
    # data_name = "worldcities-free"
    csv_file = f"data/{data_name}.csv"
    cea_suffix = "_cea_system"
    cta_suffix = "_cta_system"
    cta_file = f"data/output/{data_name}{cta_suffix}.csv"
    cea_file = f"data/output/{data_name}{cea_suffix}.csv"

    headers, data = csv_tools.read_csv_file(csv_file)
    city_col_idx = 1
    country_col_idx = 4

    # get DBpedia IDs of "city" and "country"
    city_dbpid = keyword_to_DBpedia_entity(keyword="City",
                                           type_filter_enabled=True,
                                           type_filter=[])
    country_dbpid = keyword_to_DBpedia_entity(keyword="Country",
                                              type_filter_enabled=True,
                                              type_filter=[])

    # write contents to cta_file
    csv_tools.init_csv_file(cta_file, [])
    csv_tools.write_csv_file(cta_file, [[data_name, city_col_idx, city_dbpid]])
    csv_tools.write_csv_file(cta_file,
                             [[data_name, country_col_idx, country_dbpid]])

    # get DBpedia IDs of all cells, and write to cea_file
    cells_csv_output = []
    columns_to_handle = [city_col_idx, country_col_idx]
    type_filters = [["location", "place", ["city", "town"]],
                    ["location", "place", "country"]]
    for idx2, col_idx in enumerate(columns_to_handle):
        for idx, cell in enumerate(data[col_idx]):
            row_idx = idx + 1
            cell_dbpid = keyword_to_DBpedia_entity(
                keyword=cell,
                type_filter_enabled=True,
                type_filter=type_filters[idx2])
            cells_csv_output.append(
                [data_name, f"{row_idx}", f"{col_idx}", cell_dbpid])

    csv_tools.init_csv_file(cea_file, [])
    csv_tools.write_csv_file(cea_file, cells_csv_output)


if __name__ == '__main__':
    main()
