import numpy as np


def get_np_points_array(points):
    arr = []
    for items in points:
        arr.append([items['x'], items['y']])
    return np.asarray(arr)

#returns numpy arrays of x and y coordinates as a tuple
def get_x_and_y_arrays(points):
    arr_x = []
    arr_y = []
    for items in points:
        arr_x.append(items['x'])
        arr_y.append(items['y'])
    arr_x.sort()
    return (np.asarray(arr_x), np.asarray(arr_y))

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
