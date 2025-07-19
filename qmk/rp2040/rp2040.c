/* Copyright 2019 iw0rm3r
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include "quantum.h"
#include "config.h"

#define MATRIX_HAS_GHOST

void led_init_ports(void) {
  /* Setting status LEDs pins to output and +5V (off) */
  gpio_set_pin_output(GP27);
  gpio_set_pin_output(GP28);
  gpio_write_pin_high(GP27);
  gpio_write_pin_high(GP28);
}

// Global timeout threshold in milliseconds
#define GHOST_TIMEOUT 1
uint16_t last_keypress_time = 0;

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (record->event.pressed) {
        // Check if this key was pressed too soon after the last one
        if (timer_elapsed(last_keypress_time) <= GHOST_TIMEOUT) {
            return false; // Block likely phantom key
        }

        // Update timer for this keypress
        last_keypress_time = timer_read();
    }
    return true; // Allow key
}
