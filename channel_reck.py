import helpers
import macros

keys = [
    111,
    110,
    109,
    108,

    107,
    106,
    105,
    104,

    103,
    102,
    101,
    100,

    99,
    98,
    97,
    96
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
    macros.deleteChannel,
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


def handler(e):
    print('channels')
    if e.status == 176:
        for i, key in enumerate(keys):
            if e.data1 == key and e.status == 176:
                knobHandlers[i](e)
    elif e.status == 128:
        for i, key in enumerate(keys):
            if e.data1 == key and e.status == 128:
                buttonHandlers[i](e)
