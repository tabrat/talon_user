from talon.voice import Key, press, Str, Context

# Move and resize windows with Spectacle.app

ctx = Context('spectacle')


keymap = {
    'windy center': Key('cmd-alt-f'),
    'windy max': Key('cmd-alt-f'),

    'windy left': Key('cmd-alt-left'),
    'windy right': Key('cmd-alt-right'),
    'windy top': Key('cmd-alt-top'),
    'windy bottom': Key('cmd-alt-bottom'),

    'windy upper left': Key('cmd-ctrl-left'),
    'windy lower left': Key('cmd-ctrl-shift-left'),
    'windy upper right': Key('cmd-ctrl-right'),
    'windy lower right': Key('cmd-ctrl-shift-right'),

    'windy next display': Key('cmd-ctrl-alt-right'),
    'windy previous display': Key('cmd-ctrl-alt-left'),

    'windy next third': Key('ctrl-alt-right'),
    'windy previous third': Key('ctrl-alt-left'),

    'windy larger': Key('shift-ctrl-alt-right'),
    'windy smaller': Key('shift-ctrl-alt-left'),

    'windy undo': Key('cmd-alt-z'),
    'windy redo': Key('cmd-alt-shift-z'),

}

ctx.keymap(keymap)
