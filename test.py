
#  Import python libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os

if os.path.exists('iris.dat'):
    with open('iris.dat') as f:
        data = f.read()
    print(data)
else:
    import requests
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    response = requests.get(url)
    with open('iris.dat', 'wb') as f:
        f.write(response.content)
    with open('iris.dat') as f:
        data = f.read()
    print(data)