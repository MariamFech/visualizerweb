#!/usr/bin/env python
# encoding: utf-8
from schema import validate
from algo.clustering.kmeans import kmeans
from algo.clustering.hierarchical import hierarchical
from algo.classification.svm import svm_c
from algo.classification.decisiontree import decisiontree
from algo.classification.nearestneighbors import k_neighbors_classifier


ALGONAMES = ["K-Means", "Hierarchical", "Decision Tree", "Nearest Neighbors", "SVM"]


def compute(request):
    if validate.is_valid(request):
        if request['mlAlgoName'] == ALGONAMES[0]:
            return kmeans(request)
        if request['mlAlgoName'] == ALGONAMES[1]:
            return hierarchical(request)
        if request['mlAlgoName'] == ALGONAMES[2]:
            return decisiontree(request)
        if request['mlAlgoName'] == ALGONAMES[3]:
            return k_neighbors_classifier(request)
        if request['mlAlgoName'] == ALGONAMES[4]:
            return svm_c(request)
        return request['mlAlgoName']
    else:
        return 'Server: incorrect data received'


