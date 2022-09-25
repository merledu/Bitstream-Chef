from fpga import *
import os
import re

class UTILS:
    def __init__(self):
        pass

    def extract(self, path):
        file = open(path, 'r')
        data = self.use_regex(file.read())
        file.close()
        return [dat.split(" ")[1][0:-1] for dat in data]

    def use_regex(self, input_text):
        pattern = re.compile(r"module+[\s\n\t]+[a-z_A-Z0-9]+\(", re.IGNORECASE)
        return pattern.findall(input_text)

    def prepareContraints(self, pinConfigs, fpga, clk_freq):
        COMPONENTS = None
        FPGA = None
        print(fpga)
        if fpga == "arty-a7-35t":
            COMPONENTS = {**ARTY_COMPS_i, **ARTY_COMPS_o}
            FPGA = "arty"
        
        xdc_str = XDC_ENCODS["default"] + "\n"
        xdc_str += XDC_ENCODS["clk"].replace("x", str(clk_freq)) + "\n"
        for pin in pinConfigs:
            xdc_str += COMPONENTS[pin["comp"]].replace("x", pin["pin"]) + "\n"

        if not os.path.exists("build"):
            os.makedirs("build")
        file=open(f"build/{FPGA}.xdc", "w+")
        file.write(xdc_str)
        file.close()

    def makeEmptyContraints(self,fpga):
        while os.path.exists("build/*.xdc"):
            os.remove("build/*.xdc")
        if fpga == "arty-a7-35t":
            FPGA = "arty"
        file=open(f"build/{FPGA}.xdc", "w+")
        file.write("")
        file.close()
            
    
    def bringSourceFiles(self, source_files):
        for file in source_files:
            os.system(f"cp {file} build/")

    def moduleContent(self,module):
        pass

    def extractIOs(self, top):
        # return (["test_in1", "test_in2"], ["test_out1", "test_out2"])
        file= open(f"{GENERATOR_DIR}/{RTL_FILES['fpga']}", "r")
        content = file.readlines()
        file.close()
        n = 0
        Inputs = []
        Outputs = []
        for i in content:
            if n == 1 :
                if ")" in i:
                    n = 0
                else:
                    if "input" in i:
                        newi = i.replace(",", "").split()[-1]
                        file = open(f"{GENERATOR_DIR}/src/main/scala/config.json", "r")
                        outData = json.load(file)
                        file.close()
                        ic(outData)
                        if "reset" in newi:
                            Inputs.append(newi)
                        elif outData["gpio"] == 1 and "gpio" in newi:
                            Inputs.append(newi)
                        elif outData["spi"] == 1 and "spi" in newi:
                            Inputs.append(newi)
                        elif outData["uart"] == 1 and "uart" in newi:
                            Inputs.append(newi)
                        elif outData["timer"] == 1 and "timer" in newi:
                            Inputs.append(newi)
                        elif outData["spi_flash"] == 1 and "spi_flash" in newi:
                            Inputs.append(newi)
                        elif outData["i2c"] == 1 and "i2c" in newi:
                            Inputs.append(newi)
                    elif "output" in i or "inout" in i:
                        newi = i.replace(",", "").split()[-1]
                        file = open(f"{GENERATOR_DIR}/src/main/scala/config.json", "r")
                        outData = json.load(file)
                        file.close()
                        ic(outData)
                        if outData["gpio"] == 1 and "gpio" in newi:
                            Outputs.append(newi)
                        elif outData["spi"] == 1 and "spi" in newi:
                            Outputs.append(newi)
                        elif outData["uart"] == 1 and "uart" in newi:
                            Outputs.append(newi)
                        elif outData["timer"] == 1 and "timer" in newi:
                            Outputs.append(newi)
                        elif outData["spi_flash"] == 1 and "spi_flash" in newi:
                            Outputs.append(newi)
                        elif outData["i2c"] == 1 and "i2c" in newi:
                            Outputs.append(newi)
                    
                    print("newi", newi)
            elif "module SoCNow(" in i:
                print("MATHCED", i)
                n = 1

utils = UTILS()
