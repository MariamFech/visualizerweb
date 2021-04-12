import numpy as np
from sklearn import tree
from ..npHelper import np_array_to_list, get_np_points_array, get_np_label_array


def decisiontree(data):
    depth = data['mlAlgoOptions']['Depth']
    points = get_np_points_array(data['points'])
    label = get_np_label_array(data['points'])
    predict_points = get_np_points_array(data['predictionData'])

    if len(label) == 1:
        return {"error": "at least two colors are needed"}

    dt = tree.DecisionTreeClassifier(max_depth=depth)
    dt.fit(points, label)

    classes = np_array_to_list(dt.predict(points))
    prediction = np_array_to_list(dt.predict(predict_points))

    return {"labels": classes,
            "prediction": prediction}
