import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        # half push.
        board.GP14, # COL1
        board.GP12, # COL3
        board.GP11, # COL5
        board.GP10, # COL7
        board.GP9, # COL9
        board.GP8, # COL11
        board.GP7, # COL13
        board.GP6, # COL15
        board.GP5, # COL17
        board.GP4, # COL19

        # full push.
        board.GP15, # COL0
        board.GP13, # COL2
        board.GP18, # COL4
        board.GP19, # COL6
        board.GP20, # COL8
        board.GP21, # COL10
        board.GP22, # COL12
        board.GP26, # COL14
        board.GP27, # COL16
        board.GP28, # COL18
    )

    row_pins = (
        board.GP3, # ROW0
        board.GP2, # ROW1
        board.GP1, # ROW2
        board.GP0, # ROW3
    )

    diode_orientation = DiodeOrientation.COLUMNS
