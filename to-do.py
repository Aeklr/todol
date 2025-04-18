#!/usr/bin/env python3
import argparse
import pickle
import sys
import os
from termcolor import colored # Imported colored for colored output

data_path = os.path.expanduser("~/.local/share/todol")
os.makedirs(data_path, exist_ok=True)
pkl_path = os.path.join(data_path, "quest_file.pkl")

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List")
    parser.add_argument('-v', '--view', help='View the active Tasks of the To-Do List', action='store_true')
    parser.add_argument('-a', '--add', help='Add a task into the To-Do List')
    parser.add_argument('-r', '--remove', help='Remove task from the To-Do List, Format: -r <Task NUMBER>')
    parser.add_argument('-rA', '--remove-all', help='Removes all tasks from the To-Do List', action='store_true')

    # Defined colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    # Check if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    questAdd = [args.add]
    questRemove = [args.remove]

    # -v argument
    if args.view:
        try:
            with open(pkl_path, 'rb') as f:
                questList = pickle.load(f)
        except (FileNotFoundError, EOFError):
            questList = []

    # Get max length of lines like "1. Task"
        max_length = max((len(f"{i+1}. {task}") for i, task in enumerate(questList)), default=0)
        border = '─' * (max_length + 4)  # +4 padding
        
        # Printing upper border
        print(f"{YELLOW}{border}{RESET}")
        # Printing tasks in the list
        for i, task in enumerate(questList, start=1):
            print(f"{i}. {GREEN}{task}{RESET}")
        # Printing lower border after the tasks are listed
        print(f"{YELLOW}{border}{RESET}")

    # -a argument
    if args.add:
        try:
            with open(pkl_path, 'rb') as f:
                questList = pickle.load(f)
        except (FileNotFoundError, EOFError):
            questList = []

        questList.append(args.add)

        with open(pkl_path, 'wb') as f:
            pickle.dump(questList, f)
            print(f"Added: {BLUE}{args.add}{RESET} To the list.")

    # -r argument
    if args.remove:
        try:
            with open(pkl_path, 'rb') as f:
                questList = pickle.load(f)
        except (FileNotFoundError, EOFError):
            questList = []

        try:
            index = int(args.remove) - 1
            if 0 <= index < len(questList):
                removed = questList.pop(index)
                print(f"Removed: {RED}{removed}{RESET}.")
            else:
                print("Invalid task number.")
        except ValueError: # Invalid task number handeling
            print("Please enter a valid task number.")
        with open(pkl_path, 'wb') as f:
            pickle.dump(questList, f)

    # -rA argument
    if args.remove_all:
        try:
            with open(pkl_path, 'rb') as f:
                questList = pickle.load(f)
        except (FileNotFoundError, EOFError):
            questList = []

        questList.clear()  # Clear all tasks
        print(f"{RED}All tasks have been removed.{RESET}")

        with open(pkl_path, 'wb') as f:
            pickle.dump(questList, f)

if __name__ == "__main__":
    main()

