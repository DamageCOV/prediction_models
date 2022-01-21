
def rf_grid_sinto(file):
    import h2o

    # import random forest
    from h2o.estimators.random_forest import H2ORandomForestEstimator

    # stratified data set
    assignment_type = "Stratified"

    from h2o.grid import H2OGridSearch

    drf_hyper_params = {
        "ntrees": [25, 40, 50, 75, 100],
        "max_depth": [5, 7, 10],
        "sample_rate": [0.5, 0.75, 1.0]}

    grid_search_criteria = {"strategy": "RandomDiscrete",
                            "max_models": 50,
                            "seed": 12345}

    rf_grid = H2OGridSearch(model=H2ORandomForestEstimator(
        seed=1,
        nfolds=5,
        fold_assignment=assignment_type,
        balance_classes=True,
        categorical_encoding="auto",
        keep_cross_validation_predictions=True),
        hyper_params=drf_hyper_params,
        search_criteria=grid_search_criteria,
        grid_id="rf_grid")

    # import libraries
    import pandas as pd
    import numpy as np
    from tabulate import tabulate
    # machine learning framework
    h2o.init(nthreads=-1, max_mem_size=8)
    h2o.connect()
    import os

    path = os.path.abspath(os.getcwd())

    train_df = pd.read_excel(path + '\\output\\sets\\' + file + '_train.xlsx')
    valid_df = pd.read_excel(path + '\\output\\sets\\' + file + '_valid.xlsx')
    test_df = pd.read_excel(path + '\\output\\sets\\' + file + '_test.xlsx')

    h2o.init(nthreads=-1, max_mem_size=8)
    h2o.connect()

    y = 'Ventilacion'
    x = list(train_df.columns[2:21])

    train = h2o.H2OFrame(train_df)
    train = train.asfactor()

    valid = h2o.H2OFrame(valid_df)
    valid = valid.asfactor()

    test = h2o.H2OFrame(test_df)
    test = test.asfactor()

    rf_grid.train(x=x, y=y, training_frame=train, validation_frame=valid)

    best_drf_model_t = rf_grid.get_grid(sort_by='mcc', decreasing=True)
    best_drf_model = best_drf_model_t.models[0]

    print("Predicciones")
    drf_predictions = best_drf_model.predict(test_data=test)
    print("Termina predicciones")

    # performance
    best_drf_model.score_history()

    # print variable importance table
    print(tabulate(pd.DataFrame(best_drf_model.varimp()),
                   headers=['variable', 'relative importance', 'scaled importance', 'percentage'], tablefmt='psql'))

    # variable importance plot
    best_drf_model.varimp_plot()

    # print performance metrics
    print("Train performance")
    grid_rf_performance_train = best_drf_model.model_performance(train)
    print(grid_rf_performance_train)
    print("Valid performance")
    grid_rf_performance_valid = best_drf_model.model_performance(valid)
    print(grid_rf_performance_valid)
    print("Test performance")
    grid_rf_performance = best_drf_model.model_performance(test)
    print(grid_rf_performance)

    # shutdown per every trained model
    h2o.cluster().shutdown()
