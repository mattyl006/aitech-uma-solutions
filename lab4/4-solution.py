import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib

data = pd.read_csv('mieszkania4.tsv', sep='\t')
columnsToDrop = ['cena', 'Liczba pokoi', 'Miejsce parkingowe', 'Garaż', 'Liczba pięter w budynku', 'Piętro', 'Typ zabudowy', 'Okna', 'Materiał budynku', 
'Forma własności', 'Forma kuchni', 'Stan', 'Stan instalacji', 'Głośność', 'Droga dojazdowa', 'Stan łazienki', 'Powierzchnia działki w m2', 'opis']
data = data.drop(columns=columnsToDrop)
data = data.dropna()
data = (data - data.min())/(data.max() - data.min())
data_train, data_test = train_test_split(data, test_size=0.2, random_state=1)
print(len(data_train))
print(len(data_test))