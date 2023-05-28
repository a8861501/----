import os
import pandas as pd

delete_columns = ['序號','申請人','周票數變動率','週票數變動率','出品','票數變動率','上映日數','發行']

def get_files():
    for file_path,dirnames,filenames in os.walk(r'./原始資料'):
        dirnames.sort()
        for filename in filenames:
            path = os.path.join(file_path+'/'+filename)
            fl = pd.read_csv(path,encoding='utf-8')
            
            for i in range(0,len(delete_columns)):
                try:
                    fl = fl.drop(delete_columns[i],axis=1)
                except:
                    continue
            
            fl.to_csv('merge.csv',mode='a',encoding='utf-8',index=False)
            
def to_ecel():
    df = pd.read_csv('merge.csv',encoding='utf-8')
    df.to_excel('merge.xlsx',index=False)

def delete_columns():
    df = pd.read_csv('merge.csv',encoding='utf-8')
    df = df.drop(['Unnamed: 0'],axis=1)
    df.to_csv('merge.csv',encoding='utf-8',index=False)

if __name__ == '__main__':
    get_files()
    to_ecel()