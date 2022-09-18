from fpga import *
import os
import re

class UTILS:
    def __init__(self):
        pass

    def extract(self, path):
        file = open(path, 'r')
        return self.use_regex(file.read())

    def use_regex(self, input_text):
        pattern = re.compile(r"module+[\s\n\t]+[a-z_A-Z0-9]+\(", re.IGNORECASE)
        return pattern.findall(input_text)

    def prepareContraints(self, pinConfigs, fpga):
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

utils = UTILS()
# b=a.extract("verilogDirectory/Picofoxy.v")
# print(len(b))
# print(b)