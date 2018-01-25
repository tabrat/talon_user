from talon.voice import Word, Key, Context

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(t in app.bundle for t in terminals))

keymap = {
	'cd': 'cd ',
    '(ls | run ellis | run alice)': 'ls\n',
    'run make (durr | dear)': 'mkdir ',
    'run jet': 'git ',
    'run jet clone': 'git clone ',
    'run jet diff': 'git diff ',
    'run jet commit': 'git commit ',
    'run jet push': 'git push ',
    'run jet pull': 'git pull ',
    'run jet status': 'git status ',
    'run jet add': 'git add ',
}

ctx.keymap(keymap)
def unload(): ctx.unload()