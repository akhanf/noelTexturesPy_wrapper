#!/bin/bash

#if [ "$#" -lt 4 ]
#then
#    echo "Usage: $0 ID T1 T2 output_dir"
#    exit 1
#fi

if [ "$#" -lt 3 ]
then
    echo "Usage: $0 ID T1 output_dir"
    exit 1
fi

execpath=`dirname $0`
execpath=`realpath $execpath`

container=docker://noelmni/pynoel-gui-app:latest
script=$execpath/run.py

singularity exec -e $container $script $@

