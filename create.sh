#!/bin/bash

python3 create.py $1
cd /home/ionica/Documents/Projects/$1
echo "#readme" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/dinuionica/$1.git
git push -u origin main
code .
