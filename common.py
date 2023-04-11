import general
import helpers
import macros
import transport
import ui

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
    helpers.transportTo(80),  # enter/accept
    helpers.open_plugin,
    helpers.transportTo(33),
    helpers.transportTo(35),
    helpers.transportTo(36),
    helpers.transportTo(61),
    helpers.temp,  # REWIND
    helpers.temp,  # 8 FORWARD
    helpers.back_close,
    macros.ShowScriptOutputWindow,
    helpers.q_quantize,
    helpers.transportTo(51),  # Copy
    helpers.transportTo(52),  # Paste
    helpers.transportTo(50),  # Cut
    helpers.event_wrap(general.undo),
    helpers.closeAll,
]

knobHandlers = [
    helpers.windows_switch,
    helpers.handle_knob_as_toggle(helpers.rec_toggle, transport.isRecording),
    helpers.transportTo(90, 2),  # context menu
    helpers.handle_knob_as_toggle(transport.setLoopMode, transport.getLoopMode),
    helpers.handle_knob_as_toggle(helpers.metronome_toggle, ui.isMetronomeEnabled),
    helpers.handle_knob_as_toggle(helpers.count_toggle, ui.isPrecountEnabled),
    helpers.handle_knob_args(nt, nt, 43, 42),  # browser tabs ---- 8
    helpers.handle_knob(helpers.prev_pattern, helpers.next_pattern),
    helpers.transpose_octave,
    helpers.transpose_tone,
    helpers.handle_knob(macros.quick_legato, macros.quick_staccato, [3]),
    helpers.handle_knob(macros.select_all, macros.invert_selection, [3]),
    helpers.ins_del_space,
    helpers.playlist_movement,
    helpers.tempo_scroll,
    helpers.snap_scroll,
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


def handleCommon(e):
    for i, key in enumerate(commonKeys):
        if e.data1 == key and e.status == 128:
            buttonHandlers[i](e)

# event.handled = True
