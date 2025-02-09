# TaskTracker

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Starting 🚀
### Instalation 🔧
These instructions will get you a copy of the project up and running on your local machine.

1. Clone the repository
2. Open the terminal and navigate to the project directory
3. Run the following command to install the TaskTracker-cli package and its dependencies: 
``` 
sudo pip3 install -e . 
```

Look at **Usage** to know how to use the client.


## Unit tests Running ⚙️

You need to finish the **Installation** step before running the tests.

To run the tests, run the following command in the terminal in the project directory:
```
python3 -m unittest
```


### Analyze the End-to-End Tests 🔩

These tests verify the correct behavior of the task management system by ensuring that key functionalities such as task creation, updating, status modification, and deletion work as expected.

For example:
```
def test_b_task_add(self):
    newTask = Task(self.sampleTask['description'])
    CreateTask(newTask)

    tasks = Reader()
    self.assertEqual(tasks[str(newTask.id)]['description'], self.sampleTask['description'], 'Task has not been added')
```
This test ensures that when a new task is created, it is correctly stored and retrievable from the system.

## Usage 📦
This aplication run from the command line, accept user actions and inputs as arguments, and perform the corresponding actions on the task list. The user can add, list, update, delete, mark a task as in progress, and mark a task as done.

To run any command, use the following format:
```
task-cli <command> <arguments>
```

### Commands 📋

- **add**: Add a new task to the task list.
    - **-d**: Description of the task.
- **list**: List all tasks in the task list.
    - **-s**: Filter tasks by status is optional (todo, in-progess, -done).
- **update**: Update a task in the task list.
    - **-i**: Task id.
    - **-d**: Description of the task.
- **delete**: Delete a task from the task list.
    - **-i**: Task id.
- **mark-in-progress**: Mark a task as in progress.
    - **-i**: Task id.
- **mark-done**: Mark a task as done.
    - **-i**: Task id.

## Autors ✒️

* **Luisangel Parra** - *Trabajo Inicial* - [Luisangelparra](https://github.com/Luisangelparra)

## License 📄

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details


---
⌨️ with ❤️ by [Luisangelparra](https://github.com/Luisangelparra) 😊