#!/usr/bin/env python
# encoding: utf-8
from schema import validate
from algo.clustering.kmeans import kmeans
from algo.clustering.hierarchical import hierarchical
from algo.classification.svm import svm_c
from algo.classification.decisiontree import decisiontree
from algo.classification.nearestneighbors import k_neighbors_classifier
from algo.regression.linear_regression import linear
from algo.regression.regressiontree import regressiontree

ALGONAMES = ["K-Means", "Hierarchical", "Decision Tree", "Nearest Neighbors", "SVM", "Linear Regression", "Regression Tree"]


def compute(request):
    if validate.is_valid(request):
        if request['mlAlgoName'] == ALGONAMES[0]:
            returnValue = kmeans(request)
            return returnValue
        if request['mlAlgoName'] == ALGONAMES[1]:
            returnValue = hierarchical(request)
            return returnValue
        if request['mlAlgoName'] == ALGONAMES[2]:
            returnValue = decisiontree(request)
            return returnValue
        if request['mlAlgoName'] == ALGONAMES[3]:
            returnValue = k_neighbors_classifier(request)
            return returnValue
        if request['mlAlgoName'] == ALGONAMES[4]:
            returnValue = svm_c(request)
            return returnValue
        if request['mlAlgoName'] == ALGONAMES[5]:
            returnValue = linear(request)
            return returnValue
        if request['mlAlgoName'] == ALGONAMES[6]:
            returnValue = regressiontree(request)
            return returnValue
        return request['mlAlgoName']
    else:
        return 'Server: incorrect data received'


