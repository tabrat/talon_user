from talon.voice import Context, Key

ctx = Context('navigation')

keymap = {
    # Application navigation
    'swick': Key('cmd-tab'),
    'totch': Key('cmd-w'),
    'new window': Key('cmd-n'),
    '(next window | gibby)': Key('cmd-`'),
    '(last window | shibby)': Key('cmd-shift-`'),
    '(new tab | peach)': Key('cmd-t'),
    '(next tab | goneck)': Key('ctrl-tab'),
    '(last tab | gopreev)': Key('ctrl-shift-tab'),
    'next space': Key('cmd-alt-ctrl-right'),
    'last space': Key('cmd-alt-ctrl-left'),

    # deleting
    'snipline': [Key('cmd-right cmd-backspace')],
    'steffi': [Key('alt-ctrl-backspace')],
    'stippy': [Key('alt-ctrl-delete')],
    'carmex': [Key('alt-backspace')],
    'kite': [Key('alt-delete')],
    'snipple': Key('cmd-shift-left delete'),
    'snipper': Key('cmd-shift-right delete'),

    # moving
    '(tab | tarp)':   Key('tab'),
    'tarsh': Key('shift-tab'),
    'slap': [Key('cmd-right enter')],
    'shocker': [Key('cmd-left enter up')],
    'wonkrim': Key('alt-ctrl-left'),
    'wonkrish': Key('alt-ctrl-right'),
    'fame': Key('alt-left'),
    'fish': Key('alt-right'),
    'ricky': Key('cmd-right'),
    'lefty': Key('cmd-left'),
    '(left | crimp)': Key('left'),
    '(right | chris)': Key('right'),
    '(up | jeep)': Key('up'),
    '(down | dune | doom)':  Key('down'),

    'scroll down': [Key('down')] * 30,
    '(doomway | scroll way down)': Key('cmd-down'),
    'scroll up': [Key('up')] * 30,
    '(jeepway | scroll way up)': Key('cmd-up'),

    # selecting
    'shreepway': Key('cmd-shift-up'),
    'shroomway': Key('cmd-shift-down'),
    'shreep': Key('shift-up'),
    'shroom': Key('shift-down'),
    'lecksy': Key('cmd-shift-left'),
    'ricksy': Key('cmd-shift-right'),
    'scram': Key('alt-shift-left'),
    'scrish': Key('alt-shift-right'),
    'schrim': Key('shift-left'),
    'shrish': Key('shift-right'),
}

ctx.keymap(keymap)


def unload(): ctx.unload()
