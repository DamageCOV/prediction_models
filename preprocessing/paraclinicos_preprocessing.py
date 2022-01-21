
import numpy as np
import os
import pandas as pd

def paraclinicos_preprocessing():
    path = os.path.abspath(os.getcwd())
    path_d = path + '\\input\\paraclinicos_2022.xlsx'

    data = pd.read_excel(path_d)

    df = data.iloc[np.r_[0:data.shape[0]], :]
    #Grupo 1
    print(df.shape[0])
    df = df.drop(df.columns[[3, 4, 5, 6, 7, 9, 25, 26, 27, 28, 29, 30]], axis=1)
    df =df.dropna()
    print("Grupo 1")
    print(df.shape[0])

    #Prueba 2
    # Dimero D
    df_2_d = data.iloc[np.r_[0:data.shape[0], :]]
    df_2_d =df_2_d.drop(df_2_d.columns[[3, 4, 6, 7, 9, 25, 26, 27, 28, 29, 30]], axis=1)
    #Se eliminan las filas que tengan algún vacío en la variable de interés
    df_2_d = df_2_d.dropna(subset=['Dimero D'])
    print("Grupo 2 Dimero")
    print(df_2_d.shape[0])
    df_2_d = df_2_d.dropna()
    print(df_2_d.shape[0])

    # Ferritina
    df_2_f = data.iloc[np.r_[0:data.shape[0], :]]
    df_2_f = df_2_f.drop(df_2_f.columns[[3, 4, 5, 7, 9, 25, 26, 27, 28, 29, 30]], axis=1)
    # Se eliminan las filas que tengan algún vacío en la variable de interés
    df_2_f = df_2_f.dropna(subset=['Ferritina'])
    print("Grupo 2 Ferritinina")
    print(df_2_f.shape[0])
    df_2_f = df_2_f.dropna()
    print(df_2_f.shape[0])

    # Troponina
    df_2_t = data.iloc[np.r_[0:data.shape[0], :]]
    df_2_t = df_2_t.drop(df_2_t.columns[[3, 4, 5, 6, 9, 25, 26, 27, 28, 29, 30]], axis=1)
    # Se eliminan las filas que tengan algún vacío en la variable de interés
    df_2_t = df_2_t.dropna(subset=['Troponina'])
    print("Grupo 2 Troponina")
    print(df_2_t.shape[0])
    df_2_t = df_2_t.dropna()
    print(df_2_t.shape[0])

    # Bilirrubina
    df_2_b = data.iloc[np.r_[0:data.shape[0], :]]
    df_2_b = df_2_b.drop(df_2_b.columns[[3, 4, 5, 6, 7, 25, 26, 27, 28, 29, 30]], axis=1)
    # Se eliminan las filas que tengan algún vacío en la variable de interés
    df_2_b = df_2_b.dropna(subset=['Bilirrubina'])
    print("Grupo 2 Bilirrubina")
    print(df_2_b.shape[0])
    df_2_b = df_2_b.dropna()
    print(df_2_b.shape[0])

    #Prueba 3
    # Grupo sin signos vitales
    df_3 = data.iloc[np.r_[0:data.shape[0]], :]
    df_3 = df_3.drop(df_3.columns[[3, 4, 5, 6, 7, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], axis=1)

    #Prueba 4

    #Prueba 5
    #Estadisticos

    #Promedio

    df_5_p = data.iloc[np.r_[0:data.shape[0]], :]
    df_5_p = df_5_p.drop(df_5_p.columns[[3, 4, 5, 6, 7, 9, 25, 26, 27, 28, 29, 30]], axis=1)
    df_5_p = df_5_p.dropna(subset=['Paciente'])


    g1_mean = df_5_p[["Paciente","Linfocitos","Plaquetas", "Urea","SO2", "CO2", "PO2", "FiO2","Creatinina","pH", \
                     "FR", "S","D","FC","Glasgow","Temperatura","PAM"] ].groupby("Paciente").mean()
    print("Cantidad pacientes:")
    print(g1_mean.shape[0])
    print(df_5_p)
    # print("Llenar vacíos")
    #
    # for i in range(0,df_5_p.shape[0]-1):
    #     if df_5_p.iloc[i,1].isna():
    #         p = g1_mean.index(df_5_p.iloc[i, 0])
    #         df_5_p.iloc[i, 1].replace(g1_mean(p,0))
    #
    # print(df_5_p)





    g1_median = df_5_p[["Paciente", "Linfocitos", "Plaquetas", "Urea","SO2", "CO2", "PO2", "FiO2","Creatinina","pH", \
                     "FR", "S","D","FC","Glasgow","Temperatura","PAM"] ].groupby("Paciente").median()

    # g1_mode = df_5_p[["Paciente", "Linfocitos", "Plaquetas", "Urea", "SO2", "CO2", "PO2", "FiO2", "Creatinina", "pH", \
                       # "FR", "S", "D", "FC", "Glasgow", "Temperatura", "PAM"]].groupby("Paciente").mode()

    g1_std = df_5_p[["Paciente", "Linfocitos", "Plaquetas", "Urea", "SO2", "CO2", "PO2", "FiO2", "Creatinina", "pH", \
                        "FR", "S", "D", "FC", "Glasgow", "Temperatura", "PAM"]].groupby("Paciente").std()
    # pacientes= []
    # posiciones= []
    # for i in range(0,df_5_p.shape[0]-2):
    #     if df_5_p.iloc[i,0] != df_5_p.iloc[i+1,0]:
    #         pacientes.append(df_5_p.iloc[i,0])
    #         posiciones.append(i)
    #
    # promedios = []
    # for c in range(0,len(pacientes)):
    #     promedios.append(df.iloc[(.mean())





