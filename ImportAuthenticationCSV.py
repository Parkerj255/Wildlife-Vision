import csv

def getAuthenticationFromFile(filename):
    # Open the CSV file
    with open(filename, 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)
        
        # Read the header row
        header = next(reader)
        
        # Read the first (and only) row of values
        values = next(reader)
        
        # Extract the values for the subscription_key and endpoint fields
        subscription_key = values[header.index('subscription_key')]
        endpoint = values[header.index('endpoint')]
    return [subscription_key,endpoint]