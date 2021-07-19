#!/usr/bin/env bash
# Download CSV files of hospitals

for url in $(cat csv-list.txt); do
  wget -O data/raw/$(basename $url) $url
done
