
"""Trabajo realizado por Ana María Velosa y Natalia Durán para el desarrollo del proyecto:
    Predicción de deterioro de pacientes COVID en el Hospital Militar Central de Bogotá.
    Este proyecto es promovido por la alianza de la Universidad de los Andes junto con
    el Hospital Militar Central.
    El proyecto es supervisado por el profesor Mario Valderrama y cuenta con asesoría de la
    Dra. Ledys Izquierdo.
    Parte de este trabajo se basó en el desarrollo realizado por Camilo Mayorquín.
"""
#Se importan los archivos con los diferentes modelos a procesar

from preprocessing.demografico_preprocessing import demo_preprocessing_pesos
from preprocessing.paraclinicos_preprocessing import paraclinicos_preprocessing
from preprocessing.sets_division import set_h2o
from models.RF_Grid.rf_grid_sintoma import rf_grid_sinto
from models.RF_Grid.rf_grid_comorbilidad import rf_grid_comorbilidad
from models.RF_Grid.rf_grid_demografico import rf_grid_demo

# demo_preprocessing_pesos('demograficos_20_ene.xlsx' ,"demo_pesos_20_ene")
# paraclinicos_preprocessing()

# Con pesos y ventilación

# set_h2o('demo_pesos_20_ene.xlsx', 0.70, 0.15, "demo_p_20_ene_sinto", 1, 1)
# set_h2o('demo_pesos_20_ene.xlsx', 0.70, 0.15, "demo_p_20_ene_comor", 2, 1)
# set_h2o('demo_pesos_20_ene.xlsx', 0.70, 0.15, "demo_p_20_ene", 3, 1)
# rf_grid_sinto('demo_p_20_ene_sinto', 1)
# rf_grid_comorbilidad('demo_p_20_ene_comor', 1)
# rf_grid_demo('demo_p_20_ene', 1)

# Mortalidad

# set_h2o('demo_pesos_20_ene.xlsx', 0.70, 0.15, "demo_p_20_ene_sinto_m", 1, 2)
# set_h2o('demo_pesos_20_ene.xlsx', 0.70, 0.15, "demo_p_20_ene_comor_m", 2, 2)
# set_h2o('demo_pesos_20_ene.xlsx', 0.70, 0.15, "demo_p_20_ene_m", 3, 2)

# rf_grid_sinto('demo_p_20_ene_sinto_m', 2)
# rf_grid_comorbilidad('demo_p_20_ene_comor_m', 2)
rf_grid_demo('demo_p_20_ene_m', 2)


