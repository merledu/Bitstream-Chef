                                                                             
```
 /$$$$$$$  /$$$$$$ /$$$$$$$$ /$$$$$$  /$$$$$$$$ /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$      /$$
| $$__  $$|_  $$_/|__  $$__//$$__  $$|__  $$__/| $$__  $$| $$_____/ /$$__  $$| $$$    /$$$
| $$  \ $$  | $$     | $$  | $$  \__/   | $$   | $$  \ $$| $$      | $$  \ $$| $$$$  /$$$$
| $$$$$$$   | $$     | $$  |  $$$$$$    | $$   | $$$$$$$/| $$$$$   | $$$$$$$$| $$ $$/$$ $$
| $$__  $$  | $$     | $$   \____  $$   | $$   | $$__  $$| $$__/   | $$__  $$| $$  $$$| $$
| $$  \ $$  | $$     | $$   /$$  \ $$   | $$   | $$  \ $$| $$      | $$  | $$| $$\  $ | $$
| $$$$$$$/ /$$$$$$   | $$  |  $$$$$$/   | $$   | $$  | $$| $$$$$$$$| $$  | $$| $$ \/  | $$
|_______/ |______/   |__/   \______/    |__/   |__/  |__/|________/|__/  |__/|__/     |__/
                                                                                          
                                                                                          
                                                                                          
  /$$$$$$        /$$   /$$       /$$$$$$$$       /$$$$$$$$                                
 /$$__  $$      | $$  | $$      | $$_____/      | $$_____/                                
| $$  \__/      | $$  | $$      | $$            | $$                                      
| $$            | $$$$$$$$      | $$$$$         | $$$$$                                   
| $$            | $$__  $$      | $$__/         | $$__/                                   
| $$    $$      | $$  | $$      | $$            | $$                                      
|  $$$$$$/      | $$  | $$      | $$$$$$$$      | $$                                      
 \______/       |__/  |__/      |________/      |__/                                      
                                                                                          
```
## Features
- 

## Dependencies
Node JS
```bash
apt install nodejs npm
```
Python EEL
```
pip install eel
```
sudo apt-get install python3-tk
```
F4PGA - Automated Bitstream Generation Tool

https://f4pga-examples.readthedocs.io/en/latest/getting.html 
## How to Run

### For First Time
```bash
git clone https://github.com/shahzaibk23/Bitsream-Chef.git
cd Bitsream-Chef
npm install
```

### For running the application
```bash
source ./environment.sh --activate
python main.py
```


--------------------------------

For activating environment.
```bash
source ./environment.sh --activate
```
For deactivating environment.
```bash
source ./environment.sh --deactivate
```

--------------------------------

For generating bitstream.
```bash
TARGET="arty_35" TOP_MODULE="SoCNow" VERILOG_DIR="../../verilog_dir" CONS_DIR="../../constraints_dir" CONSTRAINT_FILE="anyfile" make 
```

### Documentation:
https://docs.google.com/document/d/1xByuFOh_SIC23NHe2ZOPA65XLJydzgEiLvRrkp8hrhM/edit?usp=sharing 
