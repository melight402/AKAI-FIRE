import time

import channels
import mixer
import patterns
import playlist
import transport
import ui

import lists
import macros


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
    e.handled = True


def event_wrap(func):
    def callback(e):
        func()
        e.handled = True

    return callback


def handle_knob_args(first, second, arg1, arg2):
    def callback(e):
        if e.data2 >= 64:
            first(arg1)
            e.handled = True
        else:
            second(arg2)
            e.handled = True

    return callback


def handle_knob(first, second, windows=None):
    def callback(e):
        focused_id = ui.getFocusedFormID()
        if windows is None or not windows.index(focused_id) == -1:
            if e.data2 >= 64:
                first(e)
                e.handled = True
            else:
                second(e)
                e.handled = True

    return callback


def handle_knob_no_event(first, second, windows=None):
    def callback(e):
        focused_id = ui.getFocusedFormID()
        if windows is None or not windows.index(focused_id) == -1:
            if e.data2 >= 64:
                first()
                e.handled = True
            else:
                second()
                e.handled = True

    return callback


def transportTo(key, num=1):
    def callback(e):
        transport.globalTransport(key, num)
        e.handled = True

    return callback


def handle_knob_as_toggle(toggle, condition):
    def callback(e):
        cond = condition()
        if e.data2 >= 64 and not cond:
            toggle()
            e.handled = True
        elif e.data2 <= 64 and cond:
            toggle()
            e.handled = True

    return callback


def rec_toggle():
    transport.globalTransport(12, 2)


snaps = [14, 13, 12, 10, 9, 8, 7, 5, 4,  3]


def snap_scroll(e):
    current = ui.getSnapMode()
    curr_index = snaps.index(current)
    if e.data2 >= 64:
        if curr_index < 9:
            ui.setSnapMode(snaps[curr_index + 1])
            e.handled = True
    else:
        if curr_index > 0:
            ui.setSnapMode(snaps[curr_index - 1])
            e.handled = True


def count_toggle():
    transport.globalTransport(115, 2)


def metronome_toggle():
    transport.globalTransport(110, 1)


def tempo_scroll(e):
    if e.data2 >= 64:
        transport.globalTransport(105, 10)
        e.handled = True
    else:
        transport.globalTransport(105, -10)
        e.handled = True


def next_pattern(e):
    current = patterns.patternNumber()
    if current < 40:
        patterns.jumpToPattern(current + 1)
        e.handled = True


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
    e.handled = True


def transpose_octave(e):
    ui.showWindow(3)
    if e.data2 >= 64:
        macros.TransposeOctaveUp(e)
    else:
        macros.TransposeOctaveDown(e)
    e.handled = True


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
    e.handled = True


def transpose_tone(e):
    ui.showWindow(3)
    if e.data2 >= 64:
        macros.TransposeToneUp(e)
    else:
        macros.TransposeToneDown(e)
    e.handled = True


def back_close(e):
    focused_id = ui.getFocusedFormID()
    id_focused_plugin = ui.getFocused(lists.windows['plugin'])
    if ui.isInPopupMenu():
        ui.closeActivePopupMenu()
    elif id_focused_plugin == 1:
        transport.globalTransport(81, 81)
    elif focused_id == 4:
        ui.left()
    else:
        transport.globalTransport(81, 81)
    e.handled = True


def windows_switch(e):
    windowNumber = ui.getFocusedFormID()
    id_focused_plugin = ui.getFocused(lists.windows['plugin'])

    print("wind", id_focused_plugin)
    if e.data2 <= 64:
        if id_focused_plugin == 1:
            transport.globalTransport(81, 81)
            ui.showWindow(2)
        elif windowNumber == 3:
            channels.showCSForm(channels.channelNumber(), 1)
            e.handled = True
            return
        elif windowNumber == 2:
            ui.showWindow(4)
            e.handled = True
            return
        else:
            ui.showWindow(4)
            e.handled = True
            return

    elif e.data2 >= 64:
        if id_focused_plugin == 1:
            transport.globalTransport(81, 81)
            ui.hideWindow(2)
            ui.showWindow(3)
            e.handled = True
            return
        if windowNumber == 4:
            ui.hideWindow(4)
            ui.showWindow(2)
            e.handled = True
            return
        elif windowNumber == 2:
            channels.showCSForm(channels.channelNumber(), 1)
            e.handled = True
            return
        else:
            ui.hideWindow(2)
            ui.showWindow(3)
            e.handled = True
            return


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
    e.handled = True


def prev_pattern(e):
    current = patterns.patternNumber()
    if current > 1:
        patterns.jumpToPattern(current - 1)
    e.handled = True


def openBrowser(e):
    id_focused = ui.getFocusedFormID()
    if id_focused == 4:
        ui.escape()
    else:
        ui.showWindow(4)
        ui.setFocused(4)
    e.handled = True


def closeAll(e):
    if ui.isInPopupMenu():
        ui.closeActivePopupMenu()
    transport.globalTransport(lists.f_keys['F12'], 1)
    e.handled = True


def checkIfBrowser(func_browser, func_not):
    id_focused = ui.getFocusedFormID()
    if id_focused == 4:
        return func_browser
    else:
        return func_not


def q_quantize(e):
    channels.quickQuantize(channels.channelNumber(), 0)
    e.handled = True


def soloTrack(e):
    mixer.soloTrack(mixer.trackNumber())
    e.handled = True


def muteTrack(e):
    mixer.muteTrack(mixer.trackNumber())
    e.handled = True


def revPolarTrack(e):
    mixer.revTrackPolarity(mixer.trackNumber())
    e.handled = True


def soloChannel(e):
    channels.soloChannel(channels.selectedChannel())
    e.handled = True


def muteChannel(e):
    channels.muteChannel(channels.selectedChannel())
    e.handled = True
