import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('分析資料/totalHighSell.csv', encoding='utf-8')
df.to_excel('分析資料/totalsell.xlsx', index=False)
df = pd.read_excel('分析資料/totalsell.xlsx',sheet_name='Sheet1')

# 把df的上映日期欄位轉成日期格式
df['上映日期'] = pd.to_datetime(df['上映日期'])

plt.rc('font', family='Microsoft JhengHei') # 讓matplotlib可以顯示中文

def holiday_pie(df):
    # 計算df['假日']為1的數量
    df1 = df.groupby(['假日'])['銷售票數'].count().reset_index()  
    df = df.groupby(['假日'])['銷售票數'].sum().reset_index()
    x = df['銷售票數']/df1['銷售票數']
   
    # 把df畫成一個圓餅圖，讓圖例顯示df['假日']，並且顯示百分比到小數點第一位
    x.plot(kind='pie', y='銷售票數', labels=df['假日'], autopct='%1.1f%%')
    plt.show()

def kind_pie(df):
    # 計算df['假日']為1的數量
    df1 = df.groupby(['類型'])['銷售票數'].count().reset_index() 
    # 把df['假日']為1的df['銷售票數']相加
    df = df.groupby(['類型'])['銷售票數'].sum().reset_index()
    x = df['銷售票數']/df1['銷售票數']
    # 把df畫成一個圓餅圖，讓圖例顯示df['假日']，並且顯示百分比到小數點第一位
    x.plot(kind='pie', y='銷售票數', labels=df['類型'], autopct='%1.1f%%')
    plt.show()

def metrix(df):
    # 把df['假日']為0跟df['類型']也為0的數量相加
    df1 = df.groupby(['假日', '類型'])['銷售票數'].count().reset_index()
  
    # 把假日跟類型組成4個組合
    df = df.groupby(['假日', '類型'])['銷售票數'].sum().reset_index()
    # 把df['銷售票數']除以df1['銷售票數']
    x = (df['銷售票數']/df1['銷售票數']).round(2)
    # 把df畫成一個圓餅圖，讓圖例顯示['假日_感官刺激','假日_非感官刺激','平日_感官刺激','平日_非感官刺激']，並且顯示百分比到小數點第一位
    x.plot(kind='pie', y='銷售票數', labels=['平日_非感官刺激','平日_感官刺激','假日_非感官刺激','假日_感官刺激'], autopct='%1.1f%%')
    plt.show()

if __name__ == '__main__':
    # holiday_pie(df)
    # kind_pie(df)
    metrix(df)