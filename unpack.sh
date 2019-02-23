#!/bin/bash

cd ~/open_ifmo_ru

for f in *.gz;
	do
	gunzip -c "$f" > ~/logs/"${f%.*}";
	done;
