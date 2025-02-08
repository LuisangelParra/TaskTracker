import json

"""" Json file reader and writer module """

def Reader():
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
        tasks = json.load(read_file)
    read_file.close
    return tasks

def Writer(tasks):
    with open("tasks.json", mode="w", encoding="utf-8") as write_file:
        json.dump(tasks, write_file)
    write_file.close
    