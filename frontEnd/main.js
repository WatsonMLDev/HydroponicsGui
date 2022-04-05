const { app, BrowserWindow } = require("electron")
const {PythonShell} = require("python-shell");
require("electron-reload")(__dirname)

function createWindow(){
    const mainWindow = new BrowserWindow({
        width:900,
        height:600
    })

    mainWindow.loadFile('view/index.html')
    mainWindow.webContents.openDevTools()
}

app.whenReady().then(() => {
    const {PythonShell} =require('python-shell');
    PythonShell.run('./backEnd/app.py',null, function (err, result){
        if (err) throw err;
        console.log('result: ', result.toString());
        res.send(result.toString())
    });

    createWindow()
})