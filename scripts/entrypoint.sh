#!/bin/sh
wandb login $WANDB_API_KEY
python src/main.py --mode wandb_run