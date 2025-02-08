import json
import os

"""" Json file reader and writer module """

path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

def Reader(filename = f'{path}/tasks.json'):
    with open(filename, mode="r", encoding="utf-8") as read_file:
        tasks = json.load(read_file)
    read_file.close
    return tasks

def Writer(tasks):
    with open(f'{path}/tasks.json', mode="w", encoding="utf-8") as write_file:
        json.dump(tasks, write_file)
    write_file.close
    