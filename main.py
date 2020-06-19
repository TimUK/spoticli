import sys
import spotipy
import spotipy.util as util

import SpotifyApp # this file just contains a client_id and client_secret variable for the spotify app info

scope = 'user-library-read user-modify-playback-state user-read-currently-playing user-read-playback-state'

running = True

username = input("Spotify username: ")

token = util.prompt_for_user_token(username, scope, SpotifyApp.client_id, SpotifyApp.client_secret, 'http://google.com')

if token:
    sp = spotipy.Spotify(auth=token)
    while running:
        cmd = input("SpotiCLI> ")
        if cmd == 'quit':
            running = False
        elif cmd == 'saved':
            results = sp.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print(track['name'] + ' - ' + track['artists'][0]['name'])
        elif cmd == 'play':
                try:
                    sp.start_playback()
                    print("Playing")
                except:
                    print("No active device, trying device 1")
                    sp.start_playback(sp.devices()['devices'][0]['id'])
        elif cmd == 'pause':
            try:
                sp.pause_playback()
                print("Paused")
            except:
                print("No active device")
        elif cmd == 'next':
            try:
                sp.next_track()
                print("Skipping")
            except:
                print("No active device")

        elif cmd == 'previous':
            try:
                sp.previous_track()
                print("Previous...")
            except:
                print("No active device")
        elif cmd == 'playlist':
            playinginfo = sp.current_user_playing_track()
            print("Current playlist: ")
            results = sp.playlist_tracks(playinginfo['context']['uri'].split(":")[4])
            for item in results['items']:
                track = item['track']
                print(track['name'] + ' - ' + track['artists'][0]['name'])
        elif cmd == 'devices':
            print(sp.devices()['devices'][0]['id'])



else:
    print("Can't get token for", username)