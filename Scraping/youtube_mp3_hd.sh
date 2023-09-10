#!/bin/bash
# url='https://d2nvs31859zcd8.cloudfront.net/1d1f7f686d39067e2b3a_cinylooney_39974504139_1631817310/chunked/145.ts'
url='https://www.youtube.com/watch?v=phqPyCUF5Fk'
#youtube-dl --postprocessor-args -h "https://www.youtube.com/watch?v=ULEQb_l-N08"
#youtube-dl --postprocessor-args "-ss 00:02:20 -to 00:02:50" "$url"
#youtube-dl -f bestaudio --extract-audio --embed-thumbnail --add-metadata <Video-URL>
#youtube-dl -f bestaudio[ext=m4a] --embed-thumbnail --add-metadata <Video-URL>

youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata "$url"
