from pico2d import*

open_canvas()

Porygon = load_image('Porygon.png')

frame = 0
Porygon.clip_draw(0, frame*24+ 24*5, 26,24,400,300)
update_canvas()
delay(1)

close_canvas()
