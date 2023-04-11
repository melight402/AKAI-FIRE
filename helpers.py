import time

import channels
import lists
import macros
import patterns
import transport
import ui


def menuPause(seconds=0):
    time.sleep(seconds)


def ProcessKeys(cmd_str):
    commands = {'U': ui.up, 'D': ui.down, 'L': ui.left, 'R': ui.right,
                'E': ui.enter, 'S': ui.escape, 'N': ui.next, ',': menuPause}
    for cmd in cmd_str:
        commands.get(cmd.upper(), menuPause)()


def NavigateFLMenu(cmd_string='', alt_menu=False):
    if ui.isInPopupMenu():
        ui.closeActivePopupMenu()
    # open the File menu
    if alt_menu:
        transport.globalTransport(91, 1)
    else:
        transport.globalTransport(90, 1)
        if ui.getFocused(3) == 1:  # auto move to the tools when the PR is active.
            ProcessKeys('LL')
    if len(cmd_string) > 0:
        ProcessKeys(cmd_string)


def temp(e):
    print('temp', e)


def event_wrap(func):
    def callback(e):
        return func()

    return callback


def handle_knob_args(first, second, arg1, arg2):
    def callback(e):
        if e.data2 >= 64:
            first(arg1)
        else:
            second(arg2)

    return callback


def handle_knob(first, second, windows=None):
    def callback(e):
        focused_id = ui.getFocusedFormID()
        if windows is None or not windows.index(focused_id) == -1:
            if e.data2 >= 64:
                first(e)
            else:
                second(e)

    return callback


def handle_knob_no_event(first, second, windows=None):
    def callback(e):
        focused_id = ui.getFocusedFormID()
        if windows is None or not windows.index(focused_id) == -1:
            if e.data2 >= 64:
                first()
            else:
                second()

    return callback


def transportTo(key, num=1):
    def callback(e):
        transport.globalTransport(key, num)

    return callback


def handle_knob_as_toggle(toggle, condition):
    def callback(e):
        cond = condition()
        if e.data2 >= 64 and not cond:
            toggle()
        elif e.data2 <= 64 and cond:
            toggle()

    return callback


def rec_toggle():
    transport.globalTransport(12, 2)


snaps = [14, 13, 9, 8, 5, 3, 1]


def snap_scroll(e):
    current = ui.getSnapMode()
    curr_index = snaps.index(current)
    print('current', current)
    print('index', curr_index)
    print('next step', snaps[curr_index + 1])
    if e.data2 >= 64:
        if curr_index < 5:
            ui.setSnapMode(snaps[curr_index + 1])
    else:
        if curr_index > 0:
            ui.setSnapMode(snaps[curr_index - 1])


def count_toggle():
    transport.globalTransport(115, 2)


def metronome_toggle():
    transport.globalTransport(110, 1)


def tempo_scroll(e):
    if e.data2 >= 64:
        transport.globalTransport(105, 10)
    else:
        transport.globalTransport(105, -10)


def next_pattern(e):
    current = patterns.patternNumber()
    if current < 40:
        patterns.jumpToPattern(current + 1)


def ins_del_space(e):
    focused_id = ui.getFocusedFormID()
    if e.data2 >= 64:
        if focused_id == 2:
            macros.insertSpacePlaylist(e)
        elif focused_id == 3:
            macros.insertSpacePianoRoll(e)
    elif e.data2 < 64:
        if focused_id == 2:
            macros.deleteSpacePlaylist(e)
        elif focused_id == 3:
            macros.deleteSpacePianoRoll(e)


def transpose_octave(e):
    focused_id = ui.getFocusedFormID()
    if focused_id == 3:
        if e.data2 >= 64:
            macros.TransposeOctaveUp(e)
        else:
            macros.TransposeOctaveDown(e)


channels_first = True


def open_plugin(e):
    global channels_first
    ui.hideWindow(4)
    focused_id = ui.getFocusedFormID()
    if focused_id == 1:
        channels_first = False
        channels.showCSForm(channels.channelNumber(), 1)
    elif not focused_id == 3:
        if channels_first:
            channels_first = False
            ui.showWindow(1)
        else:
            channels_first = True
            channels.showCSForm(channels.channelNumber(), 0)
            ui.showWindow(3)
    else:
        channels_first = True
        channels.showCSForm(channels.channelNumber(), 0)
        ui.showWindow(0)
        ui.showWindow(1)


def transpose_tone(e):
    focused_id = ui.getFocusedFormID()
    if focused_id == 3:
        if e.data2 >= 64:
            macros.TransposeToneUp(e)
        else:
            macros.TransposeToneDown(e)


def back_close(e):
    focused_id = ui.getFocusedFormID()
    if ui.isInPopupMenu():
        ui.closeActivePopupMenu()
    elif focused_id == 4:
        ui.left()
    else:
        transport.globalTransport(81, 81)


def windows_switch(e):
    focused_id = ui.getFocusedFormID()
    if e.data2 >= 64:
        if not focused_id == 4:
            ui.showWindow(4)
        else:
            return
    elif e.data2 <= 64 and not focused_id == 2:
        ui.hideWindow(4)
        ui.showWindow(2)


def playlist_movement(e):
    step = 0.1
    if e.data2 >= 64:
        transport.fastForward(2)
        time.sleep(step)
        transport.fastForward(0)
    elif e.data2 <= 64:
        transport.rewind(2)
        time.sleep(step)
        transport.rewind(0)


def prev_pattern(e):
    current = patterns.patternNumber()
    if current > 1:
        patterns.jumpToPattern(current - 1)


def openBrowser(e):
    id_focused = ui.getFocusedFormID()
    if id_focused == 4:
        ui.escape()
    else:
        ui.showWindow(4)
        ui.setFocused(4)


def closeAll(e):
    if ui.isInPopupMenu():
        ui.closeActivePopupMenu()
    transport.globalTransport(lists.f_keys['F12'], 1)


def checkIfBrowser(func_browser, func_not):
    id_focused = ui.getFocusedFormID()
    if id_focused == 4:
        return func_browser
    else:
        return func_not


def q_quantize(e):
    channels.quickQuantize(channels.channelNumber(), 0)
