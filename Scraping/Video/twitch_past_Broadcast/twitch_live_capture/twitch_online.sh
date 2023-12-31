#!/bin/bash
# url='https://d2nvs31859zcd8.cloudfront.net/1d1f7f686d39067e2b3a_cinylooney_39974504139_1631817310/chunked/145.ts'
url='https://d2nvs31859zcd8.cloudfront.net/1d1f7f686d39067e2b3a_cinylooney_39974504139_1631817310/chunked/'
url='https://dgeft87wbj63p.cloudfront.net/5e1427d871f1885e0ace_gorgc_43472872860_1633674616/chunked/'
a=0
b=430
b=3828
outfile="vid_`date +%s`.ts"
outfileLog="vid_`date +%s`.log"
# -lt is less than operator

#Iterate the loop until a less than 10
while [ $a -lt $b ]
do 
    
    # increment the value
    a=`expr $a + 1`;
    # Print the values
    echo $a
      
    # echo "$url$a.ts"
    (`curl "$url$a.ts" --output "$a.ts"`) 

    cat "$a.ts" >> "$outfile"
    echo "$url$a.ts" >> "$outfileLog"
    
    rm "$a.ts"
done