import pandas as pd

'''a = pd.read_csv('data.csv')
print(a.to_string())''' 

nam={
    'name':['sakshi','varsha','yogita'],
    'subject':['math','python','c++'], 
    'marks':[9,10,8]
    }
nams=pd.DataFrame(nam)
print(nams)
#loc(locate row)
#return 1 or more specified row
print('\n',nams.loc[1]) 
print('\n',nams.loc[[0,1]])

#checking the version of pandas
print(pd.__version__)

a=[1,2,3,4,5]
val=pd.Series(a)
print(val)
print(a[1]) or print(val[0])

val=pd.Series(a,index=['v','w','x','y','z'])
print(val)
print(val['y'])

day={'day1':'mon','day2':'tue','day3':'wed'}
days=pd.Series(day)
print(days)

days=pd.Series(day,index=['day3','day2'])
print(days)

