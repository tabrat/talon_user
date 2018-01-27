from talon.voice import Context, Key

ctx = Context('java', func=lambda app, win: win.doc.endswith('.java'))

keymap = {
    'state this': 'this.',
    'state and': ' && ',
    'state or': ' || ',
    'state super': 'super.',
    'state jason': 'Json',
    'state sequence': 'Seq',
    'state universe': 'UUID',
}

ctx.keymap(keymap)


def unload(): ctx.unload()
