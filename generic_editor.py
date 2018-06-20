from talon.voice import Key, press, Str, Context

ctx = Context('generic_editor')  # , bundle='com.microsoft.VSCode')

numeral_map = dict((str(n), n) for n in range(0, 20))
for n in [20, 30, 40, 50, 60, 70, 80, 90]:
    numeral_map[str(n)] = n
numeral_map["oh"] = 0  # synonym for zero

numerals = ' (' + ' | '.join(sorted(numeral_map.keys())) + ')+'
optional_numerals = ' (' + ' | '.join(sorted(numeral_map.keys())) + ')*'


def text_to_number(m):

    tmp = [str(s).lower() for s in m.dgndictation[0]._words]
    words = [parse_word(word) for word in tmp]

    result = 0
    factor = 1
    for word in reversed(words):
        if word not in numerals:
            raise Exception('not a number')

        result = result + factor * int(numeral_map[word])
        factor = 10 * factor

    return result


def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    return word


def jump_to_bol(m):
    line = text_to_number(m)
    press('ctrl-g')
    Str(str(line))(None)
    press('enter')


def jump_to_end_of_line():
    press('cmd-right')


def jump_to_beginning_of_text():
    press('cmd-left')


def jump_to_nearly_end_of_line():
    press('left')


def jump_to_bol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m._words[1:])
        else:
            press('ctrl-a')
            press('cmd-left')
        then()
    return fn


def jump_to_eol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m._words[1:])
        press('cmd-right')
        then()
    return fn


def toggle_comments():
    # works in VSCode with Finnish keyboard layout
    # press('cmd-shift-7')

    # does not work in VSCode, see https://github.com/talonvoice/talon/issues/3
    press('cmd-/')


def snipline():
    press('shift-cmd-right')
    press('delete')
    press('delete')
    press('ctrl-a')
    press('cmd-left')


def find_next(m):
    press('cmd-f')
    Str(str(m.dgndictation[0]._words[0]))(None)
    press('escape')


def find_previous(m):
    press('left')
    press('cmd-f')
    Str(str(m.dgndictation[0]._words[0]))(None)
    press('cmd-shift-g')
    press('escape')


keymap = {
    'sprinkle' + optional_numerals: jump_to_bol,
    'spring' + optional_numerals: jump_to_eol_and(jump_to_beginning_of_text),
    'dear' + optional_numerals: jump_to_eol_and(lambda: None),
    'smear' + optional_numerals: jump_to_eol_and(jump_to_nearly_end_of_line),
    'trundle' + optional_numerals: jump_to_bol_and(toggle_comments),
    'jolt': [
        # go to beginning of text
        Key('ctrl-a cmd-left'),

        # select and copy the line
        Key('cmd-shift-right cmd-c'),

        # go to EOL and add a new line
        Key('cmd-right enter'),

        # paste and go to beginning of text
        Key('cmd-v cmd-left'),
    ],

    'snipline' + optional_numerals: jump_to_bol_and(snipline),

    # NB these do not work properly if there is a selection
    'snipple': Key('shift-cmd-left delete'),
    'snipper': Key('shift-cmd-right delete'),

    'bracken': [Key('cmd-shift-ctrl-right')],

    # poor implementations:
    'crew <dgndictation>': find_next,
    'trail <dgndictation>': find_previous,

    'shockey': Key('ctrl-a cmd-left enter up'),
    'shockoon': Key('cmd-right enter'),
    'sprinkoon' + numerals: jump_to_eol_and(lambda: press('enter')),
}

ctx.keymap(keymap)
