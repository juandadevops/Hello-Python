# importing the module 
import json 
  
# reading the data from the file 
with open('Exercises/Functions/Level 3/countries-data/countries-data.py', encoding="utf8") as f: 
    data = f.read() 
        
# reconstructing the data as a dictionary 
countries_data = json.loads(data) 

def most_populated_countries(countries_data, limit=10):
    """ Function that return 10 or 20 most populated countries in descending order.

    Args:
        countries_data (dict): All countries data to check the most populated countries
        limit (int, optional): Number of languages to be displayed. Defaults to 10.

    Returns:
        _type_: The most populated countries are returned according to the established limit.
    """
    
    # Sort the countries by population in descending order
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

    # Return the top 'limit' countries
    return sorted_countries[:limit]

# Get the 15 most populated countries
result = most_populated_countries(countries_data, 15)

# Print the result
for index, country in enumerate(result, start=1):
    print(f"{index}. {country['name']} - Population: {country['population']}")