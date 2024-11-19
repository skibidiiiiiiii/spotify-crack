import os
import ctypes

def fermer_spotify():
    try:
        os.system('taskkill /F /IM spotify.exe >nul 2>&1')
        ctypes.windll.user32.MessageBoxW(0, "echec du lancement du crack", "Statut", 0x40)
    except Exception:
        ctypes.windll.user32.MessageBoxW(0, "Échec de la fermeture de Spotify", "Erreur", 0x10)

def verifier_spotify_installe():
    spotify_path = os.path.expandvars(r"%AppData%\Spotify")
    if os.path.exists(spotify_path):
        fermer_spotify()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Spotify n'est pas installé sur ce PC.", "Information", 0x40)

verifier_spotify_installe()
