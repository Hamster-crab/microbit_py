from microbit import *
import music
import random
import time


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


            # ランダムにするために必要開始
            test = random.randrange(1, 2)
            # ランダムにするために必要終了

            # 青信号
            if test > 1:
                music.play(music.POWER_DOWN)
                print('Blue')
                for i in range(1,30):
                    display.scroll('Blue')
                    music.play(music.POWER_DOWN)
                    print('Yellow')
                
                for n in range(1,10):
                    display.scroll('Yellow')


                music.play(music.POWER_UP)
                print('Red')
                for i in range(1,30):
                    display.scroll('Red')
                    music.play(music.POWER_UP)
            
                for n in range(1,10):
                    display.scroll('Yellow')

        
            # 赤信号
            else:
                music.play(music.POWER_UP)
                print('Red')
                for i in range(1,30):
                    display.scroll('Red')
                    music.play(music.POWER_UP)
            
                for n in range(1,10):
                    display.scroll('Yellow')

                music.play(music.POWER_DOWN)
                print('Blue')
                for i in range(1,30):
                    display.scroll('Blue')
                    music.play(music.POWER_DOWN)

                for n in range(1,10):
                    display.scroll('Yellow')
            
