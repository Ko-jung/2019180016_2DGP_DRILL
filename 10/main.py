import pico2d
import play_state
import logo_state

pico2d.open_canvas()
states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()
pico2d.close_canvas()



# state = logo_state
# pico2d.open_canvas()
# state.enter()
# # game main loop code
# while state.running:
#     state.handle_events()
#     state.update()
#     state.draw()
#     pico2d.delay(0.05)
#
# state = play_state
# state.enter()
# while state.running:
#     state.handle_events()
#     state.update()
#     state.draw()
#     pico2d.delay(0.05)
# state.exit()
#
# # finalization code
# pico2d.close_canvas()