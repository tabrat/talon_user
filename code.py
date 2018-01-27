from talon.voice import Context, Key

languages = ['.php', '.py', '.java']
bundles = ['com.postmanlabs.mac']

ctx = Context('code', func=lambda app, win:
              any(app.bundle == b for b in bundles)
              or any(win.doc.endswith(l) for l in languages)
              )

keymap = {
    'sinker': [Key('cmd-right ;')],

    'args': ['()', Key('left')],
    'angler': ['<>', Key('left')],
    '(block | kirblock)': ['{}', Key('left enter')],
    'args-block': ['(', Key('enter')],
    'brax-block': ['[', Key('enter')],

    'coalshock': [':', Key('enter')],
    'coal twice': '::',
    'ellipsis': '...',
    'mintwice': '--',
    'plustwice': '++',

    '(indirect | reference)': '&',
    '([is] equal to | longqual)': ' == ',
    '([is] not equal to | banquall)': ' != ',
    'trickle': ' === ',
    '(ranqual | nockle)': ' !== ',
    '(call | prekris)': '()',

    '(index | brax)': ['[]', Key('left')],
    '(empty dict | kirk)': ['{}', Key('left')],

    '(empty array | brackers)': '[]',
    'empty dict': '{}',
    'minquall': '-=',
    'pluqual': '+=',
    'starqual': '*=',
    'lessqual': ' <= ',
    'grayqual': ' >= ',

    '(arrow | lambo)': '->',
    'shrocket': ' => ',

    'state if': ['if ()', Key('left')],
    'state else': ['else {}', Key('left enter')],
    'state else if': ['else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state for each': ['foreach ()', Key('left')],
    'state switch': ['switch ()', Key('left')],

    'const': 'const ',
    'static': 'static ',
    'tip pent': 'int ',

    'word no': 'null',
    'word printf': 'printf',
    'word define': 'def ',
    'word import': 'import ',
}

ctx.keymap(keymap)


def unload(): ctx.unload()
