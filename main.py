import eel
import tkinter, tkinter.filedialog as tkFileDialog, os
from eel import init, start
from fpga import *


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
    eel.updateSourceFilesJS([(i,os.path.basename(i)) for i in source_files])

@eel.expose
def removeSourceFile(file):
    global source_files
    source_files.remove(file)
    eel.updateSourceFilesJS([(i,os.path.basename(i)) for i in source_files])

@eel.expose
def bringOutFPGAMapping():
    eel.insertTopModules(["test_top1", "test_top2"])
    eel.showFPGAMapping()

@eel.expose
def selectTop(top, fpga):
    print(top, fpga)
    # extract pins from top module..
    if fpga == "arty-a7-35t":
        eel.mapInputs(["test_in1", "test_in2"],list(ARTY_COMPS_i.keys()))
        eel.mapOutputs(["test_out1", "test_out2"],list(ARTY_COMPS_o.keys()))


if __name__ == '__main__':
    init('web')
    start('main.html', mode='custom', cmdline_args=['/Users/shahzaibkashif/Bitstream-Chef/node_modules/electron/dist/Electron.app/Contents/MacOS/Electron', '.'], port=8007)