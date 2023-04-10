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


def handler(e):
    if e.data1 == 114 and e.status == 128:
        macros.deleteChannel()
    print('channels')

