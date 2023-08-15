# name=Beat Step Arturia My

import ui

import browserMy
import channel_reck
import common
import lists
import mixerMy
import piano_roll
import playlistMy
import plugin_general

handlers = {
    lists.windows['mixer']: mixerMy.handler,
    lists.windows['channels']: channel_reck.handler,
    lists.windows['playlist']: playlistMy.handler,
    lists.windows['piano roll']: piano_roll.handler,
    lists.windows['browser']: browserMy.handler,
}


# event.handled = True
def route_to(e):
    print(e.data1, e.data2, e.status)
    if e.status == 176:  # knobs
        common.handleKnob(e)
        id_focused = ui.getFocusedFormID()
        id_focused_plugin = ui.getFocused(lists.windows['plugin'])
        if id_focused_plugin == 1:
            plugin_general.handler(e)
        elif id_focused <= 5:
            handlers[id_focused](e)
        else:
            print('else knob', id_focused)

    elif e.status == 128:  # buttons
        common.handleButton(e)
        id_focused = ui.getFocusedFormID()
        id_focused_plugin = ui.getFocused(lists.windows['plugin'])
        if id_focused_plugin == 1:
            plugin_general.handler(e)
        elif id_focused <= 5:
            handlers[id_focused](e)
        else:
            print('else button', id_focused)


def OnMidiMsg(event):
    route_to(event)
