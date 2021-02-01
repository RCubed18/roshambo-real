def on_button_pressed_a():
    global bot_play
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        # # # # .
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        # # # . .
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        # # . . .
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        # . . . .
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . #
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . #
        . # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . #
        . . # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . #
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . #
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    if current_play == 0:
        basic.show_icon(IconNames.YES)
    if current_play == 1:
        basic.show_icon(IconNames.SAD)
    if current_play == 2:
        basic.show_icon(IconNames.NO)
    serial.write_string("paper")
    serial.write_line("")
    bot_play = serial.read_until(serial.delimiters(Delimiters.NEW_LINE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global bot_play
    basic.show_leds("""
        . . . . #
        # . # # .
        . # . . .
        # . # # .
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        # . . # #
        . # # . .
        # . . # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # . . . .
        # # # # #
        # . . . .
        . . . . .
        """)
    if current_play == 0:
        basic.show_icon(IconNames.NO)
    if current_play == 1:
        basic.show_icon(IconNames.YES)
    if current_play == 2:
        basic.show_icon(IconNames.SAD)
    serial.write_string("scissors")
    serial.write_line("")
    bot_play = serial.read_until(serial.delimiters(Delimiters.NEW_LINE))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global bot_play
    basic.show_leds("""
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    if current_play == 0:
        basic.show_icon(IconNames.SAD)
    if current_play == 1:
        basic.show_icon(IconNames.NO)
    if current_play == 2:
        basic.show_icon(IconNames.YES)
    serial.write_string("rock")
    serial.write_line("")
    bot_play = serial.read_until(serial.delimiters(Delimiters.NEW_LINE))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_three_g():
    global bot_play
    basic.show_icon(IconNames.HEART)
    bot_play = serial.read_until(serial.delimiters(Delimiters.NEW_LINE))
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

bot_play = ""
current_play = 0
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
serial.redirect_to_usb()
basic.show_icon(IconNames.HAPPY)
basic.pause(1000)