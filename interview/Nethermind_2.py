import numpy as np
import pandas as pd


def solution(files):
    result = []

    for file in files:
        dataframe_list = []

        df = pd.read_csv(file)

        # Calculate highest volume
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].dt.year

        max_volume_per_year = df.loc[df.groupby('year')['vol'].idxmax()]

        max_volume_per_year = max_volume_per_year[['date', 'vol']]

        dataframe_list.append(max_volume_per_year)

        # Highest closing price

        max_close_per_year = df.groupby('year')['close'].max()

        merged_close = pd.merge(df, max_close_per_year, on=['year', 'close'], how='inner')

        dataframe_list.append(merged_close)

        result.append(dataframe_list)

    return result


files = ['./data/framp.csv', './data/gnyned.csv', './data/gwoomed.csv', './data/hoilled.csv', './data/plent.csv', './data/throwsh.csv', './data/twerche.csv', './data/veeme.csv']

r = solution(files)

dates_list = ['2005-09-29', '2006-05-11', '2007-10-23', '2008-01-08', '2009-07-30', '2010-11-12', '2011-07-07', '2011-07-08', '2012-12-28', '2013-08-07', '2014-09-23', '2015-10-08', '2016-08-11', '2017-08-28', '2017-08-30', '2018-12-07', '2019-01-23']
close_list = [2.8489, 2.8489, 4.5976, 4.1227, 3.6434, 3.2556, 3.8671, 3.8671, 4.4573, 5.723, 4.7138, 6.4497, 5.4336, 6.875, 6.875, 7.0, 7.51]

assert dates_list == r[0][1]['date'].dt.strftime('%Y-%m-%d').to_list()
assert close_list == r[0][1]['close'].to_list()

