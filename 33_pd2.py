import pandas as pd

#csv
'''df=pd.read_csv('MOCK_DATA.csv')
# print(df.to_string()) # show all data

# print(df) # return the first 5 rows, and the last 5 rows

# print(pd.options.display.max_rows) # more than 60

pd.options.display.max_rows=100
print(df)'''

#json
'''df = pd.read_json('MOCK_DATA.json')
print(df.to_string())'''

'''data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df) '''

#analyzing dataframes
df = pd.read_json('MOCK_DATA.json')

# print(df.head(10))

# print(df.head()) #return top 5rows

# print(df.tail()) #return last 5rows

print(df.info())