import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from ..npHelper import np_array_to_list, get_x_and_y_arrays


def linear(data):
    degree = data['mlAlgoOptions']['Degree']
    x, y = get_x_and_y_arrays(data['points'])
    predict_x, predict_y = get_x_and_y_arrays(data['predictionData'])
    train_x = x.reshape(-1, 1)
    predict_x = predict_x.reshape(-1, 1)

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
    predicted_y = np_array_to_list(np.asarray(lm.predict(predict_x), dtype = 'int'))

    xyResult = (np.asarray(x).tolist(),pred_y)

    return {"specific":"Linear Regression",
            "labels": xyResult,
            "prediction": predicted_y}