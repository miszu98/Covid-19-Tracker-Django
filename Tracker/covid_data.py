import pandas as pd

URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"


def get_updated_data():
    dataset = pd.read_csv(URL)
    details = []
    for x in range(274):
        list = []
        for z in dataset.iloc[x]:
            list.append(z)
        details.append((list[0], list[1], list[-1]))
    return details


def get_total_cases():
    s = 0
    for x in get_updated_data():
        s += x[2]
    return s

