#!/bin/bash
windscribe connect
url='https://nyaa.si/?f=0&c=0_0&q=on+piece+judas+1080'
curl "$url" | grep 'download' | sed -n 's/.*href="\([^"]*\).*/\1/p' > magnetList
windscribe disconnect
