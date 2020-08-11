#!/bin/bash

./ehp.py >temp
echo '<HTML>'
echo '<HEAD><TITLE>eHP list</TITLE></HEAD>'
echo '<BODY>'
for class in $(cat temp |sed 's/^.*[(]\([^)]*\)[)]\s*$/\1/' | sort | uniq); do
   echo '<h2>'"$class"'</h2>'
   cat temp | grep '[(]'"$class"'[)]' | sed 's/[(][^)]*[)]\s*$//' | sort -nr
   echo '<P>'
done
rm temp
echo '</BODY>'
echo '</HTML>'
