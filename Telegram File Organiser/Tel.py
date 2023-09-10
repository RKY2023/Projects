## install python3 ##
#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade telethon
#python3 -m pip install tqdm

## Links
# https://tl.telethon.dev/methods/channels/get_full_channel.html
# https://core.telegram.org/methods

import re
import gdown
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from tqdm import tqdm

api_id = 25625372       # Your API ID
api_hash = 'f156d103def33a79bf838c8b9afa7e1f'  # Your API HASH


# def download_media(group, cl, name):
#     messages = cl.get_messages(group, limit=2000)

#     for message in tqdm(messages):
#         message.download_media('./' + name + '/')


with TelegramClient('name', api_id, api_hash) as client:
    ## check login start ##
    # client.send_message('me','Hello, myself')
    # print(client.download_profile_photo('me'))
    ## check login end ##

    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        # offset_peer=InputPeerEmpty(),
        offset_peer='username',
        limit=500,
        hash=0,
    ))

    # title = 'RkyGroupTest1'            # Title for group chat
    # for chat in result.chats:
        # print(chat)

        # if chat.title == title:
        #     messages = client.get_messages(chat,limit=2000)
        #     for message in tqdm(messages):
        #         # print(message)
        #         message.download_media('./' + title + './')
        #     # download_media(chat, client, title)

    title = 'Prashant Tiwari'            # Title for group chat
    for chat in result.chats:
        # print(chat)

        if chat.title == title:
            messages = client.get_messages(chat,limit=10)
            for message in tqdm(messages):
                print(message.date)
                print(message.message)
                url = re.search("(?P<url>https?://drive[^\s]+)", str(message.message))
                print(url)
                output = './'
                url = "https://drive.google.com/file/d/1qy10dGIK35t-yB3HlgYCNwrLjyLDkJ50/view"
                gdown.download(url, output, quiet=False)
                # message.download_media('./' + title + './')
            # download_media(chat, client, title)

    # title = 'RkyGroupTest1'         # Title for channel
    # channel = client(GetFullChannelRequest(title))
    # print(channel.full_chat)

    # messages = client.get_messages(channel.full_chat,limit=2000)

    # for message in tqdm(messages):
    #     message.download_media('./' + title + './')

    # download_media(channel.full_chat, client, title)