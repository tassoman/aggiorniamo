#!/bin/bash
python3 -m venv env
. env/bin/activate
python --version
pip install -r requirements.txt
