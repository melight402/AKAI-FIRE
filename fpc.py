import helpers

keys = [
    37,
    36,
    42,
    54,

    40,
    38,
    46,
    44,

    48,
    47,
    45,
    43,

    49,
    55,
    51,
    53
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
    print('FPC')
    if e.status == 176:
        for i, key in enumerate(keys):
            if e.data1 == key and e.status == 176:
                knobHandlers[i](e)
    elif e.status == 128:
        for i, key in enumerate(keys):
            if e.data1 == key and e.status == 128:
                buttonHandlers[i](e)