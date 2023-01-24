#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:58:14 2023

@author: dannelson
"""

import os
from pathlib import Path

projectName = 'projectName4'

directory=projectName
parent_dir = "/Users/dannelson/Desktop/"
path=os.path.join(parent_dir, directory)
os.mkdir(path)
print(f"Directory {directory} created")


directory="helpers"
parent_dir = f"/Users/dannelson/Desktop/{projectName}"
path=os.path.join(parent_dir, directory)
os.mkdir(path)
print(f"Directory {directory} created")


directory="tests"
parent_dir = f"/Users/dannelson/Desktop/{projectName}"
path=os.path.join(parent_dir, directory)
os.mkdir(path)
print(f"Directory {directory} created")

directory="src"
parent_dir = f"/Users/dannelson/Desktop/{projectName}"
path=os.path.join(parent_dir, directory)
os.mkdir(path)
print(f"Directory {directory} created")

Path(f'/Users/dannelson/Desktop/{projectName}/tests/__init__.py').touch()
Path(f'/Users/dannelson/Desktop/{projectName}/src/__init__.py').touch()
Path(f'/Users/dannelson/Desktop/{projectName}/helpers/__init__.py').touch()
Path(f'/Users/dannelson/Desktop/{projectName}/main.py').touch()
print('all files created')
print('Jobfinished.')