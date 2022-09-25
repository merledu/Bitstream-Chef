# define directory paths
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(patsubst %/,%,$(dir $(mkfile_path)))

# top module of RTL
TOP:=$(TOP_MODULE)

# verilog source files for bitstream generation
VERILOG := $(wildcard $(VERILOG_DIR)/*.v)

# XDC file for bitstream generation
# xdcfile := $(current_dir)/extra/Picofoxy.xdc

# part number of FPGA
DEVICE  := xc7a50t_test

# bitstream FPGA name
BITSTREAM_DEVICE := artix7

# directory where generated bitstream will be placed
BUILDDIR:=build

ifeq ($(TARGET),arty_35)
	PARTNAME := xc7a35tcsg324-1
	XDC:=${CONS_DIR}/$(CONSTRAINT_FILE).xdc
	BOARD_BUILDDIR := ${BUILDDIR}/arty_35
else ifeq ($(TARGET),arty_100)
	PARTNAME:= xc7a100tcsg324-1
	XDC:=${CONS_DIR}/$(CONSTRAINT_FILE).xdc
	DEVICE:= xc7a100t_test
	BOARD_BUILDDIR := ${BUILDDIR}/arty_100
else ifeq ($(TARGET),nexys4ddr)
	PARTNAME:= xc7a100tcsg324-1
	XDC:=${CONS_DIR}/$(CONSTRAINT_FILE).xdc
	DEVICE:= xc7a100t_test
	BOARD_BUILDDIR := ${BUILDDIR}/nexys4ddr
else ifeq ($(TARGET),zybo)
	PARTNAME:= xc7z010clg400-1
	XDC:=${CONS_DIR}/$(CONSTRAINT_FILE).xdc
	DEVICE:= xc7z010_test
	BITSTREAM_DEVICE:= zynq7
	BOARD_BUILDDIR := ${BUILDDIR}/zybo
#   VERILOG:=${current_dir}/counter_zynq.v
else ifeq ($(TARGET),nexys_video)
	PARTNAME:= xc7a200tsbg484-1
	XDC:=${CONS_DIR}/$(CONSTRAINT_FILE).xdc
	DEVICE:= xc7a200t_test
	BOARD_BUILDDIR := ${BUILDDIR}/nexys_video
else
	PARTNAME:= xc7a35tcpg236-1
	XDC:=${CONS_DIR}/$(CONSTRAINT_FILE).xdc
	BOARD_BUILDDIR := ${BUILDDIR}/basys3
endif

.DELETE_ON_ERROR:


all: ${BOARD_BUILDDIR}/${TOP}.bit

${BOARD_BUILDDIR}:
	mkdir -p ${BOARD_BUILDDIR}

${BOARD_BUILDDIR}/${TOP}.eblif: | ${BOARD_BUILDDIR}
	@echo "Running synthesis" >> log.txt
	cd ${BOARD_BUILDDIR} && symbiflow_synth -t ${TOP} -v ${VERILOG} -d ${BITSTREAM_DEVICE} -p ${PARTNAME} -x ${XDC} 2>&1 > /dev/null
	@echo "Synthesis completed" >> log.txt

${BOARD_BUILDDIR}/${TOP}.net: ${BOARD_BUILDDIR}/${TOP}.eblif
	@echo "Running packaging" >> log.txt
	cd ${BOARD_BUILDDIR} && symbiflow_pack -e ${TOP}.eblif -d ${DEVICE} 2>&1 > /dev/null
	@echo "Packaging completed" >> log.txt

${BOARD_BUILDDIR}/${TOP}.place: ${BOARD_BUILDDIR}/${TOP}.net
	@echo "Running placement" >> log.txt
	cd ${BOARD_BUILDDIR} && symbiflow_place -e ${TOP}.eblif -d ${DEVICE} -n ${TOP}.net -P ${PARTNAME} 2>&1 > /dev/null
	@echo "Placement completed" >> log.txt

${BOARD_BUILDDIR}/${TOP}.route: ${BOARD_BUILDDIR}/${TOP}.place
	@echo "Running routing" >> log.txt
	cd ${BOARD_BUILDDIR} && symbiflow_route -e ${TOP}.eblif -d ${DEVICE} 2>&1 > /dev/null
	@echo "Routing completed" >> log.txt

${BOARD_BUILDDIR}/${TOP}.fasm: ${BOARD_BUILDDIR}/${TOP}.route
	@echo "Running fasm generation" >> log.txt
	cd ${BOARD_BUILDDIR} && symbiflow_write_fasm -e ${TOP}.eblif -d ${DEVICE}
	@echo "Fasm generation completed" >> log.txt

${BOARD_BUILDDIR}/${TOP}.bit: ${BOARD_BUILDDIR}/${TOP}.fasm
	@echo "Running bitstream generation" >> log.txt;
	cd ${BOARD_BUILDDIR} && symbiflow_write_bitstream -d ${BITSTREAM_DEVICE} -f ${TOP}.fasm -p ${PARTNAME} -b ${TOP}.bit
	@echo "Bitstream generation completed" >> log.txt

clean:
	rm -rf ${BUILDDIR}