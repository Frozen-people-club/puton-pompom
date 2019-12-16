
const path = require('path')
const utl = require('url')
const isDev = require('electron-is-dev')
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
    window.loadURL(isDev ? 'http:localhost:3000' : path.join('file://', __dirname, '../public/index.html'))

    window.on('closed', () => {
        window = null
    })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    if (window === null) {
        createWindow()
    }
})