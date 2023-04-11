# name=Beat Step Arturia My

import browserMy
import channel_reck
import common
import lists
import mixerMy
import piano_roll
import playlistMy
import plugin_general
import ui

handlers = {
    lists.windows['mixer']: mixerMy.handler,
    lists.windows['channels']: channel_reck.handler,
    lists.windows['playlist']: playlistMy.handler,
    lists.windows['piano roll']: piano_roll.handler,
    lists.windows['browser']: browserMy.handler,
    lists.windows['plugin']: plugin_general.handler,
}


# event.handled = True
def route_to(e):
    print(e.data1, e.data2, e.status)

    if e.status == 176:
        common.handleKnob(e)
        id_focused = ui.getFocusedFormID()
        if id_focused <= 6:
            handlers[id_focused](e)
        else:
            print('else knob', e.data1, e.data2, e.status)

    elif e.status == 128:
        common.handleCommon(e)
        id_focused = ui.getFocusedFormID()
        if id_focused <= 6:
            handlers[id_focused](e)
        else:
            print('else button', e.data1, e.data2, e.status)


def OnMidiMsg(event):
    route_to(event)
