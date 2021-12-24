import pandas as pd
import json
import time
from faker import Factory,Faker
import numpy as np
from urllib import request

url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
response = request.urlopen(url)
contenido = response.read()
df = pd.read_json(contenido)
bn = pd.DataFrame(df.features.values.tolist())['tags']
pd.DataFrame(bn)




