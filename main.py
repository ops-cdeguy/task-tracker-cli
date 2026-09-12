import argparse
import json
from scripts import *


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Database parser
    parser_db = subparsers.add_parser("db", help="Database management commands")
    parser_db.add_argument("-i", "--initialize", action="store_true", help="Initialize the database")
    parser_db.add_argument("-rm", "--remove", action="store_true", help="Remove the database")
    parser_db.add_argument("-gen", "--sample", action="store_true", help="Get sample data for the database")
    
    # Pass function names WITHOUT parentheses ()
    parser_db.set_defaults(func=handle_db)

    # Task parser
    parser_task = subparsers.add_parser("task", help="Task management commands")
    parser_task.add_argument("-a", "--add", action="store_true", help="Add a new task")
    parser_task.set_defaults(func=handle_task)

    args = parser.parse_args()
    args.func(args)


def handle_db(args):
    if args.initialize:
        initialize()
    if args.remove:
        remove()
    if args.sample:
        generate_sample()


def handle_task(args):
    if args.add:
        # Load tasks only when a task command is actually executed
        with open("db.json", "r") as file:
            tasks = json.load(file)

        task_desc = input("Enter a task: ")
        updated_tasks = add_new(tasks, description=task_desc)

        with open("db.json", "w") as file:
            json.dump(updated_tasks, file, indent=4)


if __name__ == "__main__":
    main()