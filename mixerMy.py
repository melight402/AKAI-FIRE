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

    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,

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

    helpers.soloTrack,
    helpers.muteTrack,
    helpers.revPolarTrack,
    helpers.temp,

    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
]


def handler(e):
    print('mixer')
    if e.status == 176:
        for i, key in enumerate(keys):
            if e.data1 == key and e.status == 176:
                knobHandlers[i](e)
    elif e.status == 128:
        for i, key in enumerate(keys):
            if e.data1 == key and e.status == 128:
                buttonHandlers[i](e)
