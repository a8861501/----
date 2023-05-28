import pandas as pd

def delete():
    df = pd.read_csv('merge.csv',encoding='utf-8')
    # 刪除有國別地區,中文片名,上映日期,上映院數,銷售票數,銷售金額,累計銷售票數,累計銷售金額文字的行
    df = df.drop(df[df['國別地區']=='國別地區'].index)
    df.to_csv('clean.csv',encoding='utf-8',index=False)

def select():
    # 選擇國別地區為中華民國的行
    df = pd.read_csv('clean.csv',encoding='utf-8')
    df = df[df['國別地區']=='中華民國']
    df.to_csv('clean.csv',encoding='utf-8',index=False)

def to_ecel():
    df = pd.read_csv('clean.csv',encoding='utf-8')
    df.to_excel('clean.xlsx',index=False)
    
if __name__=='__main__':
    # delete() # 把重複的標題行刪掉
    to_ecel() # 轉成excel檔
    # select() # 選擇國別地區為中華民國的行