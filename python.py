from talon.voice import Context, Key

ctx = Context('python', func=lambda app, win: '.py' in win.title)

keymap = {
	'state any': ['any()', Key('left')], 
}

ctx.keymap(keymap)
def unload(): ctx.unload()