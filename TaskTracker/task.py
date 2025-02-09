# /TaskTracker/task.py
from datetime import datetime
from TaskTracker.filemanager import Reader, Writer

""" Class task module """


class Task:
    def __init__(self, description):
        self.id = self.__SetID()
        self.description = description
        self.status = 'todo'
        self.createdAt = datetime.now().strftime("Created on %B %d, %Y at %I:%M %p")
        self.updatedAt = None

    def __SetID(self):
        tasks = Reader()
        if (len(list(tasks)) == 0):
            return 1
        id = list(tasks)[-1]
        return int(id)+1


def CreateTask(task):
    tasks = Reader()
    tasks[task.id] = {
        'description': task.description,
        'status': task.status,
        'createdAt': task.createdAt,
        'updatedAt': task.updatedAt
    }
    Writer(tasks)
    __PrintTasks(tasks)


def UpdateTask(id, description):
    tasks = Reader()
    tasks[str(id)] = {
        'description': description,
        'status': tasks[str(id)]['status'],
        'createdAt': tasks[str(id)]['createdAt'],
        'updatedAt': __UpdateDate()
    }
    Writer(tasks)


def DeleteTask(id):
    tasks = Reader()
    tasks.pop(str(id))
    Writer(tasks)


def SetStatus(id, status):
    tasks = Reader()
    tasks[str(id)] = {
        'description': tasks[str(id)]['description'],
        'status': status,
        'createdAt': tasks[str(id)]['createdAt'],
        'updatedAt': __UpdateDate()
    }
    Writer(tasks)


def ListTasks(status):
    tasks = Reader()
    if (status == None):
        return __PrintTasks(tasks)
    tasksWithStatus = {}
    for id in tasks:
        if (tasks[id]['status'] == status):
            tasksWithStatus[id] = tasks[id]
    __PrintTasks(tasksWithStatus)


def __UpdateDate():
    updatedAt = datetime.now().strftime("Last update on %B %d, %Y at %I:%M %p")
    return updatedAt


def __PrintTasks(tasksDict):
    print('Task Tracker - List')
    for id in tasksDict:
        print('')
        print(f'Task ID: {id} Description: {tasksDict[id]['description']}')
        print(f'Status: {tasksDict[id]['status']}')
        print(f'Creation Date: {tasksDict[id]['createdAt']}')
        print(f'Udated: {tasksDict[id]['updatedAt']}')
        print('')
