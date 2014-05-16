from PySpotifyControl import spotify_control
import json
import urllib2

class SpeechRecognization(object):
     @staticmethod
     def actionFromInput(speech):
        # standardize input
        speech = speech.strip()
        speech = speech.lower()

        exact_match = {
            'play': ['play'],
            'pause': ['pause', 'paws'],
            'volume up': ['volume up', 'louder'],
            'volume down': ['volume down', 'softer', 'quieter'],
            'next': ['next', 'next song', 'skip', 'skip song'],
            'previous': ['previous', 'previous song', 'back']
        }

        if speech in exact_match['play']:
            # handle play
            spotify_control.play()
        elif speech in exact_match['pause']:
            #handle pause
            spotify_control.pause()
        elif speech in exact_match['volume up']:
            # handle volume up
            spotify_control.volumeUp()
        elif speech in exact_match['volume down']:
            # handle volume down
            spotify_control.volumeDown()
        elif speech in exact_match['next']:
            # handle next song
            spotify_control.next()
        elif speech in exact_match['previous']:
            # handle previous song
            spotify_control.previous()
        elif speech.startswith('play'): # input starts with play but isn't just play
            # to do: add 'play song', 'play track', 'play album'
            # handle play by search
            ## remove play prefix from input
            query = 'http://ws.spotify.com/search/1/track.json?q=' + speech.split(' ',1)[1].replace (" ", "+") # remove first word, replace spaces with plus, make url
            data = json.load(urllib2.urlopen(query))
            spotify_control.playTrack(data["tracks"][0]["href"])

