'''
Instagram Media Exporter
This python app will login to Instagram using your username and password
and download a given instagram account's media list into an excel file

Required libraries: pandas (with excel support), instagrapi
'''

#initializing the app
print('Initializing app...')
import sys
sys.stdout.flush()
import pandas as pd
from instagrapi import Client
import os.path
from os import path

#setting the user agent cookies for the Instagram library
settings = {
   "uuids": {
      "phone_id": "57d64c41-a916-3fa5-bd7a-3796c1dab122",
      "uuid": "8aa373c6-f316-44d7-b49e-d74563f4a8f3",
      "client_session_id": "6c296d0a-3534-4dce-b5aa-a6a6ab017443",
      "advertising_id": "8dc88b76-dfbc-44dc-abbc-31a6f1d54b04",
      "device_id": "android-e021b636049dc0e9"
   },
   "cookies":  {},  # set here your saved cookies
   "last_login": 1596069420.0000145,
   "device_settings": {
      "cpu": "h1",
      "dpi": "640dpi",
      "model": "h1",
      "device": "RS988",
      "resolution": "1440x2392",
      "app_version": "117.0.0.28.123",
      "manufacturer": "LGE/lge",
      "version_code": "168361634",
      "android_release": "6.0.1",
      "android_version": 23
   },
   "user_agent": "Instagram 117.0.0.28.123 Android (23/6.0.1; ...US; 168361634)"
}
cl = Client(settings)


#get user's instagram credentials
igUser = input('What is your Instagram username: ')
igPass = input('What is your Instagram password: ')


#log into instagram
print('Logging into Instagram...')
sys.stdout.flush()
cl.login(igUser, igPass)


#ask the user for the username that we want to export media from
igAccount = input('What is the Instagram user account that you want to export to Excel? ')

#start our loop to go through the list of accounts (or one account if a simple string was entered)
total_count = 0

print('Loading Instagram account: ' + igAccount)
sys.stdout.flush()

#get the Instagram user details using the instagrapi library
user = cl.user_info_by_username(igAccount).pk
media_count = cl.user_info(user).media_count

#increase the total media count
total_count += media_count


print('Instagram accounts loaded successfully...')
print('Total Instagram posts found: ' + str(total_count))
sys.stdout.flush()

#start our loop to go through the list of media

#create a dataframe for this instgram account's media files
df = pd.DataFrame(columns=['IG Account','Post URL','Comments','Likes','Text / Caption'])
columns = list(df)
data = []

user = cl.user_info_by_username(igAccount).pk
media_count = cl.user_info(user).media_count
filename = igAccount + ".xlsx"

#check to see if there is already a file with that name and skip if exists
if path.isfile(filename):
	print('File already exists! Exiting app...')
	exit
else:
	print('Exporting Instagram posts for account: ' + igAccount)
sys.stdout.flush()

media_list = cl.user_medias(user, media_count)

#go through each media and get the details
for media in media_list:

	media_url = "https://www.instagram.com/p/"+media.code
	comments = media.comment_count
	likes = media.like_count
	caption = media.caption_text
	media_row = [igAccount,media_url,comments,likes,caption]
	media_row_z = zip(columns,media_row)
	media_row_d = dict(media_row_z)
	data.append(media_row_d)

#add the media file to our dataset
df = df.append(data, ignore_index=True)

#export our dataset as an excel file
df.to_excel(filename,index=False)

print('Account exported successfully!')
