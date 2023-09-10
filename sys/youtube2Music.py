# yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' https://www.youtube.com/watch?v=Jlfgtb1_qlI --downloader ffmpeg --downloader-args "ffmpeg_i:-ss 175 -to 1125"
import json
import yt_dlp
import ffmpeg
import os
from pydub import AudioSegment
# pip install ffmpeg-python
def downloadfullaudio():
    URL = 'https://www.youtube.com/watch?v=dSoFCCEOQ8o'

    ydl_opts = {
        'output': '%(title)s.%(ext)s',
        'format': 'm4a/bestaudio/best',
        
        # 'postprocessors': [{  # Extract audio using ffmpeg
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'm4a',
        # }]
    }
    # t=[]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)
        # print(json.dumps(ydl.sanitize_info(info)))
        # t = ydl.sanitize_info(info)
        er = ydl.download(URL)

def tt(file):
    # # Open an mp3 file
    # song = AudioSegment.from_file(file, format="m4a")
    
    # # pydub does things in milliseconds
    # ten_seconds = 10 * 1000
    
    # # song clip of 10 seconds from starting
    # first_10_seconds = song[:ten_seconds]
    
    # # save file
    # first_10_seconds.export("first_10_seconds.m4a",
    #                         format="m4a")
    # print("New Audio file is created and saved")
    import ffmpeg

    audio_input = ffmpeg.input("output_sounddevice.m4a")
    audio_cut = audio_input.audio.filter('atrim', duration=1)
    audio_output = ffmpeg.output(audio_cut, 'trimmed_output_ffmpeg.m4a', format='m4a')

def movefile():
    allfiles = os.listdir('D:\\work')
    for f in allfiles:
        ff = f.split('.')
        if(ff[len(ff)-1]=='m4a'):
            src_path = os.path.join('D:\\work', f)
            dst_path = os.path.join('D:\\Music', f)
            print(f)
            # tt(f)
            mav = os.rename(src_path, dst_path)

# downloadfullaudio()
# movefile()
tt('aa.m4a')