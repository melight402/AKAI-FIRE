import general
import transport
import ui

import helpers
import macros

nt = ui.navigateBrowserTabs

commonKeys = [
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

buttonHandlers = [
    # block 1
    helpers.transportTo(80),  # enter/accept
    helpers.back_close,
    macros.ShowScriptOutputWindow,
    helpers.transportTo(50),  # Cut

    # block 2
    helpers.transportTo(51),  # Copy
    helpers.transportTo(52),  # Paste
    helpers.temp,
    helpers.temp,


    # block 3
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,

    # block 4
    helpers.transportTo(63),
    helpers.transportTo(61),
    helpers.event_wrap(general.undo),
    helpers.closeAll,


]

knobHandlers = [
    # block 1
    helpers.windows_switch,
    helpers.handle_knob(helpers.prev_pattern, helpers.next_pattern),
    helpers.snap_scroll,
    helpers.tempo_scroll,
    # block 2
    helpers.handle_knob_as_toggle(helpers.rec_toggle, transport.isRecording),
    helpers.handle_knob_as_toggle(transport.setLoopMode, transport.getLoopMode),
    helpers.handle_knob_as_toggle(helpers.metronome_toggle, ui.isMetronomeEnabled),
    helpers.handle_knob_as_toggle(helpers.count_toggle, ui.isPrecountEnabled),
    # block 3
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,
    # block 4
    helpers.temp,
    helpers.temp,
    helpers.temp,
    helpers.temp,

]


def handleKnob(e):
    id_focused = ui.getFocusedFormID()

    if e.data1 == 0:
        if id_focused == 4:
            helpers.handle_knob_no_event(ui.down, ui.up)(e)
        else:
            helpers.handle_knob_no_event(ui.next, ui.previous)(e)

    for i, key in enumerate(commonKeys):
        if e.data1 == key and e.status == 176:
            knobHandlers[i](e)


def handleButton(e):
    for i, key in enumerate(commonKeys):
        if e.data1 == key and e.status == 128:
            buttonHandlers[i](e)

# event.handled = True
