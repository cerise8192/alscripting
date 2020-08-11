#!/bin/bash

./ehp.py >temp
echo '<HTML>'
echo '<HEAD><TITLE>eHP list</TITLE></HEAD>'
echo '<BODY>'
cat README.head
echo '<P>'
for class in $(cat temp |sed 's/^.*[(]\([^)]*\)[)]\s*$/\1/' | sort | uniq); do
   echo '<h2>'"$class"'</h2>'
   cat temp | grep '[(]'"$class"'[)]' | sed 's/[(][^)]*[)]\s*$//' | sort -nr | sed 's/$/<BR>/'
   echo '<P>'
done
rm temp
echo '</BODY>'
echo '</HTML>'
