import argparse

"""" Argument parser module """


CommandParser = argparse.ArgumentParser(prog='TaskTracker', description='Task tracker is a project used to track and manage your tasks.')
CommandSubparsers = CommandParser.add_subparsers()

AddTaskParser = CommandSubparsers.add_parser('add')
AddTaskParser.set_defaults(cmd='add')

UpdateTaskParser = CommandSubparsers.add_parser('update')
UpdateTaskParser.set_defaults(cmd='update')

DeleteTaskParser = CommandSubparsers.add_parser('delete')
DeleteTaskParser.set_defaults(cmd='delete')

StatusInProgressParser = CommandSubparsers.add_parser('mark-in-progress')
StatusInProgressParser.set_defaults(cmd='mark-in-progress')

StatusDoneParser = CommandSubparsers.add_parser('mark-done')
StatusDoneParser.set_defaults(cmd='mark-done')

ListTaskParser = CommandSubparsers.add_parser('list')
ListTaskParser.set_defaults(cmd='list')

for parser in [ UpdateTaskParser, DeleteTaskParser, StatusInProgressParser, StatusDoneParser ]:
    parser.add_argument('id', type=int)

for parser in [ AddTaskParser, UpdateTaskParser ]:
    parser.add_argument('description', type=str)

ListTaskParser.add_argument('status', nargs='?',choices=['done', 'todo', 'in-progress'])


def StringParser():
    args = CommandParser.parse_args()
    return args
