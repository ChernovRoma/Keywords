from functions import *


FILE = "Fresh queries.csv"
filter = "time"

result = main(FILE, filter)
# result.to_excel(r'/Users/roman.chernov/Downloads/PS ICP groups/Business process.xlsx', index = False)

print(result)