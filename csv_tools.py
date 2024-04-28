import csv


# initialize a csv data file with headers
def init_csv_file(file_name: str, headers: list[str]):
    with open(file_name, 'w', newline='', encoding='UTF-8') as csv_file:
        if len(headers) > 0:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(headers)


# append multiple lines to a csv data file
def write_csv_file(file_name: str, data: list[list[str]]):
    with open(file_name, 'a', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerows(data)


# read the headers and data from a csv file
def read_csv_file(csv_file_name: str):
    with open(csv_file_name, 'r', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # read headers and initialize data arrays
        cdf_headers = next(csv_reader)
        cdf_data = [[] for i in range(len(cdf_headers))]

        # read data
        for row in csv_reader:
            for idx, one_data in enumerate(row):
                cdf_data[idx].append(one_data)

    return cdf_headers, cdf_data
