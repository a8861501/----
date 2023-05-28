import pandas as pd

def twenty_March():
    df = pd.read_excel('final.xlsx',sheet_name='Sheet1')

    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])
    # 只保留df['上映日期']'2020-02-29'到'2020-03-30'的時間
    df = df[(df['上映日期'] > '2020-02-29') & (df['上映日期'] < '2020-03-30')]

    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)

    # 把df['上映日期']跟df['中文片名']一樣的df['銷售票數']相加
    df = df.groupby(['上映日期', '中文片名'])['銷售票數'].sum().reset_index()
    # 把df['銷售票數']不為0的寫進一個csv檔
    df[df['銷售票數'] != 0].to_csv('分析資料/twenty_March.csv', index=False)

    print(df[df['銷售票數'] != 0])

def twenty_Nov():
    df = pd.read_excel('final.xlsx',sheet_name='Sheet1')

    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])
    # 只保留df['上映日期']'2020-02-29'到'2020-03-30'的時間
    df = df[(df['上映日期'] > '2020-10-25') & (df['上映日期'] < '2020-11-30')]
    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)

    # 把df['上映日期']跟df['中文片名']一樣的df['銷售票數']相加
    df = df.groupby(['上映日期', '中文片名'])['銷售票數'].sum().reset_index()
    # 把df['銷售票數']不為0的寫進一個csv檔
    df[df['銷售票數'] != 0].to_csv('分析資料/twenty_Nov.csv', index=False)


    print(df[df['銷售票數'] != 0])
def tewntyOne_Feb():
    df = pd.read_excel('final.xlsx',sheet_name='Sheet1')

    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])
    # 只保留df['上映日期']'2020-02-29'到'2020-03-30'的時間
    df = df[(df['上映日期'] > '2021-01-25') & (df['上映日期'] < '2021-02-25')]
    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)

    # 把df['上映日期']跟df['中文片名']一樣的df['銷售票數']相加
    df = df.groupby(['上映日期', '中文片名'])['銷售票數'].sum().reset_index()
    # 把df['銷售票數']不為0的寫進一個csv檔
    df[df['銷售票數'] != 0].to_csv('分析資料/twentyOne_Feb.csv', index=False)
    print(df)

def twentyOne_Apr():
    df = pd.read_excel('final.xlsx',sheet_name='Sheet1')
    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])
    # 只保留df['上映日期']'2020-02-29'到'2020-03-30'的時間
    df = df[(df['上映日期'] > '2021-03-25') & (df['上映日期'] < '2021-04-20')]
    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)

    # 把df['上映日期']跟df['中文片名']一樣的df['銷售票數']相加
    df = df.groupby(['上映日期', '中文片名'])['銷售票數'].sum().reset_index()
    # 把df['銷售票數']不為0的寫進一個csv檔
    df[df['銷售票數'] != 0].to_csv('分析資料/twentyOne_Apr.csv', index=False)
    print(df[df['銷售票數'] != 0])

def twentyOne_Nov():
    df = pd.read_excel('final.xlsx',sheet_name='Sheet1')
    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])
    # 只保留df['上映日期']'2020-02-29'到'2020-03-30'的時間
    df = df[(df['上映日期'] > '2021-11-01') & (df['上映日期'] < '2021-11-30')]
    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)

    # 把df['上映日期']跟df['中文片名']一樣的df['銷售票數']相加
    df = df.groupby(['上映日期', '中文片名'])['銷售票數'].sum().reset_index()
    # 把df['銷售票數']不為0的寫進一個csv檔
    df[df['銷售票數'] != 0].to_csv('分析資料/twentyOne_Nov.csv', index=False)
    print(df[df['銷售票數'] != 0])

def twentyTwo_March():
    df = pd.read_excel('final.xlsx',sheet_name='Sheet1')
    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])
    # 只保留df['上映日期']'2020-02-29'到'2020-03-30'的時間
    df = df[(df['上映日期'] > '2022-03-01') & (df['上映日期'] < '2022-03-30')]
    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)

    # 把df['上映日期']跟df['中文片名']一樣的df['銷售票數']相加
    df = df.groupby(['上映日期', '中文片名'])['銷售票數'].sum().reset_index()
    # 把df['銷售票數']不為0的寫進一個csv檔
    df[df['銷售票數'] != 0].to_csv('分析資料/twentyTwo_Mar.csv', index=False)
    print(df[df['銷售票數'] != 0])

def twentyThree_Feb():
    df = pd.read_excel('final.xlsx',sheet_name='Sheet1')
    # 把df的上映日期欄位轉成日期格式
    df['上映日期'] = pd.to_datetime(df['上映日期'])
    # 只保留df['上映日期']'2020-02-29'到'2020-03-30'的時間
    df = df[(df['上映日期'] > '2023-01-31') & (df['上映日期'] < '2023-02-28')]
    # 把df['累計銷售票數']欄位轉成整數格式
    df['銷售票數'] = df['銷售票數'].str.replace(',', '').fillna(0).astype(int)

    # 把df['上映日期']跟df['中文片名']一樣的df['銷售票數']相加
    df = df.groupby(['上映日期', '中文片名'])['銷售票數'].sum().reset_index()
    # 把df['銷售票數']不為0的寫進一個csv檔
    df[df['銷售票數'] != 0].to_csv('分析資料/twentyThree_Feb.csv', index=False)
    print(df[df['銷售票數'] != 0])

if __name__=='__main__':
    # twenty_March()
    # twenty_Nov()
    # tewntyOne_Feb()
    # twentyOne_Apr()
    # twentyOne_Nov()
    # twentyTwo_March()
    twentyThree_Feb()