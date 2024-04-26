import os

# Construct the path to 'all_data.csv' assuming it's in the same directory as 'solardashboard.py'
csv_file_path = os.path.join(os.path.dirname(__file__), 'all_data.csv')

# Now you can use 'csv_file_path' to access 'all_data.csv'
# For example, to read the CSV file:
with open(csv_file_path, 'r') as file:
    data = file.read()
    # Process the data
print(csv_file_path)