import pandas as pd

df = pd.DataFrame()

f = open("7_new_new.txt")
SNR_sum = 0
count_of_SNR = 0
startcol = 0

for line in f:

    if 'Power' in line:
        if count_of_SNR != 0:
            df = df.append({'SNR': SNR_sum / count_of_SNR, 'probability': count_of_SNR / 10}, ignore_index=True)
            SNR_sum = 0
            count_of_SNR = 0

    SNR_positions = line.find('SNR:')
    if SNR_positions > 0:
        SNR = int(line[SNR_positions + 5:-4])
        SNR_sum += SNR
        count_of_SNR += 1

    if "SF:" in line:

        if count_of_SNR != 0:
            df = df.append({'SNR': SNR_sum / count_of_SNR, 'probability': count_of_SNR / 10}, ignore_index=True)
            SNR_sum = 0
            count_of_SNR = 0
        df = df.sort_values(by=["probability", 'SNR'])
        with pd.ExcelWriter(f'result.xlsx', mode="a", engine="openpyxl", if_sheet_exists="overlay", ) as writer:
            df.to_excel(writer, index=False, startcol=startcol, )
        del df
        df = pd.DataFrame()
        startcol += 3

if count_of_SNR != 0:
    df = df.append({'SNR': SNR_sum / count_of_SNR, 'probability': count_of_SNR / 10}, ignore_index=True)
    SNR_sum = 0
    count_of_SNR = 0
df = df.sort_values(by=["probability", 'SNR'])
with pd.ExcelWriter(f'result.xlsx', mode="a", engine="openpyxl", if_sheet_exists="overlay", ) as writer:
    df.to_excel(writer, index=False, startcol=startcol, )
del df
df = pd.DataFrame()
startcol += 3
