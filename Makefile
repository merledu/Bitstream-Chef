SHELL := /bin/bash

all:
	wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O conda_installer.sh
	export INSTALL_DIR=~/opt/f4pga
	export FPGA_FAM=xc7
	bash conda_installer.sh -u -b -p $(INSTALL_DIR)/$(FPGA_FAM)/conda;
	source "$(INSTALL_DIR)/$(FPGA_FAM)/conda/etc/profile.d/conda.sh";
	wget --no-check-certificate --directory-prefix=$(FPGA_FAM) --content-disposition https://raw.githubusercontent.com/SymbiFlow/symbiflow-examples/master/xc7/environment.yml
	wget --no-check-certificate --directory-prefix=$(FPGA_FAM) --content-disposition https://raw.githubusercontent.com/SymbiFlow/symbiflow-examples/master/xc7/requirements.txt
	conda env create -f $(FPGA_FAM)/environment.yml
	mkdir -p $INSTALL_DIR/xc7/install
	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-install-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-xc7a50t_test-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-xc7a100t_test-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-xc7a200t_test-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
	wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/20220404-212755/symbiflow-arch-defs-xc7z010_test-afbfe04.tar.xz | tar -xJC $(INSTALL_DIR)/xc7/install
