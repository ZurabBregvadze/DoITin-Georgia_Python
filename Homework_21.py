########################################
#Homework_21 Task_1
########################################
import json
import threading
import os

# Step 1: Create JSON files
def create_json_files():
    data = [
        {"name": "Zurab", "age": 51, "city": "Tbilisi"},
        {"name": "Alexander", "age": 9, "city": "Tbilisi"},
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "San Francisco"},
        {"name": "Charlie", "age": 35, "city": "Los Angeles"},
        {"name": "David", "age": 51, "city": "Tbilisi"},
    ]
    os.makedirs("json_files", exist_ok=True)
    for i, entry in enumerate(data, start=1):
        filename = f"json_files/file_{i}.json"
        with open(filename, "w") as f:
            json.dump(entry, f, indent=4)
    print("JSON files created!")

# Step 2: Define a parser function
def parse_json_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    print(f"Data from {filename}:\n{json.dumps(data, indent=4)}\n")

# Step 3: Multithreading function
def process_files_with_threads():
    files = [f"json_files/{file}" for file in os.listdir("json_files") if file.endswith(".json")]
    threads = []
    for file in files:
        thread = threading.Thread(target=parse_json_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Main execution
if __name__ == "__main__":
    create_json_files()
    process_files_with_threads()


########################################

########################################
#Homework_21 Task_2
########################################


##############################################

