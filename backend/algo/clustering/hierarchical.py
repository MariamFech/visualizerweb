import numpy as np
from sklearn.cluster import AgglomerativeClustering
from ..npHelper import np_array_to_list, get_np_points_array


def hierarchical(data):
    cluster = data['mlAlgoOptions']['Cluster']
    linkage = data['mlAlgoOptions']['Linkage']
    points = get_np_points_array(data['points'])
    print(points)

    if len(points) < cluster:
        return {"error": "less points than cluster"}

    h = AgglomerativeClustering(n_clusters=cluster, linkage=linkage)
    h.fit(points)
    labels = np_array_to_list(h.labels_)

    return {
        "labels": labels}
