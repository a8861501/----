import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def bar():
    
    df = pd.read_excel('final.xlsx', sheet_name='Sheet1')

    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])
    # 把df按照上映日期欄位排序
    df = df.sort_values(by='上映日期')
    
    df = df[(df['上映日期'] > '2020-01-01') & (df['上映日期'] < '2023-04-28')]
    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)
    
    # 把df['上映日期']跟df['中文片名']一樣的df['銷售票數']相加
    df = df.groupby(['上映日期'])['銷售票數'].sum().reset_index()

    x = df[df['上映日期'] > '2020-01-01']['上映日期']
    y = df[df['上映日期'] > '2020-01-01']['銷售票數']

    plt.rc('font', family='Microsoft JhengHei') # 讓matplotlib可以顯示中文
    # 長條圖
    plt.bar(x, y, width=10)
    # 把Y軸的刻度設為整數
    plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    # 把圖放大一點
    plt.gcf().set_size_inches(10, 5)
    plt.xticks(pd.date_range('2020-01-01', '2023-5-31', freq='M'), rotation=90)
    # 把X軸Y軸的名稱加上去
    plt.xlabel('上映日期')
    plt.ylabel('銷售票數')
    plt.title('電影累計銷售金額與時間變化')
    plt.show()

def numOFtheather_and_sell():
    df = pd.read_excel('final.xlsx', sheet_name='Sheet1')
    df = df.sort_values(by='上映院數') 
    
    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)
    
    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])

    x = df[df['上映日期'] > '2020-01-01']['上映院數']
    y = df[df['上映日期'] > '2020-01-01']['銷售票數']

    # 讓matplotlib可以顯示中文
    plt.rc('font', family='Microsoft JhengHei') 
    # 長條圖
    plt.bar(x, y, width=0.3)
    # 把Y軸的刻度設為整數
    plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    # 把圖放大一點
    plt.gcf().set_size_inches(10, 5)

    plt.xlabel('上映院數')
    plt.ylabel('銷售票數')
    plt.title('電影銷售票數與上映院數關係')
    plt.show()

if __name__ == '__main__':
    bar()
    # numOFtheather_and_sell()