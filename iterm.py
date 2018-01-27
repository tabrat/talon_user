from talon.voice import Key, Context

ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    'full-screen': Key('cmd-shift-enter'),
    'exit session': [Key('ctrl-c'), 'exit\n'],
    'broadcaster': Key('cmd-alt-i'),
    'clear session': [Key('ctrl-c'), 'clear\n'],
    'split horizontal': Key('cmd-shift-d'),
    'split vertical': Key('cmd-d'),
}

ctx.keymap(keymap)


def unload(): ctx.unload()
