input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    if (current_play == 0) {
        basic.showIcon(IconNames.Yes)
    }
    if (current_play == 1) {
        basic.showIcon(IconNames.Sad)
    }
    if (current_play == 2) {
        basic.showIcon(IconNames.No)
    }
    serial.writeString("paper")
    serial.writeLine("")
    bot_play = serial.readUntil(serial.delimiters(Delimiters.NewLine))
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . . . . #
        # . # # .
        . # . . .
        # . # # .
        . . . . #
        `)
    if (current_play == 0) {
        basic.showIcon(IconNames.No)
    }
    if (current_play == 1) {
        basic.showIcon(IconNames.Yes)
    }
    if (current_play == 2) {
        basic.showIcon(IconNames.Sad)
    }
    serial.writeString("scissors")
    serial.writeLine("")
    bot_play = serial.readUntil(serial.delimiters(Delimiters.NewLine))
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        `)
    if (current_play == 0) {
        basic.showIcon(IconNames.Sad)
    }
    if (current_play == 1) {
        basic.showIcon(IconNames.No)
    }
    if (current_play == 2) {
        basic.showIcon(IconNames.Yes)
    }
    serial.writeString("rock")
    serial.writeLine("")
    bot_play = serial.readUntil(serial.delimiters(Delimiters.NewLine))
})
input.onGesture(Gesture.ThreeG, function () {
    basic.showIcon(IconNames.Heart)
    bot_play = serial.readUntil(serial.delimiters(Delimiters.NewLine))
})
let bot_play = ""
let current_play = 0
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
serial.redirectToUSB()
basic.showIcon(IconNames.Happy)
basic.pause(1000)
