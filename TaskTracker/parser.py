import argparse

"""" Argument parser module """


CommandParser = argparse.ArgumentParser(prog='TaskTracker', description='Task tracker is a project used to track and manage your tasks.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
CommandParser.set_defaults(cmd='')
CommandSubparsers = CommandParser.add_subparsers()

AddTaskParser = CommandSubparsers.add_parser('add', help='Add a new task')
AddTaskParser.set_defaults(cmd='add')

UpdateTaskParser = CommandSubparsers.add_parser('update', help='Update an existing task')
UpdateTaskParser.set_defaults(cmd='update')

DeleteTaskParser = CommandSubparsers.add_parser('delete', help='Delete a task')
DeleteTaskParser.set_defaults(cmd='delete')

StatusInProgressParser = CommandSubparsers.add_parser('mark-in-progress', help='Mark a task as in progress')
StatusInProgressParser.set_defaults(cmd='mark-in-progress')

StatusDoneParser = CommandSubparsers.add_parser('mark-done', help='Mark a task as done')
StatusDoneParser.set_defaults(cmd='mark-done')

ListTaskParser = CommandSubparsers.add_parser('list', help='List tasks with optional status filter (done, todo, in-progress)')
ListTaskParser.set_defaults(cmd='list')

for parser in [ UpdateTaskParser, DeleteTaskParser, StatusInProgressParser, StatusDoneParser ]:
    parser.add_argument('-i','--id', type=int)

for parser in [ AddTaskParser, UpdateTaskParser ]:
    parser.add_argument('-d','--description', type=str)

ListTaskParser.add_argument('-s','--status', nargs='?',choices=['done', 'todo', 'in-progress'], help='Status filter')


def StringParser():
    args = CommandParser.parse_args()
    if (args.cmd == ''):
        CommandParser.print_help()
    return args
