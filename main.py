import utime
import urandom
import picodisplay as display

buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
display.set_backlight(0.8)
display.set_pen(255, 255, 0)
display.clear()
display.set_pen(0, 0, 0)
display.text("Get Ready!", 10, 10, 240, 5)
display.update()

player1_score = 0
player2_score = 0





for i in range(11):
    utime.sleep(urandom.randint(3, 8))
    display.set_led(255, 136, 79)
    display.set_pen(255, 136, 79)
    display.clear()
    display.set_pen(0, 0, 0)
    display.text("Begin!", 10, 10, 240, 5)
    display.update()
    while True:
         if display.is_pressed(display.BUTTON_Y):
             display.set_led(0, 0, 0)
             display.set_pen(250, 228, 63)
             display.clear()
             display.update()
             display.set_pen(0, 0, 0)
             display.text("Player 2 wins!", 10, 10, 240, 5)
             player2_score += 1
             display.update()
             break
         elif display.is_pressed(display.BUTTON_A):
             display.set_led(0, 0, 0)
             display.set_pen(250, 228, 63)
             display.clear()
             display.update()
             display.set_pen(0, 0, 0)
             display.text("Player 1 wins!", 10, 10, 240, 5)
             player1_score += 1
             display.update()
             break
if player1_score > player2_score: 
    display.set_pen(255, 255, 2)
    display.clear()
    display.set_pen(0, 0, 0)
    display.text("Player 1 wins!", 10, 10, 240, 5)
elif player2_score > player1_score:
    display.set_pen(255, 255, 0)
    display.clear()
    display.set_pen(0, 0, 0)
    display.text("Player 2 wins!", 10, 10, 240, 5)
utime.sleep(1)

display.set_pen(255, 255, 0)
display.clear()
display.set_pen(0, 0, 0)
display.text(str(player1_score), 30, 40, 4, 6)
display.text(str(player2_score), 170, 40, 4, 6)


display.update()


