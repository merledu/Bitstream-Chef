# Updated F4PGA install script
sudo apt update -y
sudo apt install -y git wget xz-utils
git clone https://github.com/chipsalliance/f4pga-examples
cd f4pga-examples
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O conda_installer.sh
export F4PGA_INSTALL_DIR=~/opt/f4pga
export FPGA_FAM=xc7
bash conda_installer.sh -u -b -p $F4PGA_INSTALL_DIR/$FPGA_FAM/conda;
source "$F4PGA_INSTALL_DIR/$FPGA_FAM/conda/etc/profile.d/conda.sh";
conda env create -f $FPGA_FAM/environment.yml
export F4PGA_PACKAGES='install-xc7 xc7a50t_test xc7a100t_test xc7a200t_test xc7z010_test'
mkdir -p $F4PGA_INSTALL_DIR/$FPGA_FAM

F4PGA_TIMESTAMP='20220907-210059'
F4PGA_HASH='66a976d'

for PKG in $F4PGA_PACKAGES; do
  wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/${F4PGA_TIMESTAMP}/symbiflow-arch-defs-${PKG}-${F4PGA_HASH}.tar.xz | tar -xJC $F4PGA_INSTALL_DIR/${FPGA_FAM}
done

# SHELL := /bin/bash

# all:
# 	wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O conda_installer.sh
# 	export INSTALL_DIR=~/opt/f4pga
# 	export FPGA_FAM=xc7
# 	bash conda_installer.sh -u -b -p $(INSTALL_DIR)/$(FPGA_FAM)/conda;
# 	source "$(INSTALL_DIR)/$(FPGA_FAM)/conda/etc/profile.d/conda.sh";
# 	wget --no-check-certificate --directory-prefix=$(FPGA_FAM) --content-disposition https://raw.githubusercontent.com/SymbiFlow/symbiflow-examples/master/xc7/environment.yml
# 	wget --no-check-certificate --directory-prefix=$(FPGA_FAM) --content-disposition https://raw.githubusercontent.com/SymbiFlow/symbiflow-examples/master/xc7/requirements.txt
# 	conda env create -f $(FPGA_FAM)/environment.yml
# 	mkdir -p $INSTALL_DIR/xc7/install
# 	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-install-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
# 	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-xc7a50t_test-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
# 	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-xc7a100t_test-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
# 	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-xc7a200t_test-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
# 	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-xc7z010_test-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install


# Updated F4PGA install script
# apt update -y
# apt install -y git wget xz-utils
# git clone https://github.com/chipsalliance/f4pga-examples
# cd f4pga-examples
# wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O conda_installer.sh
# export F4PGA_INSTALL_DIR=~/opt/f4pga
# export FPGA_FAM=xc7
# bash conda_installer.sh -u -b -p $F4PGA_INSTALL_DIR/$FPGA_FAM/conda;
# source "$F4PGA_INSTALL_DIR/$FPGA_FAM/conda/etc/profile.d/conda.sh";
# conda env create -f $FPGA_FAM/environment.yml
# export F4PGA_PACKAGES='install-xc7 xc7a50t_test xc7a100t_test xc7a200t_test xc7z010_test'
# mkdir -p $F4PGA_INSTALL_DIR/$FPGA_FAM

# F4PGA_TIMESTAMP='20220907-210059'
# F4PGA_HASH='66a976d'

# for PKG in $F4PGA_PACKAGES; do
#   wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/${F4PGA_TIMESTAMP}/symbiflow-arch-defs-${PKG}-${F4PGA_HASH}.tar.xz | tar -xJC $F4PGA_INSTALL_DIR/${FPGA_FAM}
# done
