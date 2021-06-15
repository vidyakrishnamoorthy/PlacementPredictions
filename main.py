import pandas as pd
import EDA
import Regression

# Placed or not based on ssc_p, hsc_p, degree_p, workex, etest_p, mba_p
# If placed, Salary based on hcs_c, degree_t, specialization
# predict status based on the not influencing variables

def main():
    df = pd.read_csv("Placement_Data_Full_Class.csv")
    df = EDA.preprocessing(df)
    EDA.describe_data(df)
    EDA.status_by_gender(df)
    EDA.status_by_degree(df)
    EDA.status_by_specialization(df)
    EDA.status_by_hsc_s(df)
    EDA.status_by_workex(df)
    Regression.linear_regression(df)
    Regression.linear_regression_of_codes(df)
    Regression.PolynomialRegression(df)
    Regression.pipelines(df)


main()
