import eel
import json
import os
from tkinter import Tk, filedialog

eel.init("web")
CONFIG_FILE = "config.json"
DEFAULT_TASKS_PATH = "tasks.json"

# Load saved path if available
def load_saved_path():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as cfg:
                return json.load(cfg).get("task_path", DEFAULT_TASKS_PATH)
        except:
            pass
    return DEFAULT_TASKS_PATH

tasks = []
tasks_path = load_saved_path()

def choose_file():
    global tasks_path
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        tasks_path = file_path
        # Save this new path to config
        with open(CONFIG_FILE, "w") as cfg:
            json.dump({"task_path": tasks_path}, cfg)
        if not os.path.exists(tasks_path):
            with open(tasks_path, "w") as f:
                json.dump([], f)
    return tasks_path

@eel.expose
def get_tasks():
    global tasks
    if not os.path.exists(tasks_path):
        return []
    with open(tasks_path, "r") as f:
        tasks = json.load(f)
    return tasks

@eel.expose
def set_tasks(updated_tasks):
    global tasks
    tasks = updated_tasks
    with open(tasks_path, "w") as f:
        json.dump(tasks, f)

@eel.expose
def choose_task_file():
    return choose_file()

eel.start("index.html", size=(500, 600))
