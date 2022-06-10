from kmk.extensions.lock_status import LockStatus
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.extensions import lock_status
from kb import KMKKeyboard
import digitalio
import board
print("Starting")


keyboard = KMKKeyboard()

# led statuses
locks = LockStatus()
keyboard.extensions.append(locks)

# led mappings
INACTIVE = False
ACTIVE = True

led_num_lock = digitalio.DigitalInOut(board.GP27)  # change to pin of LED
led_num_lock.direction = digitalio.Direction.OUTPUT
led_caps_lock = digitalio.DigitalInOut(board.GP28)  # change to pin of LED
led_caps_lock.direction = digitalio.Direction.OUTPUT

# for some reason this has to be set to disabled led at start
led_num_lock.value = ACTIVE
led_caps_lock.value = ACTIVE


keyboard.modules = [
    Layers(),
]

# Keys mapping
SUPER = KC.LWIN
SHIFT = KC.LSHIFT
RSHIFT = KC.RSHIFT
LCTRL = KC.LCTRL
RCTRL = KC.RCTRL
ALT = KC.LALT
RALT = KC.RALT
TAB = KC.TAB
ESC = KC.ESCAPE
ENTER = KC.ENTER
SPACE = KC.SPACE
BACK = KC.BACKSPACE
DEL = KC.DELETE
# CAPS = KC.CAPS
CAPS = SUPER

XX = KC.NO
NONE = XX
TO_CHECK = XX
___ = XX


def update_capslock_led_state(*args, **kwargs):
    if locks.get_caps_lock():
        led_caps_lock.value = ACTIVE
    else:
        led_caps_lock.value = INACTIVE


def update_numlock_led_state(*args, **kwargs):
    if locks.get_num_lock():
        led_num_lock.value = ACTIVE
    else:
        led_num_lock.value = INACTIVE


KC.CAPSLOCK.after_press_handler(update_capslock_led_state)
KC.NUMLOCK.after_press_handler(update_numlock_led_state)

# Settings
keyboard.tap_time = 350
keyboard.debug_enabled = False

# keymap
keyboard.keymap = [
    [
        ___, ___, ___, ___, ___, KC.B, SPACE, KC.N, RSHIFT, ___, KC.SLASH, KC.DOWN, KC.RIGHT, ___, KC.LEFT, RALT,
        RCTRL, ___, KC.Z, KC.X, KC.C, KC.V, ENTER, KC.M, KC.COMMA, KC.DOT, KC.BSLASH, KC.NUMLOCK, KC.KP_SLASH, KC.KP_ASTERISK, KC.PAUSE, ___,
        ___, ___, KC.A, KC.S, KC.D, KC.F, ___, KC.J, KC.K, KC.L, KC.SCOLON, KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_ENTER, ___,
        ___, ___, KC.Q, KC.W, KC.E, KC.R, ___, KC.U, KC.I, KC.O, KC.P, KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_PLUS, KC.SCROLLLOCK,
        ___, ___, KC.N1, KC.N2, KC.N3, KC.N4, KC.F10, KC.N7, KC.N8, KC.N9, KC.N0, KC.F11, KC.F12, KC.PGDOWN, KC.END, KC.PSCREEN,  # V
        LCTRL, ___, KC.ZKHK, KC.F1, KC.F2, KC.N5, KC.F9, KC.N6, KC.EQUAL, KC.F8, KC.MINUS, DEL, KC.INSERT, KC.PGUP, KC.HOME, KC.Q,  # V
        ___, SHIFT, TAB, CAPS, KC.F3, KC.T, BACK, KC.Y, KC.RBRACKET, KC.F7, KC.LBRACKET, KC.KP_4, KC.KP_5, KC.KP_6, ___, ___,
        ___, ___, ESC, KC.BSLASH, KC.F4, KC.G, KC.F5, KC.H, KC.F6, ___, KC.QUOTE, ___, KC.KP_0, KC.KP_DOT, KC.UP, ALT,
    ],
]

if __name__ == '__main__':
    keyboard.go()
