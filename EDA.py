def status_code(row):
    if row['status'] == 'Placed':
        return 1
    else:
        return 0


def hsc_s_code(row):
    if row['hsc_s'] == 'Commerce':
        return 1
    elif row['hsc_s'] == 'Science':
        return 2
    elif row['hsc_s'] == 'Arts':
        return 3
    else:
        return 0


def degree_t_code(row):
    if row['degree_t'] == 'Comm&Mgmt':
        return 1
    elif row['degree_t'] == 'Sci&Tech':
        return 2
    elif row['degree_t'] == 'Others':
        return 3
    else:
        return 0


def specialisation_code(row):
    if row['specialisation'] == 'Mkt&Fin':
        return 1
    elif row['specialisation'] == 'Mkt&HR':
        return 2
    else:
        return 0


def preprocessing(df):
    df['status_code'] = df.apply(lambda row: status_code(row), axis = 1)
    df['hsc_s_code'] = df.apply(lambda row: hsc_s_code(row), axis=1)
    df['degree_t_code'] = df.apply(lambda row: degree_t_code(row), axis=1)
    df['specialisation_code'] = df.apply(lambda row: specialisation_code(row), axis=1)
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