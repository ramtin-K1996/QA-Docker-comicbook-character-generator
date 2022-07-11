#!/bin/bash

declare -a dirs=(service_1 service_2 service_3 service_4)

for dir in ${dirs[@]}; do
 cd ${dir}
 pip3 install -r requirements.txt
 python3 -m pytest --cov application 
 cd .. 

done


