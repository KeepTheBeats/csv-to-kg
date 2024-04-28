'''
Created on 19 Jan 2021

@author: ejimenez-ruiz
'''
import owlready2
from rdflib import Graph


def getClasses(onto):
    return onto.classes()


def getDataProperties(onto):
    return onto.data_properties()


def getObjectProperties(onto):
    return onto.object_properties()


def getIndividuals(onto):
    return onto.individuals()


def getRDFSLabelsForEntity(entity):
    #if hasattr(entity, "label"):
    return entity.label


def getRDFSLabelsForEntity(entity):
    #if hasattr(entity, "label"):
    return entity.label


def loadOntology(urionto):

    #Method from owlready
    onto = owlready2.get_ontology(urionto).load()

    print("Classes in Ontology: " + str(len(list(getClasses(onto)))))
    # print(list(getClasses(onto)))
    for cls in getClasses(onto):
        #Name of entity in URI. But in some cases it may be a
        #code like in mouse and human anatomy ontologies
        print(cls.iri)
        print("\t" + cls.name)
        #Labels from RDFS label
        print("\t" + str(getRDFSLabelsForEntity(cls)))


if __name__ == '__main__':
    #Load ontology from URI or local file
    data_path = "../lab-session3/data"
    # urionto = data_path + "/cmt.owl"
    urionto = data_path + "/ekaw.owl"
    # urionto = data_path + "/confOf.owl"
    # urionto = data_path + "/human.owl"
    # urionto = data_path + "/mouse.owl"

    loadOntology(urionto)
