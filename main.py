import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

# print(df.groupby("level")["attempt"].mean())

level = ["level1", "level2", "level3", "level4"]

fig = go.Figure(go.Bar(x=df.groupby("level")["attempt"].mean(), y=level, orientation="h"))
fig.show()