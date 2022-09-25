import eel, tkinter, tkinter.filedialog as tkFileDialog, os, time, shutil
from eel import init, start
from fpga import *
from UTILS import utils


global source_files, FPGA
source_files = []
FPGA = None

shutil.rmtree("build", ignore_errors=True)
os.mkdir("build")

@eel.expose
def getSourceFile():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    ask_source_files = tkFileDialog.askopenfilenames()
    global source_files
    source_files += root.tk.splitlist(ask_source_files)
    source_files = list(set(source_files))
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
    modules = []
    for file in source_files:
        modules += utils.extract(file)
    eel.insertTopModules(modules)
    eel.showFPGAMapping()

@eel.expose
def selectTop(top, fpga):
    print(top, fpga)
    global FPGA
    FPGA = fpga
    if fpga == "arty-a7-35t":
        pins = utils.extractIOs(top)
        eel.mapInputs( pins[0] ,list(ARTY_COMPS_i.keys()))
        eel.mapOutputs(pins[1] ,list(ARTY_COMPS_o.keys()))

def check_status(match_case):
    while True:
        file = open("log.txt", "r")
        content = file.readlines()
        file.close()
        if match_case+"\n" in content:
            break
        else:
            time.sleep(5)
    return

@eel.expose
def generateBitstream(pinConfigs, clk_freq, fpga):
    if fpga == FPGA:
        utils.prepareContraints(pinConfigs, FPGA, clk_freq)
    else:
        utils.makeEmptyContraints(fpga)
        
    utils.bringSourceFiles(source_files)

    # synth
    eel.changeStatus("synth", "blue")
    check_status("Synthesis completed")
    eel.changeStatus("synth", "green")

    # pack
    eel.changeStatus("pack", "blue")
    check_status("Packaging completed")
    eel.changeStatus("pack", "green")

    # place
    eel.changeStatus("place", "blue")
    check_status("Placement completed")
    eel.changeStatus("place", "green")

    # route
    eel.changeStatus("route", "blue")
    check_status("Routing completed")
    eel.changeStatus("route", "green")

    #fasm
    eel.changeStatus("fasm", "blue")
    check_status("Fasm generation completed")
    eel.changeStatus("fasm", "green")

    # bitstream
    eel.changeStatus("bit", "blue")
    check_status("Bitstream generation completed")
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