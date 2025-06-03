const { app, BrowserWindow, ipcMain, Menu } = require('electron');
const fs = require('fs');
const path = require('path');

let tasksPath = path.join(app.getPath('userData'), 'tasks.json');
if (!fs.existsSync(tasksPath)) fs.writeFileSync(tasksPath, '[]');

function createWindow() {
  const win = new BrowserWindow({
    width: 500,            // Set initial width
    height: 600,           // Set initial height
    minWidth: 500,
    minHeight: 600,
    icon: path.join(__dirname, 'def.ico'),
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });
  win.loadFile('index.html');

  Menu.setApplicationMenu(null);
}

ipcMain.handle('get-tasks', () => {
  return JSON.parse(fs.readFileSync(tasksPath));
});

ipcMain.handle('set-tasks', (e, tasks) => {
  fs.writeFileSync(tasksPath, JSON.stringify(tasks));
});

app.whenReady().then(createWindow);
console.log('Tasks stored at:', tasksPath); // C:\Users\<USER>\AppData\Roaming\todo-electron\tasks.json