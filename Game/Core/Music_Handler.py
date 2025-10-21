import pygame

if not pygame.mixer.get_init():
    pygame.mixer.init()

# STATE_MAIN_MENU = 0
# STATE_ACCOUNT_MENU = 1
# STATE_CHARACTER_SELECTION = 2
# STATE_CHARACTER_RACE = 2.5
# STATE_GAME_RUNNING = 3
# STATE_INVENTORY_OPEN = 4
# STATE_STATUS_VIEW = 5
# STATE_SKILLS_VIEW = 6
# STATE_QUESTS_VIEW = 7
# STATE_EQUIPMENT_VIEW = 8
# STATE_CONFIG = 9
# STATE_SETTINGS_MENU = 10

current_music = None

# Maps game states to music files
music_tracks = {
    "0": "Game/Assets/Music/Menu_Theme.mp3",
    "3": "Game/Assets/Music/Game_Theme.mp3",
}

def play_music(state):
    global current_music
    track = music_tracks.get(state)
    if track is None:
        stop_music()
        return
    if current_music != track:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)
        current_music = track

def stop_music():
    global current_music
    pygame.mixer.music.stop()
    current_music = None

