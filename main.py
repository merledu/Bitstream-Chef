import eel,tkinter, tkinter.filedialog as tkFileDialog, os
from eel import init, start


global source_files
source_files = []

@eel.expose
def getSourceFile():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    ask_source_files = tkFileDialog.askopenfilenames()
    global source_files
    source_files += root.tk.splitlist(ask_source_files)
    # updateSourceFiles()
    print(source_files)
    eel.updateSourceFilesJS()

# def updateSourceFiles():
    # eel.updateSourceFilesJS(source_files)

if __name__ == '__main__':
    init('web')
    start('main.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron', '.'], port=8007)