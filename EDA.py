import matplotlib.pyplot as plt

def preprocessing(df):
    return df


def describe_data(df):
    print(df.describe())
    print(df.dtypes)
    print(df.corr())


def status_by_gender(df):
    print("group by gender")
    df_gender = df[['sl_no', 'gender', 'status']]
    df_grp = df_gender.groupby(['gender', 'status'], as_index = False).count()

    df_pivot = df_grp.pivot(index = "gender", columns = ["status"])
    print(df_pivot)


def status_by_degree(df):
    print("group by degree")
    df_degree = df[['sl_no', 'degree_t', 'status']]
    df_grp = df_degree.groupby(['degree_t', 'status'], as_index = False).count()

    df_pivot = df_grp.pivot(index = "degree_t", columns = ["status"])
    print(df_pivot)


def status_by_specialization(df):
    print("group by specialization")
    df_specialisation = df[['sl_no', 'specialisation', 'status']]
    df_grp = df_specialisation.groupby(['specialisation', 'status'], as_index = False).count()

    df_pivot = df_grp.pivot(index = "specialisation", columns = ["status"])
    print(df_pivot)


def status_by_hsc_s(df):
    print("group by hsc_s")
    df_hsc_s = df[['sl_no', 'hsc_s', 'status']]
    df_grp = df_hsc_s.groupby(['hsc_s', 'status'], as_index = False).count()

    df_pivot = df_grp.pivot(index = "hsc_s", columns = ["status"])
    print(df_pivot)


def status_by_workex(df):
    print("group by workex")
    df_workex = df[['sl_no', 'workex', 'status']]
    df_grp = df_workex.groupby(['workex', 'status'], as_index = False).count()

    df_pivot = df_grp.pivot(index = "workex", columns = ["status"])
    print(df_pivot)