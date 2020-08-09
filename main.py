import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

class Playlistify:
  def __init__(self, nome: str, qte_musicas: int, genre: str, danceablity: float):
    self.nome = nome
    self.qte_musicas = qte_musicas
    self.genre = genre
    self.danceability = danceablity

    # Spotify Stuff
    self.spotify = 