from kb import KMKKeyboard

from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.keys import KC
from kmk.modules.layers import Layers

Mini48 = KMKKeyboard()

Mini48.modules.append(Layers())
Mini48.extensions.append(StringyKeymaps())

MOLYR = KC.MO(1)

# Make this for better looking formatting...
______ = 'NO'

# fmt:off
Mini48.keymap = [[
    # Layer 0 QWERTY
    'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',    'P',
    '1',    '2',    '3',    '4',    '5',    '6',    '7',    '8',    '9',    '0',
    'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L',    'MINS',
    'EXLM', 'AT',   'HASH', 'DLR',  'PERC', 'CIRC', 'AMPR', 'ASTR', 'LPRN', 'RPRN',
    'Z',    'X',    'C',    'V',    'B',    'N',    'M',    'COMM', 'DOT',  'BSPC',
    'EQL',  'LBRC', 'RBRC', 'BSLS', 'SCLN', 'QUOT', 'GRV',  'LABK', 'RABK', 'QUES',
    'ESC',  'LCTL', 'LALT', MOLYR, 'SPC',   'LEFT', 'DOWN', 'UP',   'RGHT', 'ENT',
    '1',    '2',    '3',    '4',    '5',    '6',    '7',    '8',    '9',    '0',
], [
    # Layer 1
    'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',    'P',
    '1',    '2',    '3',    '4',    '5',    '6',    '7',    '8',    '9',    '0',
    'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L',    'MINS',
    'EXLM', 'AT',   'HASH', 'DLR',  'PERC', 'CIRC', 'AMPR', 'ASTR', 'LPRN', 'RPRN',
    'Z',    'X',    'C',    'V',    'B',    'N',    'M',    'COMM', 'DOT',  'BSPC',
    'EQL',  'LBRC', 'RBRC', 'BSLS', 'SCLN', 'QUOT', 'GRV',  'LABK', 'RABK', 'QUES',
    'ESC',  'LCTL', 'LALT', MOLYR, 'SPC',   'LEFT', 'DOWN', 'UP',   'RGHT', 'ENT',
    '1',    '2',    '3',    '4',    '5',    '6',    '7',    '8',    '9',    '0',
]]
# fmt:on

if __name__ == '__main__':
    Mini48.go()
