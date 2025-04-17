import argparse
import pickle
import sys

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List")
    parser.add_argument('-v', '--view', help='View the active Tasks of the To-Do List', action='store_true')
    parser.add_argument('-a', '--add', help='Add a task into the To-Do List')
    parser.add_argument('-r', '--remove', help='Remove task from the To-Do List, Format: -r <Task NUMBER>')
    parser.add_argument('-rA', '--remove-all', help='Remove all tasks from the To-Do List', action='store_true')

    # Check if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    questAdd = [args.add]
    questRemove = [args.remove]

    if args.view:
        with open('quest_file.pkl', 'rb') as f:
            for i, task in enumerate(pickle.load(f), start=1):
                print(f"{i}. {task}")

    if args.add:
        try:
            with open('quest_file.pkl', 'rb') as f:
                questList = pickle.load(f)
        except (FileNotFoundError, EOFError):
            questList = []

        questList.append(args.add)

        with open('quest_file.pkl', 'wb') as f:
            pickle.dump(questList, f)

    if args.remove:
        try:
            with open('quest_file.pkl', 'rb') as f:
                questList = pickle.load(f)
        except (FileNotFoundError, EOFError):
            questList = []

        try:
            index = int(args.remove) - 1
            if 0 <= index < len(questList):
                removed = questList.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

        with open('quest_file.pkl', 'wb') as f:
            pickle.dump(questList, f)

    if args.remove_all:
        try:
            with open('quest_file.pkl', 'rb') as f:
                questList = pickle.load(f)
        except (FileNotFoundError, EOFError):
            questList = []

        questList.clear()  # Clear all tasks
        print("All tasks have been removed.")

        with open('quest_file.pkl', 'wb') as f:
            pickle.dump(questList, f)

if __name__ == "__main__":
    main()

