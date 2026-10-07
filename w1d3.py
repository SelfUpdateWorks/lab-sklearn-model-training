import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()

print(type(cancer_data))
print(cancer_data.data.shape)
print(cancer_data.feature_names[:5])
print(cancer_data.target_names)