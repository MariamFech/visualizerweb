import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from ..npHelper import np_array_to_list, get_x_and_y_arrays, get_prediction_points


def linear(data):
    degree = data['mlAlgoOptions']['Degree']
    x, y = get_x_and_y_arrays(data['points'])
    train_x = x.reshape(-1, 1)
    pred_x = get_prediction_points(x, degree)
    predict_x = pred_x.reshape(-1, 1)

    #transform x values for polynomial linear regression
    if degree > 1:
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        train_x = poly.fit_transform(train_x)
        predict_x = poly.fit_transform(predict_x)

    # Create linear regression object
    lm = LinearRegression()

    # Train the model using the training sets
    lm.fit(train_x, y)

    # Make predictions using the testing set
    pred_y = np_array_to_list(np.asarray(lm.predict(train_x), dtype = 'int'))

    # Make predictions using the testing set
    predict_y = np_array_to_list(np.asarray(lm.predict(predict_x), dtype = 'int'))

    result = (np.asarray(pred_x).tolist(),predict_y)

    return {"specific":"Linear Regression",
            "labels": result,
            "prediction": ''}