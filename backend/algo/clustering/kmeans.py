from sklearn.cluster import KMeans
from ..npHelper import np_array_to_list, get_np_points_array


def kmeans(data):
    cluster = data["mlAlgoOptions"]["Cluster"]
    iterations = data["mlAlgoOptions"]["Iterations"]
    centroid_seeds = data["mlAlgoOptions"]["Centroid Seeds"]
    points = get_np_points_array(data["points"])
    predict_points = get_np_points_array(data["predictionData"])

    if len(points) < cluster:
        return {"error": "less points than cluster"}

    km = KMeans(init='k-means++', n_clusters=cluster, n_init=centroid_seeds, max_iter=iterations)
    km.fit(points)
    centroids = np_array_to_list(km.cluster_centers_)
    labels = np_array_to_list(km.labels_)
    iterations = km.n_iter_
    prediction = np_array_to_list(km.predict(predict_points))





    return {
        "specific": {
            "centroids": centroids,
            "iterations": iterations
        },
        "labels": labels,
        "prediction": prediction

    }
