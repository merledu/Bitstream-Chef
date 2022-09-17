from fpga import *
import os

def prepareContraints(pinConfigs, fpga):
    COMPONENTS = None
    FPGA = None
    if fpga == "arty-a7-35t":
        COMPONENTS = {**ARTY_COMPS_i, **ARTY_COMPS_o}
        FPGA = "arty"
    
    xdc_str = XDC_ENCODS["default"] + "\n"

    for pin in pinConfigs:
        xdc_str += COMPONENTS[pin["comp"]].replace("x", pin["pin"]) + "\n"

    if not os.path.exists("build"):
        os.makedirs("build")
    file=open(f"build/{FPGA}.xdc", "w+")
    file.write(xdc_str)
    file.close()