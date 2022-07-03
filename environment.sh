export INSTALL_DIR=~/opt/f4pga
export FPGA_FAM=xc7
source "$INSTALL_DIR/$FPGA_FAM/conda/etc/profile.d/conda.sh"

if [ $1 = "--activate" ]; then
    echo "Activating environment..."
    conda activate xc7
fi

if [ $1 = "--deactivate" ]; then
    echo "Deactivating environment..."
    conda deactivate
fi


# if [ $1 = "--help" ]; then
#     echo "Usage: $0 [--help] [--activate] [--deactivate] [--fpga-family]"
#     echo "  --help: show this help message and exit"
#     echo "  --activate: activate the conda environment default-fpga-family=xc7"
#     echo "  --deactivate: activate the conda environment"
#     echo "  --fpga-family: set another fpga family"
#     exit 0
# fi