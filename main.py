import pandas as pd

study_hours = {"Saturday": 2.5,
"Sunday": 3,
"Monday": 1.5,
"Tuesday": 4,
"Wednesday": 0,
"Thursday": 3.5,
"Friday": 2}

series = pd.Series(study_hours)

#A#  understand the obj
#print(series.values)
#print(series.index)
#print(series.dtypes)
#print(series.size)
#print(series.shape)
#print(series.name)

#B#  selecting data
#print(series.loc["Saturday":"Monday"])
#print(series.loc["Friday"])
#print(series.iloc[:3])
#print(series.iloc[5:])

#C#  filtering
#print(series > 2)
#print(series == 0)
#print(series.between(2, 3.5))
#print(series > 0)
#print((series > 3).sum())

#D#  calculations
#print(series.sum())
#print(series.mean())
#print(min(series))
#print(max(series))
#print(series.median())
#print(series.count())
#print(series.idxmin())
#print(series.idxmax())

#E# vectorized operations
#series_second = series + 0.5
#print(series_second)
#series_mins = series * 60
#print(series_mins)
#print(series * 2)
#print(series - 1)
#print(series >= 3)

#F# sorting
#print(series.sort_values())
#print(series.sort_values(ascending=False))
#print(series.sort_index(ascending=False))
#print(series.sort_values())
#print(series.sort_values(ascending=False))

#G# editing safely
#copy_series = series.copy()
#copy_series["Wednesday"] = 2
#copy_series["Extra"] = 1.5
#del copy_series["Extra"]
#print(copy_series)