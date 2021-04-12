import numpy as np


def get_np_points_array(points):
    arr = []
    for items in points:
        arr.append([items['x'], items['y']])
    return np.asarray(arr)


def np_array_to_list(np_array):
    return np.asarray(np_array).tolist()


def get_np_label_array(points):
    colors_arr = []
    numbers_arr = []
    unique_colors = []

    for items in points:
        colors_arr.append([items['strokeColor']])

    for color in colors_arr:
        if color not in unique_colors:
            unique_colors.append(color)

    for color in colors_arr:
        numbers_arr.append(unique_colors.index(color))

    return np.asarray(numbers_arr)
