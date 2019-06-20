"""
Enter all your personal information in this file
"""

"""Reddit Identification"""
# Enter your personal reddit acount information
# Create a Reddit application under https://old.reddit.com/prefs/apps/

application_id_reddit = ''
application_secret_reddit = ''
password_reddit = ''
user_agent_reddit = ''
username_reddit = ''


"""Spotify Identification"""
# To use the Spotify Api you have to create a Spotify app under https://developer.spotify.com/dashboard/applications
# Enter your username, scope (what you want to do to the account or with the api. I used the needed scopes for this
# script. Look at the documentation for more) and finally the playlist ID where the songs should be saved.

username_spotify = ''
scope_spotify = 'playlist-modify-private,playlist-modify-public'
client_id_spotify = ''
client_secret_spotify = ''
redirect_uri_spotify = 'https://google.de/'
playlist_id = ''


"""Script variables"""
# Enter the:
#    Search limit for Reddit (max. 967)
#    With What filter the Subreddit should be searched ('day' / 'month' / 'year' / 'all')
#    The max size for your Spotify playlist
#    If you want to print the Debug Data

reddit_search_limit = 100
time_filter_reddit_search = 'month'
playlist_size_limit = 50
printDebugData = True
