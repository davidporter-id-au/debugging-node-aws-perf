#!/bin/bash -e

# the longest file has only about 140 results
maxLength=140

cd results
rm *.csv || true
cat clj-amazonica.log | grep '[0-9]' | awk '{print $3}' | head -n $maxLength > clj-amazonica.csv
cat clj-faraday.log | grep '[0-9]' | awk '{print $3}' | head -n $maxLength > clj-faraday.csv
cat go.log | sed 's/[^0-9.]*//g' | head -n $maxLength > go.csv
cat node.log | sed 's/[^0-9.]*//g' | head -n $maxLength > node.csv
cat python.log | grep '[0-9]' | head -n $maxLength > python.csv

echo clj-amazonica.csv,clj-faraday.csv,go.csv,node.csv,python.csv > combined.csv
paste -d , clj-amazonica.csv clj-faraday.csv go.csv node.csv python.csv  >> combined.csv
cat combined.csv  | column -t  > ../output.csv
