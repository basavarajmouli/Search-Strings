from urllib import request
import json

# API for census data
url_str = 'http://api.census.gov/data/2000/surname?get=NAME,COUNT&RANK=1:100000'

# reading the response
response = request.urlopen(url_str)

# convert the response into string
html_str = response.read().decode("utf-8")
# convert the string into json 
json_data = json.loads(html_str)

# Enter the string that ned to be searched
search_string = input("Please Enter the string to be searched: ")

# iterating over the each element to find the substring 
for i in range(len(json_data)):
    if json_data[i][0].endswith(search_string.upper()):
        print(json_data[i][0])
