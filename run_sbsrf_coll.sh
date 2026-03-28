#!/bin/bash

for ((i=5; i<=200; i++));
do
    python3 Sbsrf_collection.py "$i" ;
done
