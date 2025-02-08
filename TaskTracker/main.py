#!/usr/bin/python3

from parser import StringParser
from task import Task, UpdateTask, DeleteTask, SetStatus, ListTasks

""" Main module Task Tracker """

def main():
    args = StringParser()
    if (args.cmd == 'add'):
        NewTask = Task(args.description)
        print(f'Adding task {args.description}.')
    elif(args.cmd == 'update'):
        UpdateTask(args.id, args.description)
        print(f'Modifiying task {args.id} description to {args.description}.')
    elif(args.cmd == 'delete'):
        DeleteTask(args.id)
        print(f'Deleting task {args.id}.')
    elif(args.cmd == 'mark-in-progress'):
        SetStatus(args.id, status='in-progress')
        print(f'Mark task {args.id} in progress.')
    elif(args.cmd == 'mark-done'):
        SetStatus(args.id, status='done')
        print(f'Task {args.id} is done.')
    elif(args.cmd == 'list'):
        if (args.status != None):
            print(f'Listing tasks with status {args.status}')
        else:
            print(f'Listing all tasks')
        ListTasks(args.status)

if __name__ == "__main__":
    main()
