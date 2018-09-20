#!/bin/bash

if [ ! -f fibs.csv ]
then
	touch fibs.csv
	for i in $(seq 100); do
		./fib.py $i | tr -d "\n" >> fibs.csv
		echo -n ", ">> fibs.csv
	done
    exit 0
fi
if [ ! -f fibs.csv.bak ]
then
	cp ./fibs.csv ./fibs.csv.bak 
	echo File exists, backup created.
    for i in $(seq 100); do
		./fib.py $i | tr -d "\n" >> fibs.csv
		echo -n ", ">> fibs.csv
	done
    exit 0
fi
echo backup exists
exit 1