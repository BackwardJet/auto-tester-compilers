#!/bin/bash

for i in $( ls *.asm ); do
    eval "c=_out"
    eval "output_file=$i$c"
    echo dummy_text >> $output_file
    rm $output_file
    #echo $output_file
    eval "spim -f $i" >> $output_file
    #echo spim -f $i >> $output_file
    filename=$(echo $i| cut -d'.' -f 1)
    eval "d=.out"
    eval "correct_output=$filename$d"
    echo $correct_output
    eval "python compare_files_asm.py $correct_output $output_file"

done
