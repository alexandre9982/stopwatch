let start = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    start = input.runningTime()
})
start = 0
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    let elapesed = input.runningTime() - start
    basic.showNumber(Math.idiv(elapesed, 1000))
})
