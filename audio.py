from talon.voice import Key, Context
from subprocess import Popen, PIPE

ctx = Context('audio')


def run_script(script, args=[]):
    p = Popen(['osascript', '-'] + args, stdin=PIPE,
              stdout=PIPE, stderr=PIPE, universal_newlines=True)
    p.communicate(script)
    p.terminate()


def play_pause(m):
    script = '''tell app "Spotify" to playpause'''
    run_script(script)


def next_track(m):
    script = '''tell app "Spotify" to play next track'''
    run_script(script)


def previous_track(m):
    script = '''tell app "Spotify" to play previous track'''
    run_script(script)


keymap = {
    'play pause': play_pause,
    'next track': next_track,
    'previous track': previous_track,
}

ctx.keymap(keymap)


def unload(): ctx.unload()
