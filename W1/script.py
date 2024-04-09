import os
import csv
import json

def read_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error occurred while reading CSV file: {e}")
        return None

def write_csv(data, file_path):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV file '{file_path}' written successfully.")
    except Exception as e:
        print(f"Error occurred while writing CSV file: {e}")

def read_json(file_path):
    try:
        with open(file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error occurred while reading JSON file: {e}")
        return None

def write_json(data, file_path):
    try:
        with open(file_path, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f"JSON file '{file_path}' written successfully.")
    except Exception as e:
        print(f"Error occurred while writing JSON file: {e}")


input_csv_path = '/home/bitcot/Desktop/Bitcot_Task/Week1/Day4/revenue.csv'
output_json_path = '/home/bitcot/Desktop/Bitcot_Task/Week1/Day4/output_revenue.json'

input_json_path = '/home/bitcot/Desktop/Bitcot_Task/Week1/Day4/company.json'
output_csv_path = '/home/bitcot/Desktop/Bitcot_Task/Week1/Day4/output_company.csv'

# Check if output directories exist, if not, create them
output_json_dir = os.path.dirname(output_json_path)
output_csv_dir = os.path.dirname(output_csv_path)
os.makedirs(output_json_dir, exist_ok=True)
os.makedirs(output_csv_dir, exist_ok=True)

csv_data = read_csv(input_csv_path)
if csv_data:
    write_json(csv_data, output_json_path)

json_data = read_json(input_json_path)
if json_data:
    try:
        if isinstance(json_data, list):
            data_to_write = json_data
        else:
            data_to_write = [json_data]
        write_csv(data_to_write, output_csv_path)
    except Exception as e:
        print(f"Error converting JSON data to CSV format: {e}")

  
