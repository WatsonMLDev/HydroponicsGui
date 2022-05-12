
/*
imports required librarys Electron (for turing web code into an app), PythonShell ( to run backend code), and
electron-reload (to reload the app when code changes)
 */
const { app, BrowserWindow } = require("electron")
const {PythonShell} = require("python-shell");
require("electron-reload")(__dirname)


// creats a new window when called
function createWindow(){
    const mainWindow = new BrowserWindow({
        width:900,
        height:600
    })

    mainWindow.loadFile('view/index.html') // loads the file index.html into view
    mainWindow.webContents.openDevTools() // just opens dev tools, comment out to hide
}
/*
when the app is ready, create a new window and run the backend code
 */
app.whenReady().then(() => {
    try {
        PythonShell.run('./backEnd/app.py',null, function (err, result){
            if (err) throw err;
            console.log('result: ', result.toString());
            res.send(result.toString())
        });
    }
    catch (err) {
        console.log(err)
    }

    createWindow() // creates the new window
})