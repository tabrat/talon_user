from talon.voice import Context, Key

ctx = Context('python', func=lambda app, win: win.doc.endswith('.py'))

keymap = {
    'state any': ['any()', Key('left')],
}

ctx.keymap(keymap)
