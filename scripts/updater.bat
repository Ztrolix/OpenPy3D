@echo off
title OpenPy3D - Console
color 0f

py -m ensurepip --upgrade  --user
py get-pip.py --user

pip install --upgrade pip --user
pip install pygame --user
pip install PyOpenGL --user
pip install tk --user
pip install pillow --user
pip install tqdm --user 
pip install alive-progress --user
pip install pathlib --user
pip install setuptools --user
pip install zipp --user
pip install urllib3 --user
pip install requests --user
pip install colorama --user
pip install grapheme --user
pip install certifi --user
pip install idna --user
pip install charset-normalizer --user
pip install logging --user
pip install noise --user