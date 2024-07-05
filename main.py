from microbit import *
import music


SHAKE_THRESHOLD = 2000

while True:

    # もしaが押されたら
    if button_a.is_pressed():
            display.scroll(temperature())
            print('temperature()')

    # もしbが押されたら
    if button_b.is_pressed():

        # 必要
        acceleration = accelerometer.get_values()
        total_acceleration = abs(acceleration[0]) + abs(acceleration[1]) + abs(acceleration[2])
        # 必要

        # もし振られたら
        if total_acceleration > SHAKE_THRESHOLD:
            while True:
                for i in range(1,10):
                    print('Blue')
                    display.scroll('Blue')
                    music.play(music.POWER_DOWN)
                for n in range(1,3):
                    print('Yellow')
                    display.scroll('Yellow')

                music.play(music.POWER_UP)
                print('Red')
                for i in range(1,10):
                    print('Red')
                    display.scroll('Red')
                    music.play(music.POWER_UP)
            
                for n in range(1,10):
                    print('Yellow')
                    display.scroll('Yellow')
