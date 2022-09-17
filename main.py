import eel, tkinter, tkinter.filedialog as tkFileDialog, os, time
from eel import init, start
from fpga import *
from utils import *


global source_files, FPGA
source_files = []
FPGA = None

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
    global FPGA
    FPGA = fpga
    # extract pins from top module..
    if fpga == "arty-a7-35t":
        eel.mapInputs(["test_in1", "test_in2"],list(ARTY_COMPS_i.keys()))
        eel.mapOutputs(["test_out1", "test_out2"],list(ARTY_COMPS_o.keys()))

@eel.expose
def generateBitstream(pinConfigs):
    prepareContraints(pinConfigs, FPGA)

    # synth
    eel.changeStatus("synth", "blue")
    time.sleep(5)
    eel.changeStatus("synth", "green")

    # pack
    eel.changeStatus("pack", "blue")
    time.sleep(5)
    eel.changeStatus("pack", "green")

    # place
    eel.changeStatus("place", "blue")
    time.sleep(5)
    eel.changeStatus("place", "green")

    # route
    eel.changeStatus("route", "blue")
    time.sleep(5)
    eel.changeStatus("route", "green")

    #fasm
    eel.changeStatus("fasm", "blue")
    time.sleep(5)
    eel.changeStatus("fasm", "green")

    # bitstream
    eel.changeStatus("bit", "blue")
    time.sleep(5)
    eel.changeStatus("bit", "green")

    eel.showBitFile()

@eel.expose
def exportBitstream():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    export_src = tkFileDialog.askdirectory()
    print(export_src)
   



if __name__ == '__main__':
    init('web')
    start('main.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron', '.'], port=8007)