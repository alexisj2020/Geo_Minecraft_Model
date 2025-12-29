#!/bin/bash

for ((i=0; i<=256; i++))
do
    python3 Sbsrf_collection.py "$i" ;
done
