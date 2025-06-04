let taskInput = document.getElementById('task-input');
let prioritySelect = document.getElementById('priority-select');
let taskList = document.getElementById('task-list');

async function loadTasks() {
  let tasks = await eel.get_tasks()();
  tasks.sort((a, b) => ({ high: 0, mid: 1, low: 2 }[a.priority] - { high: 0, mid: 1, low: 2 }[b.priority]));
  taskList.innerHTML = '';
  tasks.forEach((task, index) => {
    let li = document.createElement('li');
    li.className = task.priority;
    li.innerText = task.text;
    let deleteBtn = document.createElement('button');
    deleteBtn.innerText = '×';
    deleteBtn.className = 'delete-btn';
    deleteBtn.onclick = async () => {
      tasks.splice(index, 1);
      await eel.set_tasks(tasks)();
      loadTasks();
    };
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
  });
}

async function addTask() {
  let task = taskInput.value.trim();
  let priority = prioritySelect.value;
  if (task) {
    let tasks = await eel.get_tasks()();
    tasks.push({ text: task, priority });
    await eel.set_tasks(tasks)();
    taskInput.value = '';
    loadTasks();
  }
}

async function clearTasks() {
  await eel.set_tasks([])();
  loadTasks();
}

async function chooseFile() {
  await eel.choose_task_file()();
  loadTasks();
}

const modeToggle = document.getElementById('dark-mode-toggle');
let isDark = false;
modeToggle.onclick = () => {
  isDark = !isDark;
  document.body.classList.toggle('dark', isDark);
  modeToggle.textContent = isDark ? '☀️' : '🌙';
};

loadTasks();
