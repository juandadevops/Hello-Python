# importing the module 
import json 
  
# reading the data from the file with encoding correctly
with open('Exercises/Functions/Level 3/countries-data/countries-data.py', encoding="utf8") as f: 
    data = f.read() 
        
# reconstructing the data as a dictionary 
countries_data = json.loads(data) 

def most_spoken_languages(countries_data, limit=10):
    """ Function that return 10 or 20 most spoken languages in the world in descending order

    Args:
        countries_data (dict): All countries data to check the languages
        limit (int, optional): Number of languages to be displayed. Defaults to 10.

    Returns:
        _type_: The most spoken languages are returned according to the established limit.
    """
    # Extract all languages from the countries data
    all_languages = [language for country in countries_data for language in country['languages']]

    # Count occurrences of each language
    language_counts = {}
    for language in all_languages:
        language_counts[language] = language_counts.get(language, 0) + 1

    # Sort languages by count in descending order
    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top N languages
    return [language[0] for language in sorted_languages[:limit]]
    
    
# Get the top 15 most spoken languages
top_languages = most_spoken_languages(countries_data, 15)

# Print the result
print("Top 15 most spoken languages:", top_languages)