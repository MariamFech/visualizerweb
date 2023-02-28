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

# get x valued for prediction (linear and tree)
def get_prediction_points(x_values, degree):
    x_min = x_values[0]
    x_max = x_values[len(x_values) - 1]

    # two point prediction for 1st grade linear regression (streight line) 
    if(degree == 1):
        pred_x = [x_min, x_max]
        return np.asarray(pred_x)
    
    neg_offset = 200
    pos_offset = 200

    # avoid negative x-values (important for the frontend)
    if(x_min <= neg_offset):
        neg_offset = x_min

    # no offset of prediction data for regressiontree
    if(degree == -1):
        neg_offset = 0
        pos_offset = 0
    
    x = x_min - neg_offset
    x_end = x_max + pos_offset
    
    pred_x = np.arange(x, x_end, 1, dtype = int)
    
    # add last given value if not included
    if pred_x[len(pred_x)-1] < x_max:
        pred_x = np.append(pred_x, x_max)
    
    sorted_points = np.sort(pred_x, axis=None)
    return sorted_points
