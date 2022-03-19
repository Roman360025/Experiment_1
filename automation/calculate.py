import pandas as pd
import shutil
from zipfile import ZipFile
import os


df = pd.DataFrame()

sf = 12

f = open(f"{sf}.txt")
SNR_sum = 0
count_of_SNR = 0
power = -12124141
for line in f:
    if 'Power' in line:
        if count_of_SNR != 0:
            # print(SNR_sum / count_of_SNR, count_of_SNR / 100)
            df = df.append({'SNR': SNR_sum / count_of_SNR, 'probability': count_of_SNR / 100}, ignore_index=True)
            SNR_sum = 0
            count_of_SNR = 0
        # power = int(re.findall(r'[-+]?\d+', line)[0])
        # print(power, ':', end='')
    SNR_positions = line.find('SNR:')
    if SNR_positions > 0:
        SNR = int(line[SNR_positions + 5:-4])
        SNR_sum += SNR
        count_of_SNR += 1

if count_of_SNR != 0:
    df = df.append({'SNR': SNR_sum / count_of_SNR, 'probability': count_of_SNR / 100}, ignore_index=True)
    SNR_sum = 0
    count_of_SNR = 0

df = df.sort_values(by=["probability", 'SNR'])
# df.to_csv('12.csv', mode='a', sep=';', index=False, float_format="%.3f")
df.to_excel(f'{sf}.xlsx', index=False)