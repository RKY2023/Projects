#!/bin/bash
# url='# https://d27yfew3jd3yhj.cloudfront.net/mpkgr-production-af207a25/qzy4wy/GATE/210924/B3/21ECS01C01T03ST003_LAMA_Vectors/dash/aac_6ba46a15_64k/5.m4s'


# https://d1m7jfoe9zdc1j.cloudfront.net/1a0afa61c672d2cf57e9_gorgc_44288678253_1635862153/chunked/6.ts

# https://www.twitch.tv/videos/1193894895

# <img alt="win win win (lose)" title="2 Nov 2021" data-test-selector="preview-card-thumbnail__image-selector" class="tw-image" src="https://static-cdn.jtvnw.net/cf_vods/d1m7jfoe9zdc1j/1a0afa61c672d2cf57e9_gorgc_44288678253_1635862153//thumb/thumb0-320x180.jpg">

# preview-card-thumbnail__image-selector

# url "https://www.twitch.tv/videos/1193894895" | grep 'preview-card-thumbnail__image-selector' | sed -n 's/.*class="\([^"]*\).*/\1/p' >> magnetList

# dgeft87wbj63p/f0183cfb95ecc3b3454e_arteezy_43696862652_1635883550//thumb/thumb0-320x180.jpg
# https://dgeft87wbj63p.cloudfront.net/f0183cfb95ecc3b3454e_arteezy_43696862652_1635883550/chunked/6.ts
# dgeft87wbj63p/4236d88be25e09733c96_arteezy_43687775804_1635794851//thumb/thumb0-320x180.jpg
# https://dgeft87wbj63p.cloudfront.net/4236d88be25e09733c96_arteezy_43687775804_1635794851/chunked/6.ts


# subDomain='dgeft87wbj63p';
# fileDomainDir='4236d88be25e09733c96_arteezy_43687775804_1635794851';

# # Request URL: https://d2nvs31859zcd8.cloudfront.net/2f23d0fba2f7056f085a_gorgc_40305635851_1638803339/chunked/802.ts
# subDomain='d2nvs31859zcd8';
# fileDomainDir='2f23d0fba2f7056f085a_gorgc_40305635851_1638803339';
url='https://gs-classroom.grdp.co/electron/rec/1655620682285859/stream-'
# url="https://$subDomain.cloudfront.net/$fileDomainDir/chunked/"

a=28
b=830
outfile="vid_`date +%s`.ts"
# -lt is less than operator

#Iterate the loop until a less than 10
while [ $a -lt $b ]
do 
    
    # increment the value
    a=`expr $a + 1`;
    # Print the values
    echo $a
      
    # echo "$url$a.ts"
    curl "$url$a.ts" --output "$a.ts"
    cat "$a.ts" >> "$outfile"
    rm "$a.ts"
done