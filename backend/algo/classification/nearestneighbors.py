import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from ..npHelper import np_array_to_list, get_np_points_array, get_np_label_array


def k_neighbors_classifier(data):
    neighbors = data['mlAlgoOptions']['Neighbors']
    points = get_np_points_array(data['points'])
    label = get_np_label_array(data['points'])
    predict_points = get_np_points_array(data['predictionData'])

    if len(label) == 1:
        return {"error": "at least two colors are needed"}

    knb = KNeighborsClassifier(n_neighbors=neighbors)
    knb.fit(points, label)

    classes = np_array_to_list(knb.predict(points))
    prediction = np_array_to_list(knb.predict(predict_points))

    return {"labels": classes,
            "prediction": prediction}
