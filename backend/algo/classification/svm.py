import threading
import time

from sklearn import svm
from ..npHelper import np_array_to_list, get_np_points_array, get_np_label_array


def svm_c(data):
    c = data['mlAlgoOptions']['C']
    k = data['mlAlgoOptions']['Kernel']
    points = get_np_points_array(data['points'])
    label = get_np_label_array(data['points'])
    predict_points = get_np_points_array(data['predictionData'])

    if len(label) == 1:
        return {"error": "at least two colors are needed"}

    svc = svm.SVC(C=c, kernel=k)


    t = threading.Thread(target=svc_fit, args=(svc, points, label,))
    t.start()
    t.join(timeout=60)


    try:
        classes = np_array_to_list(svc.predict(points))
        prediction = np_array_to_list(svc.predict(predict_points))
    except:
        return {"error": "Calculation takes longer than 1 minute. Try a model with fewer points."}

    return {"labels": classes,
            "prediction": prediction}


def svc_fit(svc, points, label):
    svc.fit(points, label)
