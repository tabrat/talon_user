from talon.voice import Context, Key

ctx = Context('application')

keymap = {
	'prefies': Key('cmd-,'),
	'marco': Key('cmd-f'),
}

ctx.keymap(keymap)


def unload(): ctx.unload()
