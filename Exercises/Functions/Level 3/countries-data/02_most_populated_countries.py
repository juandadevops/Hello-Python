# importing the module 
import json 
  
# reading the data from the file 
with open('countries-data.py', encoding="utf8") as f: 
    data = f.read() 
        
# reconstructing the data as a dictionary 
countries_data = json.loads(data) 

def most_populated_countries(countries_data, limit=10):
    
    # Sort the countries by population in descending order
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

    # Return the top 'limit' countries
    return sorted_countries[:limit]

# Get the 15 most populated countries
result = most_populated_countries(countries_data, 15)

# Print the result
for index, country in enumerate(result, start=1):
    print(f"{index}. {country['name']} - Population: {country['population']}")