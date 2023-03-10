import bar_chart_race as bcr
import pandas as pd

def generate_bcr(male: bool):
    if(male):
        df = pd.read_csv("data/main_csv/m.csv", index_col='time')
        title = 'Noworoczna Liga Wspinaczkowa - Mężyczyźni'
        filename = 'data/mp4/wspinliga_male.mp4'
    else:
        df = pd.read_csv("data/main_csv/f.csv", index_col='time')
        title = 'Noworoczna Liga Wspinaczkowa - Kobiety '
        filename = 'data/mp4/wspinliga_female.mp4'

    bcr.bar_chart_race(
    df=df,
    filename = filename,
    n_bars=16,
    period_length=125,
    title = title
)