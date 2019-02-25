#!/bin/bash

cd ./edx_archives

for f in *.gz;
	do
	gunzip -c "$f" > ./data_source/"${f%.*}";
	done;
