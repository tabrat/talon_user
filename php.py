from talon.voice import Context, Key

ctx = Context('php', func=lambda app, win: win.doc.endswith('.php'))

keymap = {
    'comment see': '// ',

    'state this': '$this->',
    'state and': ' && ',
    'state or': ' || ',
    'state not': '!',
    'state super': 'parent::',
    'state self': 'self::',
    'state jason': 'json',
    'state jason response': 'JsonResponse::',
    'state sequence': 'Seq',
    'state universe': 'Uuid',
    'state dump': ['dump();', Key('left left')],

}

ctx.keymap(keymap)
