from talon.voice import Context

ctx = Context('words')

keymap = {
    'dot pie': '.py',
    'word queue': 'queue',
    'word enqueue': 'enqueue',
    'word cmd': 'cmd',
}

ctx.keymap(keymap)


def unload(): ctx.unload()
