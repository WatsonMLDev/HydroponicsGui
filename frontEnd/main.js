const { app, BrowserWindow } = require("electron")
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
    createWindow()
})