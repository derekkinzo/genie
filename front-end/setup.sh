#!/bin/bash
pip3 install -r requirements.txt
psql < database.sql
python3 app.py
