# Tests/test.py

import unittest

from TaskTracker.task import Task, CreateTask, UpdateTask, DeleteTask, SetStatus
from TaskTracker.filemanager import Reader

""" Test module """

class TestTaskTacker(unittest.TestCase):

    sampleTask = {
        'description': 'task test'
    }

    def test_a_id_assignation(self):
        tasks = Reader()
        currentId = list(tasks)[-1]

        newTask = Task(self.sampleTask['description'])
        self.assertEqual(newTask.id, int(currentId)+1, 'Id assignation is NOT correct')

    def test_b_task_add(self):
        newTask = Task(self.sampleTask['description'])
        CreateTask(newTask)

        tasks = Reader()
        self.assertEqual(tasks[str(newTask.id)]['description'], self.sampleTask['description'], 'Task has not been added')

    def test_c_task_update(self):
        updatedDescription = 'task test updated'

        tasks = Reader()
        currentId = list(tasks)[-1]

        UpdateTask(currentId, updatedDescription)

        tasks = Reader()
        self.assertEqual(tasks[currentId]['description'], updatedDescription, 'Task has not been updated')

    def test_d_task_set_status(self):
        tasks = Reader()
        currentId = list(tasks)[-1]

        SetStatus(currentId, 'in-progress')
        tasks = Reader()
        self.assertEqual(tasks[currentId]['status'], 'in-progress', 'Tasks status has not been updated')


    def test_e_task_delete(self):
        tasks = Reader()
        currentId = list(tasks)[-1]

        DeleteTask(currentId)
        tasks = Reader()

        self.assertEqual(tasks.get(currentId), None, 'Task has not been deleted.')

if __name__ == '__main__':
    unittest.main()
