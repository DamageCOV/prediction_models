"""
Se presenta el procesamiento que se debe hacer del archivo original de demográficos para los modelos
"""
import numpy as np
import os
import pandas as pd


def demo_preprocessing_pesos(file, file_n):
    # Abrir el archivo
    path = os.path.abspath(os.getcwd())
    path_d = path + '\\input\\'+file

    data = pd.read_excel(path_d)

    # Eliminar columnas que no se van a usar
    df = data.iloc[np.r_[0:data.shape[0]], :]
    df = df.drop(df.columns[[3, 21, 22, 30, 53, 56, 57, 58, 59, 60, 63, 64, 65]], axis=1)

    # Asignar pesos
    df.loc[(df['Mortalidad'] == "Muerto "), 'Mortalidad'] = "Muerto"
    df.loc[(df['Mortalidad'] == "Vivo "), 'Mortalidad'] = "Vivo"

    df.loc[(df['Genero'] == "Masculino "), 'Genero'] = "Masculino"
    df.loc[(df['Genero'] == "Femenino "), 'Genero'] = "Femenino"

    var_principal = {"Genero": {"Masculino": 0, "Femenino": 1},
                     "Ventilacion": {1: "Invasiva", 0: "No invasiva"},
                     "Mortalidad": {1: "Vivo", 0: "Muerto"}
                     }

    df = df.replace(var_principal)

    df.loc[df['Edad'] < 70, 'Edad'] = 5
    df.loc[df['Edad'] >= 70, 'Edad'] = 0

    df.loc[(df['Tos'] == 1), 'Tos'] = 5
    df.loc[(df['Diarrea'] == 1), 'Diarrea'] = 3
    df.loc[(df['Dificultad respiratoria si disnea y si taquipnea'] == 1), 'Dificultad respiratoria si disnea y si taquipnea'] = 5
    df.loc[(df['Dolor abdominal'] == 1), 'Dolor abdominal'] = 1
    df.loc[(df['Dolor toracico'] == 1), 'Dolor toracico'] = 4
    df.loc[(df['Escalofrios'] == 1), 'Escalofrios'] = 4
    df.loc[(df['Fiebre'] == 1), 'Fiebre'] = 5
    df.loc[(df['Malestar General'] == 1), 'Malestar General'] = 4
    df.loc[(df['Mialgia'] == 1), 'Mialgia'] = 3
    df.loc[(df['Nauseas'] == 1), 'Nauseas'] = 3
    df.loc[(df['Odinofagia'] == 1), 'Odinofagia'] = 3
    df.loc[(df['Hiporexia (Perdida del apetito)'] == 1), 'Hiporexia (Pedida del apetito)'] = 1
    df.loc[(df['Anosmia (Perdida del olfato)'] == 1), 'Anosmia (Perdida del olfato)'] = 5
    df.loc[(df['Cefalea'] == 1), 'Cefalea'] = 3
    df.loc[(df['Taquipnea'] == 1), 'Taquipnea'] = 5
    df.loc[(df['Vomito (Episodios emeticos)'] == 1), 'Vomito (Episodios emeticos)'] = 3

    df.loc[(df['Asma'] == 1), 'Asma'] = 3
    df.loc[(df['EPOC'] == 1), 'EPOC'] = 5
    df.loc[(df['Diabetes'] == 1), 'Diabetes'] = 5
    df.loc[(df['VIH'] == 1), 'VIH'] = 2
    df.loc[(df['Enfermedad coronaria'] == 1), 'Enfermedad coronaria'] = 5
    df.loc[(df['Falla Cardiaca'] == 1), 'Falla Cardiaca'] = 5
    df.loc[(df['Enfermedad Valvular'] == 1), 'Enfermedad Valvular'] = 5
    df.loc[(df['Cancer'] == 1), 'Cancer'] = 5
    df.loc[(df['Desnutricion'] == 1), 'Desnutricion'] = 3
    df.loc[(df['Obesidad'] == 1), 'Obesidad'] = 3
    df.loc[(df['Enfermedad renal'] == 1), 'Enfermedad renal'] = 3
    df.loc[(df['Tabaquismo'] == 1), 'Tabaquismo'] = 4
    df.loc[(df['Tuberculosis'] == 1), 'Tuberculosis'] = 2
    df.loc[(df['Hipertension'] == 1), 'Hipertension'] = 5
    df.loc[(df['Enfermedades reumaticas'] == 1), 'Enfermedades reumaticas'] = 3
    df.loc[(df['Transtornos neurologicos cronicos'] == 1), 'Transtornos neurologicos cronicos'] = 2
    df.loc[(df['Enfermedad hematologica cronica'] == 1), 'Enfermedad hematologica cronica'] = 2
    df.loc[(df['Enfermedad hepatica cronica'] == 1), 'Enfermedad hepatica cronica'] = 2
    df.loc[(df['Alcoholismo'] == 1), 'Alcoholismo'] = 2
    df.loc[(df['Lupus eritematoso sistemico'] == 1), 'Lupus eritematoso sistemico'] = 3

    # Guardar nuevo archivo
    path_out = path + "\\output\\data_models\\"+file_n+".xlsx"
    df.to_excel(path_out)

    # Imprimir estadísticas en consola
    print(df["Ventilacion"].value_counts())
    print(df["Mortalidad"].value_counts())
    print(df["Genero"].value_counts())
