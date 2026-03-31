#!/bin/bash

for ((i=479; i<=1153; i++));
do
    python3 ore_deposits.py "$i" ;
done