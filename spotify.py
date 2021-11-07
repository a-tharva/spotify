from time import sleep
from os import system

from spotipy import Spotify, SpotifyOAuth
from pynput.keyboard import Key, Controller

class SpotifyClient:

    def __init__(self, client_id: Optional[str] = None, client_secret: Optional[str] = None,
                 username: Optional[str] = None):
        self._spotify = Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                username=username,
                redirect_uri='https://www.google.com',
            )
        )

        self._keyboard = Controller()

    @staticmethod
    def opn():
        system('spotify.exe')
        sleep(0.25)

    @staticmethod
    def close():
        system("taskkill /f /im spotify.exe")
        sleep(0.25)

    def play(self):
        sleep(1.5)
        self._keyboard.press(Key.media_play_pause)
        self._keyboard.release(Key.media_play_pause)
        self._keyboard.press(Key.media_next)
        self._keyboard.release(Key.media_next)
        sleep(2.0)
        self._keyboard.press(Key.alt_l)
        self._keyboard.press(Key.tab)
        self._keyboard.release(Key.alt_l)
        self._keyboard.release(Key.tab)

    def restart(self):
        self.close()
        self.opn()
        self.play()

    def current_user_playing_track(self) -> dict:
        return self._spotify.current_user_playing_track()
    
if __name__ == '__main__':
    spotify = SpotifyClient(
        username='INSERT_USERNAME',
        client_id='INSERT_CLIENT_ID',
        client_secret='INSERT_CLIENT_SECRET'
    )
    # Or use environment variables
    # spotify = SpotifyClient()

    while True:
        if spotify.current_user_playing_track()['currently_playing_type'] == 'ad':
            spotify.restart()
        sleep(1)