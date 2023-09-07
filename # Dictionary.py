
# Dictionary.py
#
# @ author: A. N. Other
# date: September 2016
 
dictionary_1 = {"V344LDA":2000,
                "J245DWE":6350,
                "K265QWS":500}
 
# retrieving a value from the dictionary
print("The car with registration V344LDA is worth $", dictionary_1["V344LDA"])

# now for a more challenging example.....
 
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}