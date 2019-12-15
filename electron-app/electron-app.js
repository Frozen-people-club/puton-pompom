
const path = require('path')
const {app, BrowserWindow} = require('electron')

let window = null

function createWindow() {
    const windowOptionsn = {
        width: 1080,
        minWidth: 680,
        height: 840,
        title: "Avocether",
        webPreferences: {
            nodeIntegration: true
        }
    }

    window = new BrowserWindow(windowOptionsn)
    window.loadURL(path.join('file://', __dirname, '/index.html'))

    window.on('closed', () => {
        window = null
    })
}

app.on('ready', createWindow)