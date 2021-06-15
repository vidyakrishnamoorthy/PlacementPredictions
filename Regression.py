from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score


def linear_regression(df):
    lm = LinearRegression()
#    X = df[["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]]
    X = df[["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]]
    Y = df[["status_code"]]
    lm.fit(X[:-20], Y[:-20])
    Yhat = lm.predict(X[-20:])
    print(lm.intercept_, lm.coef_)
    #[-0.99829544] [[ 0.01986416  0.01076585  0.015015   -0.00125281 -0.02056289]]
    # df[["status_code"]] = -0.99829544 + 0.01986416*ssc_p + 0.01076585*hsc_p +
    # 0.015015*degree_p + -0.00125281*etest_p + -0.02056289*mba_p
    print("Rsquare linear regression", r2_score(Y[-20:], Yhat))

    axl = sns.kdeplot(df["status_code"], color = 'r', label = "Actual value")
    sns.kdeplot(np.concatenate(Yhat, axis = 0), color = 'b', label = "Fitted value", ax = axl)
    plt.show()


def linear_regression_of_codes(df):
    lm = LinearRegression()
    X = df[["hsc_s_code", "degree_t_code", "specialisation_code"]]
    Y = df[["status_code"]]
    lm.fit(X[:-20], Y[:-20])
    Yhat = lm.predict(X[-20:])
    print(lm.intercept_, lm.coef_)
    #[10.30879257] [[ 0.42226427 -0.66736126 -2.23823676]]
    # df[["status_code"]] = 10.30879257 + 0.4222642*hsc_s_code + -0.66736126*degree_t_code +
    # -2.23823676*specialisation_code
    print("Rsquare linear regression of codes", r2_score(Y[-20:], Yhat))

    axl = sns.kdeplot(df["status_code"], color = 'r', label = "Actual value")
    sns.kdeplot(np.concatenate(Yhat, axis = 0), color = 'b', label = "Fitted value", ax = axl)
    plt.show()


def PolynomialRegression(df):
    X = df[["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]]
    Y = df[["status_code"]]

    pr = PolynomialFeatures(degree = 2, include_bias = False)
    X = pr.fit_transform(X[:-20])
    Y = pr.fit_transform(Y[:-20])

    model = LinearRegression()
    model.fit(X, Y)

    print("Model:", model.score(X, Y))

#    print("Rsquare polynomial regression", r2_score(Y[-20:], Yhat[-20:]))

#    axl = sns.kdeplot(df["status_code"], color = 'r', label = "Actual value")
#    sns.kdeplot(np.concatenate(Yhat, axis = 0), color = 'b', label = "Fitted value", ax = axl)
#    plt.show()


def pipelines(df):
    input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(degree = 2)),
             ('mode', LinearRegression())] # tuple: ('name_of_estimator', model_constructor)
    pipe = Pipeline(input)
    X = df[["ssc_p", "hsc_p", "degree_p", "mba_p"]] # "etest_p",
    Y = df["status_code"]
    pipe.fit(X[:-20], Y[:-20])
    Yhat = pipe.predict(X[-20:])
    print("Rsquare pipelines", r2_score(Y[-20:], Yhat))

    axl = sns.kdeplot(df["status_code"], color='r', label="Actual value")
    sns.kdeplot(Yhat, color='b', label="Fitted value", ax=axl)
    plt.show()

