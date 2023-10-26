#! /bin/bash
rm -rf .variable.txt

touch .variable.txt
echo "creating yml filefiles"
echo " "
python3 .ymlcreater.py
echo "#####################################################"
echo " "
echo "http://10.21.3.168/ymlfiles/hostname/files"
