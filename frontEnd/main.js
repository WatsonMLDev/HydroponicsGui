
/*
imports required librarys Electron (for turing web code into an app), PythonShell ( to run backend code), and
electron-reload (to reload the app when code changes)
 */
const { app, BrowserWindow } = require("electron")
const {PythonShell} = require("python-shell");
const fetch = require('node-fetch');
require("electron-reload")(__dirname)



// creats a new window when called
function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 900,
        height: 600
    })

    mainWindow.loadFile('view/index.html') // loads the file index.html into view
    mainWindow.webContents.openDevTools() // just opens dev tools, comment out to hide

    mainWindow.on('close', function () { //   <---- Catch close event
        fetch('http://localhost:5000/stop', // <---- Send close event to backend
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(res => res.json())
            .then(data => {
                console.log(data)
                return
            }).catch(err => {
            console.log(err)
        })
    })
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