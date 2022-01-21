
import numpy as np
import os
import pandas as pd


def set_h2o(file, ratio_t, ratio_v, file_s, t, p):
    # p=1 es predecir ventilación
    # p=2 es predecir mortalidad con ventilación como variable

    # t=1 es síntomas
    # t=2 es comorbilidades
    # t=3 es sintomas + comorbilidades
    # t=4 es signos vitales
    # t=5 es paraclínicos
    # t=6 es síntomas sin sesgos
    # t=7 es comorbilidades sin sesgos
    # t=8 es sintomas + comorbilidades sin sesgos
    # t=9 es síntomas con nuevas
    # t=10 es comorbilidades con nuevas
    # t=11 es sintomas + comorbilidades con nuevas
    import h2o
    assignment_type = "Stratified"
    h2o.init(nthreads=-1, max_mem_size=8)
    h2o.connect()
    path = os.path.abspath(os.getcwd())
    df = pd.read_excel(path + '\\output\\data_models\\' + file)
    df = df.drop(df.columns[[0]], axis=1)
    if t == 1 and p == 1:
        df_m = df.iloc[:, np.r_[0:20, 50], ]
    elif t == 2 and p == 1:
        df_m = df.iloc[:, np.r_[0:3, 20:51], ]
    elif t == 3 and p == 1:
        df_m = df.iloc[:, np.r_[0:51], ]
    elif t == 1 and p == 2:
        df_m = df.iloc[:, np.r_[0:20, 50, 52], ]
    elif t == 2 and p == 2:
        df_m = df.iloc[:, np.r_[0:3, 20:51, 52], ]
    elif t == 3 and p == 2:
        df_m = df.iloc[:, np.r_[0:51, 52], ]

    df_m = h2o.H2OFrame(df_m)
    df_m = df_m.asfactor()
    splits = df_m.split_frame(ratios=[ratio_t, ratio_v], seed=1)
    train = splits[0]
    valid = splits[1]
    test = splits[2]

    train_df = h2o.as_list(train)
    valid_df = h2o.as_list(valid)
    test_df = h2o.as_list(test)
    train_df = train_df.dropna()

    if p == 1:
        print("Train")
        print(train_df["Ventilacion"].value_counts())
        print("")
        print(("Valid"))
        print(valid_df["Ventilacion"].value_counts())
        print("")
        print(("Test"))
        print(test_df["Ventilacion"].value_counts())
    elif p == 2:
        print("Train")
        print(train_df["Mortalidad"].value_counts())
        print("")
        print(("Valid"))
        print(valid_df["Mortalidad"].value_counts())
        print("")
        print(("Test"))
        print(test_df["Mortalidad"].value_counts())

    train_df.to_excel(path + "\\output\\sets\\"+file_s+"_train.xlsx", sheet_name='sheet1')
    valid_df.to_excel(path + "\\output\\sets\\"+file_s+"_valid.xlsx", sheet_name='sheet1')
    test_df.to_excel(path + "\\output\\sets\\"+file_s+"_test.xlsx", sheet_name='sheet1')




def set_train_valid_test(set_dir, train_p, valid_p, test_p):
    data = pd.read_excel(set_dir)
    train_c = data.shape[0]*train_p/100
    valid_c = data.shape[0]*valid_p/100
    test_c = data.shape[0]*test_p/100



