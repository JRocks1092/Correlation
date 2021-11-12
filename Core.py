from re import X
import pandas as pd
import numpy as np
import plotly.express as px

def getdata(array = []):
    ar = []
    for i in array:
        ar.append(float(i))
    return ar

df = pd.read_csv("data.csv")
Marks = df["Marks In Percentage"].tolist()
daysPresent = df["Days Present"].tolist()

Marks = getdata(Marks)
daysPresent = getdata(daysPresent)

coeff = np.corrcoef(Marks, daysPresent)
print("Correlation is "+str(coeff[0][1]))

gr = px.scatter(x=Marks, y=daysPresent)
gr.show()