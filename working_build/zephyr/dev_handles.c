#include <device.h>
#include <toolchain.h>

/* 1 : /soc/rcc@40023800:
 * Direct Dependencies:
 *   - (/soc)
 *   - (/clocks/pll)
 * Supported:
 *   - (/soc/adc@40012000)
 *   - (/soc/dma@40026000)
 *   - (/soc/dma@40026400)
 *   - (/soc/i2c@40005400)
 *   - (/soc/i2c@40005800)
 *   - (/soc/i2c@40005c00)
 *   - (/soc/i2s@40003800)
 *   - (/soc/i2s@40003c00)
 *   - (/soc/rtc@40002800)
 *   - /soc/serial@40004400
 *   - /soc/serial@40011000
 *   - (/soc/serial@40011400)
 *   - (/soc/spi@40003800)
 *   - (/soc/spi@40003c00)
 *   - (/soc/spi@40013000)
 *   - (/soc/spi@40013400)
 *   - (/soc/timers@40000000)
 *   - (/soc/timers@40000400)
 *   - (/soc/timers@40000800)
 *   - (/soc/timers@40000c00)
 *   - (/soc/timers@40010000)
 *   - (/soc/timers@40014000)
 *   - (/soc/timers@40014400)
 *   - (/soc/timers@40014800)
 *   - (/soc/usb@50000000)
 *   - (/soc/watchdog@40002c00)
 *   - /soc/pin-controller@40020000/gpio@40020000
 *   - /soc/pin-controller@40020000/gpio@40020400
 *   - /soc/pin-controller@40020000/gpio@40020800
 *   - /soc/pin-controller@40020000/gpio@40020c00
 *   - /soc/pin-controller@40020000/gpio@40021000
 *   - /soc/pin-controller@40020000/gpio@40021400
 *   - /soc/pin-controller@40020000/gpio@40021800
 *   - /soc/pin-controller@40020000/gpio@40021c00
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_rcc_40023800[] = { DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, 12, 7, 2, 8, 3, 9, 4, 11, 5, 6, DEVICE_HANDLE_ENDS };

/* 2 : /soc/pin-controller@40020000/gpio@40021c00:
 * Direct Dependencies:
 *   - (/soc/pin-controller@40020000)
 *   - /soc/rcc@40023800
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_pin_controller_40020000_S_gpio_40021c00[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 3 : /soc/pin-controller@40020000/gpio@40021800:
 * Direct Dependencies:
 *   - (/soc/pin-controller@40020000)
 *   - /soc/rcc@40023800
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_pin_controller_40020000_S_gpio_40021800[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 4 : /soc/pin-controller@40020000/gpio@40021400:
 * Direct Dependencies:
 *   - (/soc/pin-controller@40020000)
 *   - /soc/rcc@40023800
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_pin_controller_40020000_S_gpio_40021400[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 5 : /soc/pin-controller@40020000/gpio@40021000:
 * Direct Dependencies:
 *   - (/soc/pin-controller@40020000)
 *   - /soc/rcc@40023800
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_pin_controller_40020000_S_gpio_40021000[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 6 : /soc/pin-controller@40020000/gpio@40020c00:
 * Direct Dependencies:
 *   - (/soc/pin-controller@40020000)
 *   - /soc/rcc@40023800
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_pin_controller_40020000_S_gpio_40020c00[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 7 : /soc/pin-controller@40020000/gpio@40020800:
 * Direct Dependencies:
 *   - (/soc/pin-controller@40020000)
 *   - /soc/rcc@40023800
 * Supported:
 *   - (/gpio_keys/button)
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_pin_controller_40020000_S_gpio_40020800[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 8 : /soc/pin-controller@40020000/gpio@40020400:
 * Direct Dependencies:
 *   - (/soc/pin-controller@40020000)
 *   - /soc/rcc@40023800
 * Supported:
 *   - (/soc/spi@40013000)
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_pin_controller_40020000_S_gpio_40020400[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 9 : /soc/pin-controller@40020000/gpio@40020000:
 * Direct Dependencies:
 *   - (/soc/pin-controller@40020000)
 *   - /soc/rcc@40023800
 * Supported:
 *   - (/leds/led_2)
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_pin_controller_40020000_S_gpio_40020000[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 10 : /soc/interrupt-controller@40013c00:
 * Direct Dependencies:
 *   - (/soc)
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_interrupt_controller_40013c00[] = { DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 11 : /soc/serial@40004400:
 * Direct Dependencies:
 *   - (/soc)
 *   - (/soc/interrupt-controller@e000e100)
 *   - /soc/rcc@40023800
 *   - (/soc/pin-controller@40020000/usart2_rx_pa3)
 *   - (/soc/pin-controller@40020000/usart2_tx_pa2)
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_serial_40004400[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };

/* 12 : /soc/serial@40011000:
 * Direct Dependencies:
 *   - (/soc)
 *   - (/soc/interrupt-controller@e000e100)
 *   - /soc/rcc@40023800
 *   - (/soc/pin-controller@40020000/usart1_rx_pb7)
 *   - (/soc/pin-controller@40020000/usart1_tx_pb6)
 */
const device_handle_t __aligned(2) __attribute__((__section__(".__device_handles_pass2")))
__devicehdl_DT_N_S_soc_S_serial_40011000[] = { 1, DEVICE_HANDLE_SEP, DEVICE_HANDLE_SEP, DEVICE_HANDLE_ENDS };
