start = 0

def on_button_pressed_a():
    global start
    start = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)
start = 0
def on_button_pressed_b():
    elapesed = input.running_time() - start
    basic.show_number(Math.idiv(elapesed, 1000))
input.on_button_pressed(Button.B, on_button_pressed_b)