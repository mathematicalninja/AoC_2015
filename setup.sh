#!/bin/bash
ENV_NAME="AoC-2015"


# Path to conda binary (adjust if you installed into ~/miniconda3)
# CONDA_BIN="$HOME/miniconda3/bin/conda"
#
# # Load shell functions into *this* shell
# eval "$($CONDA_BIN shell.bash hook)"

conda env create -f environment.yml -n $ENV_NAME
conda init
conda activate $ENV_NAME

