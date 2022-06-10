import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

row1 = board.GP16
row2 = board.GP17
row3 = board.GP18
row4 = board.GP19
row5 = board.GP20
row6 = board.GP21
row7 = board.GP22
row8 = board.GP26

col1 = board.GP0
col2 = board.GP1
col3 = board.GP2
col4 = board.GP3
col5 = board.GP4
col6 = board.GP5
col7 = board.GP6
col8 = board.GP7
col9 = board.GP8
col10 = board.GP9
col11 = board.GP10
col12 = board.GP11
col13 = board.GP12
col14 = board.GP13
col15 = board.GP14
col16 = board.GP15


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        col1,
        col2,
        col3,
        col4,
        col5,
        col6,
        col7,
        col8,
        col9,
        col10, 
        col11,
        col12,
        col13,
        col14,
        col15,
        col16
    )
    row_pins = (
        row1,
        row2,
        row3,
        row4,
        row5,
        row6,
        row7,
        row8
    )
    diode_orientation = DiodeOrientation.COL2ROW
