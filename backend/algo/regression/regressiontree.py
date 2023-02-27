import numpy as np
from sklearn.tree import DecisionTreeRegressor
from ..npHelper import np_array_to_list, get_x_and_y_arrays


def regressiontree(data):
    depth = data['mlAlgoOptions']['Depth']
    x, train_y = get_x_and_y_arrays(data['points'])
    predict_x, predict_y = get_x_and_y_arrays(data['predictionData'])
    train_x = x.reshape(-1, 1)
    predict_x = predict_x.reshape(-1, 1)

    # Fit regression model
    lm = DecisionTreeRegressor(max_depth=depth)
    lm.fit(train_x, train_y)

    # Predict
    y_pred = np_array_to_list(np.asarray(lm.predict(train_x), dtype = 'int'))
    predicted_y = np_array_to_list(np.asarray(lm.predict(predict_x), dtype = 'int'))

    xyResult = (np.asarray(x).tolist(),y_pred)


    return { "specific" : "Regression Tree",
             "labels": xyResult,
             "prediction": predicted_y }