# Explore json.load vs json.loads in practical
#URL:https://medium.com/p/f3ca223c7851

import json
import os
import pandas as pd

json_str = '{"a": 1, "b": 2}'

# loads the json string to Python
print(json.loads(json_str))

print("current directory", os.getcwd())
data = None
with open("data.json", "r") as f:
    data = json.load(f)

# Accessing data using While loop
counter = 0
df = None
while True:
    print("Name:", data[0]["name"])
    print("Age:", data[0]["age"])
    print("Is a student:", data[0]["is_student"])
    print("Courses:", data[0]["courses"])
    print("Address:", data[0]["address"]["city"])

    df = pd.DataFrame(data[0]['courses'], columns=["courses"])
    print("df", df)
    counter += 1

    if len(data) == counter:
        break

df2 = pd.DataFrame(data)
print(df2)
# Explore json.dump vs json.dumps
df2.to_csv("data_export.csv")


# accessing data using for loops
for row in data:
    print("Name:", row["name"])
    print("courses:", row["courses"])
    print("address:", row["address"])


# create a JSON file from the JSON data
with open("new_json_data.json", "w") as file:
    json.dump(data, file)


# convert Python objects into json string
json_new_str = json.dumps(data)

print("json_new_str", json_new_str)