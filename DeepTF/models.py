"""
Built all models for evaluation
Current proposed models for Predicting TFs are:
    -RF and/or GradientBoosting
    - CNN / LSTM
    - Transformers / Self attention
"""
import pandas as pd
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

"""
TODO:
    - Convert protein sequence into onehot (categorical -> numerical)
    - Try to atleast finish 
"""

class CNN_module(nn.module):
    """
    Own implementation of CNN classifier for TF predicting
    """
    def __init__(self):
        super().__init__()
        pass

    def foward(self):
        pass

    def fit(self):
        pass

class LSTM_module(nn.module):
    """
    Own implementation of LSTM classifier for TF prediction
    """
    def __init__(self):
        pass

    def foward(self):
        pass

    def fit(self):
        pass

class attention_module(nn.module):
    """
    Own implementation of Transformer for TF prediction
    """
    def __init__(self):
        pass

class RF_module(RandomForestClassifier):
    """
    Own implementation of RF for TF prediction
    """
    def __init__(self, data):
        super().__init__()
        self.data = data

    @classmethod
    def split(self, data):
        X_train, X_test, y_train, y_test = train_test_split(data["enc"], data["marker"])
        # we need to format data further due to our procedure when applying Encoder
        # This should already be refactored: X_train and X_test need to be formatted
        new_train = []
        new_test = []
        for arr in X_train:
            new_train.append(arr.flatten())
        X_train = np.asarray(new_train)
        for arr in X_test:
            new_test.append(arr.flatten())
        X_test = np.asarray(new_test)  

        return X_train, X_test, y_train, y_test
    def fit(self):
        pass
    
    def predict(self):
        pass

    def metric(self):
        pass