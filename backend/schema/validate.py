# !/usr/bin/env python
# encoding: utf-8
import json
import jsonschema
from jsonschema import validate

ALGONAMES = ["K-Means", "Hierarchical", "Decision Tree", "Nearest Neighbors", "SVM"]


def get_schema(name):
    algo = ''
    if name == ALGONAMES[0]:
        algo = 'kmeans'
    if name == ALGONAMES[1]:
        algo = 'hierarchical'
    if name == ALGONAMES[2]:
        algo = 'decision_tree'
    if name == ALGONAMES[3]:
        algo = 'nearest_neighbors'
    if name == ALGONAMES[4]:
        algo = 'svm'

    schema_path = "schema/" + algo + "_schema.json"
    with open(schema_path, 'r') as file:
        schema = json.load(file)
    return schema


def __validate_json(json_data):
    if json_data["mlAlgoName"] in ALGONAMES:
        schema = get_schema(json_data["mlAlgoName"])
    else:
        return False

    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        return False
    return True

# TODO: check cluster and points... and labels etc....
def is_valid(json_data):
    return __validate_json(json_data)
