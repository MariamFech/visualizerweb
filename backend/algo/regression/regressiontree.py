import numpy as np
from sklearn.tree import DecisionTreeRegressor
from ..npHelper import np_array_to_list, get_x_and_y_arrays, get_prediction_points


def regressiontree(data):
    depth = data['mlAlgoOptions']['Depth']
    samples = data['mlAlgoOptions']['Samples']
    x, train_y = get_x_and_y_arrays(data['points'])
    train_x = x.reshape(-1, 1)
    pred_x = get_prediction_points(x, -1)
    predict_x = pred_x.reshape(-1, 1)

    # Fit regression model
    lm = DecisionTreeRegressor(max_depth=depth, min_samples_leaf=samples)
    lm.fit(train_x, train_y)

    # Predict
    y_pred = np_array_to_list(np.asarray(lm.predict(train_x), dtype = 'int'))
    predict_y = np_array_to_list(np.asarray(lm.predict(predict_x), dtype = 'int'))

    result = (np.asarray(pred_x).tolist(),predict_y)


    return { "specific" : "Regression Tree",
             "labels": result,
             "prediction": '' }