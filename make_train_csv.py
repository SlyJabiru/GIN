import numpy as np
import pandas as pd
import random
import datetime


#  -----------------------------------
# | timestamp  |  energy  |
#  -----------------------------------

# TODO: image_name 에서 png 빼기.
# COT 하고 CLL 은 파일 이름 똑같게.

colnames=['timestamp', 'energy']

dtypes = {'timestamp': 'str', 'energy': 'float'}
parse_dates = ['timestamp']

df = pd.read_csv('./SolarPV_Elec_Problem.csv', names=colnames, header=None, dtype=dtypes, parse_dates=parse_dates)

size = len(df)
i = 3

data = []

while i <= size:
    d1 = "202002010030"
    d2 = "202002082350"
    # d1 = datetime.datetime(2020, 2, 1, 0, 30)
    # d2 = datetime.datetime(2020, 2, 8, 23, 50)

    ts = df['timestamp'][i-1].strftime("%Y%m%d%H%M")
    if ts < d1 or ts >= d2:
        i += 2
        continue

    energy_sum = df[i-2:i]['energy'].sum()

    temp = [ts, energy_sum]
    # print(temp)
    data.append(temp)

    i += 2

random.shuffle(data)
threshold = int(len(data) * 0.8)
train_data = data[:threshold]
test_data = data[threshold:]

train_df = pd.DataFrame(train_data, columns=['timestamp', 'energy'])
test_df = pd.DataFrame(test_data, columns=['timestamp', 'energy'])

train_df.to_csv('~/PycharmProjects/GIN/train.csv', header=False, index=False)
test_df.to_csv('~/PycharmProjects/GIN/test.csv', header=False, index=False)
