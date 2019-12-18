#!/bin/bash
function create(){
    cd Desktop/my_environments {{should be path to your environments folder}}
    source Pygithub/bin/activate {{activate your env}}
    cd ~
    cd Desktop/Projects/PythonProjectAutomation
    python create.py $1
    cd ~
    cd Desktop/Projects/$1
    git init
    git remote add origin https://github.com/{{Github UserName}}/$1.git
    touch README.md
    git add .
    git commit -m "Initial Commit"
    git push -u origin master
    code .
    
}
