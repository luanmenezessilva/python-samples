import requests
import json
import datetime
import os


list = []
timestamp_file = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')


# Read CEPs from CSV file
with open('./data/ceps_to_search.csv', 'r') as file:
    for line in file:
        cep = line.strip()
        if cep.isdigit() and len(cep) == 8:
            list.append(cep)


for cep in list:

    log_msg = ''
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    # Write a log file    
    with open(f'./data/logs/log-{timestamp_file}.txt', 'a', encoding='utf-8') as f:
        log_msg = cep + ';' + timestamp

    # Check if cep exists in log file
    try:
        search = True
        if os.path.exists(f'./data/ceps_searched/{cep}.json'):
            msg = f'{cep};CEP file already search!'
            print(f'{msg}')
            log_msg += f'{msg}'
            search = False
    except FileNotFoundError:
        pass

    if not search:
        continue

    # Make a GET request to an API endpoint
    response = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')

    # Check if the request was successful
    if response.status_code == 200:
        
        # Parse the JSON response
        data = response.json()
        
        # Write the JSON data to a file
        with open(f'./data/ceps_searched/{cep}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # Write a log file
        with open(f'./data/logs/log-{timestamp_file}.txt', 'a', encoding='utf-8') as f:
            f.write(f'{log_msg}\n')

        # Print the JSON data
        print(data)
    else:
        print(f"Request failed with status code:\n{response.status_code}\n{response.text}")
        with open('./data/logs/log-erro.txt', 'a', encoding='utf-8') as f:
            f.write(f'{cep};{response.status_code};{response.text}\n')
