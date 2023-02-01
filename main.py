from functions import *


FILE = "Fresh queries.csv"
filter = "team manag"

result = main(FILE, filter)
result.to_excel(r'/Users/roman.chernov/Downloads/PS ICP groups/Team management.xlsx', index = False)

print(result)