
import numpy as np
import os
import pandas as pd


def set_train_valid_test(set_dir, train_p, valid_p, test_p):
    data = pd.read_excel(set_dir)
    train_c = data.shape[0]*train_p/100
    valid_c = data.shape[0]*valid_p/100
    test_c = data.shape[0]*test_p/100



