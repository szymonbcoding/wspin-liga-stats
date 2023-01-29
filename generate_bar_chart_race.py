import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv("data/main_csv/m.csv", index_col='time')
bcr.bar_chart_race(
    df=df,
    filename = 'wspinliga_male.mp4',
    n_bars=16,
    title = 'Noworoczna Liga Wspinaczkowa Mężyczyźni'
)