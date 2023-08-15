import helpers

keys = [
    127,
    126,
    125,
    124,
    123,
    122,
    121,
    120,  # 8
    119,
    118,
    117,
    116,
    115,
    114,
    113,
    112,
]

knobHandlers = [
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,

    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,

    helpers.ins_del_space,
    helpers.temp,
    helpers.temp,
    helpers.transportTo(90, 2),  # context menu

]

buttonHandlers = [
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,

    helpers.transportTo(33),  # AddMarker
    helpers.transportTo(35),  # MarkerJumpJog
    helpers.transportTo(36),  # MarkerSelJog
    helpers.q_quantize,

    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
]


def handler(e):
    print('playlist')
    if e.status == 176:
        for i, key in enumerate(keys):
            if e.data1 == key and e.status == 176:
                knobHandlers[i](e)
    elif e.status == 128:
        for i, key in enumerate(keys):
            if e.data1 == key and e.status == 128:
                buttonHandlers[i](e)
