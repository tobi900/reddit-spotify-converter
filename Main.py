"""
This script takes the top posts from a subreddit (programmed for the formatting of r/listentothis)
and adds them to a Spotify playlist.
Add your personal information, accounts and the playlist Id in InputData.

---Run this Script, not Input Data!
"""
import re
import praw
import time
import InputData
import spotipy
import spotipy.util as util


def get_reddit_data():
    """Requests top reddit posts"""
    for submission in reddit.subreddit('listentothis').top(time_filter=InputData.time_filter_reddit_search,
                                                           limit=InputData.reddit_search_limit):
        data.append(submission.title)


def cleanup(data_var, return_data_var, cleanup_type):
    """Replaces unwanted chars with regular expressions"""
    ''' 
        cleanup_type 0 for first cleanup 
        cleanup_type 1 for second cleanup
    '''
    if cleanup_type == 0:
        for h in data_var:
            u = str(h)
            u = re.sub('\[.*]', '', u)
            u = re.sub('\(.*\)', '', u)
            u = u.replace('  ', ' ')
            u = u.replace('--', '-')
            u = u.replace('—', '-')
            u = u.replace('”', '')
            u = u.replace('“', '')
            u = u.replace(',', '')
            u = u.replace('\'', '')
            for year in years:
                u = u.replace(year, '')
            return_data_var.append(u)

    if cleanup_type == 1:
        for i in data_var:
            i = str(i)
            i = re.sub('\[', '', i)
            i = re.sub(']', '', i)
            i = re.sub('—', '', i)
            i = re.sub('\'', '', i)
            i = re.sub(',', '', i)
            i = re.sub('  ', ' ', i)
            i = re.sub('\(.*\)', '', i)
            for year in years:
                i = i.replace(year, '')
            return_data_var.append(i)


def swap_arist_songname(data_var, output_list):
    """
    Track and Artist are seperated by a "-".
    To improve search results I swap their position.
    Artist - Song title --> Song title - Artist
    """
    for j in data_var:
        u = j.split("-")
        u.insert(0, u[-1])
        u.pop(-1)
        output_list.append(u)


def get_track_id(track_seatch_tags):
    """
    Enters search tags (name and artist) and returns the Track ID to a list.
    """
    try:
        results = spotify.search(q='track:' + track_seatch_tags, type='track', limit=1)
        if printResults:
            print("Result for:", track_seatch_tags, "=============: ", results)
        all_track_ids.append(results['tracks']['items'][0]['id'])
    except:
        pass


def remove_duplicates(list_object):
    for j, index in zip(reversed(list_object), range(len(list_object))):
        duplicate = 0
        for i in reversed(list_object):
            if j == i:
                duplicate += 1
                if duplicate == 2:
                    list_object.pop(list_object.index(j, list_object.index(j) + 1))


def spotify_add_track(track_id):
    spotify.user_playlist_add_tracks(user=InputData.username_spotify,
                                     playlist_id=InputData.playlist_id,
                                     tracks=[track_id]
                                     )


def print_row(filename, addition_status):
    """
    Prints Song addition Information with nice formatting.
    """
    print(" %-110s %45s" % (filename, addition_status))


def main():
    """
    Where the actual work gets done.
    """
    get_reddit_data()
    cleanup(data, data_cl, 0)
    swap_arist_songname(data_cl, data_rev)
    cleanup(data_rev, fl_output, 1)
    if printRedditData:
        print("Data 1: (cleaned)", "Length:", len(data_cl), data_cl)
        print("Data 2: (reversed)", "Length:", len(fl_output), fl_output)

    for l1, l2 in zip(data_cl, fl_output):      # Combine data_cl an fl_output into one list
        all_tracks.append(l1)
        all_tracks.append(l2)

    for reee in all_tracks:
        get_track_id(reee)

    remove_duplicates(all_track_ids)

    loop = True
    while loop:
        if len(all_track_ids) > InputData.playlist_size_limit:
            all_track_ids.pop(-1)
        if len(all_track_ids) <= InputData.playlist_size_limit:
            loop = False

    for lul in all_track_ids:
        spotify_add_track(lul)


if __name__ == '__main__':
    """
    Mostly preperation and the Setup for the main script.
    """
    data = []
    data_cl = []
    data_rev = []
    fl_output = []
    all_track_ids = []
    added_tracks = []
    all_tracks = []

    printRedditData = InputData.printDebugData
    printResults = InputData.printDebugData
    printTrackInformation = InputData.printDebugData
    printTrackAdditionStatus = InputData.printDebugData
    printNeededTime = InputData.printDebugData

    '''
    Creates a list with years from 1800 to 2020.
    Titles with for example (2017) in them were sometimes not removed.
    '''
    start = 1800
    years = []
    for year_l in range(220):
        years.append(str(year_l))
        start += 1

    """Reddit verification"""
    reddit = praw.Reddit(client_id=InputData.application_id_reddit,
                         client_secret=InputData.application_secret_reddit,
                         password=InputData.password_reddit,
                         user_agent=InputData.user_agent_reddit,
                         username=InputData.username_reddit
                         )

    """Spotify Verification"""
    spotify = spotipy.Spotify(auth=util.prompt_for_user_token(username=InputData.username_spotify,
                                                              scope=InputData.scope_spotify,
                                                              client_id=InputData.client_id_spotify,
                                                              client_secret=InputData.client_secret_spotify,
                                                              redirect_uri=InputData.redirect_uri_spotify
                                                              )
                              )

    time_start = time.time()
    main()
    time_end = time.time()
    if printNeededTime:
        needed_time = time_end - time_start
        print(" Needed time: {}s".format(needed_time))

        
# Test
