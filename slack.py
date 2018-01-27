from talon.voice import Context, Key

ctx = Context('slack', bundle='com.tinyspeck.slackmacgap')

keymap = {
    'channel': Key('cmd-k'),
    'channel up': Key('alt-up'),
    'channel down': Key('alt-down'),
    'highlight command': ['``', Key('left')],
    'highlight code': ['``````', Key('left left left')],
}

ctx.keymap(keymap)


def unload(): ctx.unload()
