import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")

print(df.groupby("student_id")["attempt"].mean())

# studentDF = df.loc[df["student_id"] == "TRL_123"]
# level = ["level1", "level2", "level3", "level4"]

# fig = go.Figure(
#     go.Bar(x=studentDF.groupby("level")["attempt"].mean(),
#           y=level,
#           orientation="h"))
# fig.show()

# studentDF = df.loc[df["student_id"] == "TRL_987"]
# level = ["level1", "level2", "level3", "level4"]

# fig = go.Figure(
#     go.Bar(x=studentDF.groupby("level")["attempt"].mean(),
#           y=level,
#           orientation="h"))
# fig.show()

studentDF = df.loc[df["student_id"] == "TRL_xsl"]
level = ["level1", "level2", "level3", "level4"]

fig = go.Figure(
    go.Bar(x=studentDF.groupby("level")["attempt"].mean(),
          y=level,
          orientation="v"))
fig.show()