const { app, BrowserWindow } = require('electron');

const createMainWindow = () => {

  const win = new BrowserWindow({ webPreferences: {
            nodeIntegration: true
    }, icon: __dirname + '/web/img/logo.png' });

    win.maximize();
    
    win.show();

    win.loadURL('http://localhost:8007/main.html');
  }


app.whenReady().then(() => {
    createMainWindow()
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
});

process.env['ELECTRON_DISABLE_SECURITY_WARNINGS'] = 'true';