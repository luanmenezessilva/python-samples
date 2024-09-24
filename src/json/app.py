import json
from prettytable import PrettyTable

# Read the JSON file
filename = './src/json/data.json'
with open(filename, "r", encoding="utf-8") as file:
    data = json.load(file)


# Create a table
table = PrettyTable()
table.field_names = ['index', 'id', 'subject', 'serviceFirstLevel', 'status']

# Add data to the table
for index, item in enumerate(data):
    # Caracteres para remover do subject
    subject = item['subject'].replace('\n', '')
    # Fwd: 
    subject = subject.replace('FWD: ', '', 1)
    subject = subject.replace('Fwd: ', '', 1)
    subject = subject.replace('fwd: ', '', 1)
    # ENC: 
    subject = subject.replace('ENC: ', '', 1)
    subject = subject.replace('Enc: ', '', 1)
    subject = subject.replace('enc: ', '', 1)
    # Re: 
    subject = subject.replace('RE: ', '', 1)
    subject = subject.replace('Re: ', '', 1)
    subject = subject.replace('re: ', '', 1)
    
    table.add_row([index+1, item['id'], subject, item['serviceFirstLevel'], item['status']])

# Print the table
print(table)
# Save the table to a file
with open('./src/json/table.txt', 'w', encoding="utf-8") as file:
    file.write(str(table))

