import channels
import ui

import helpers


def TransposeOctaveUp(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDDE')


def TransposeOctaveDown(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDDDE')


def TransposeToneUp(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDE')


def TransposeToneDown(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDE')


def QuickQuantize():
    channels.quickQuantize(channels.channelNumber())


def ShowScriptOutputWindow(e):
    print('script')
    ui.showWindow(1)  # make CR the active window, so it pulls up the main menu
    helpers.NavigateFLMenu(',LLLLDDDDDDDDDDE')  # series of keys to pass


def ShowProject():
    ui.showWindow(1)  # make CR the active window, so it pulls up the main menu
    helpers.NavigateFLMenu(',LLL,LUUUUUELL')  # series of keys to pass


def ViewArrangeIntoWorkSpace():
    ui.showWindow(1)  # make CR the active window, so it pulls up the main menu
    helpers.NavigateFLMenu(',LLLLDDDDDDDDDDDDDDDDDDRDE')  # series of keys to pass


def Articulate():
    helpers.NavigateFLMenu(',R,DR,DDDE,')


def deleteChannel():
    if ui.isInPopupMenu():
        ui.closeActivePopupMenu()

    ui.showWindow(1)
    channels.showCSForm(1)
    # helpers.NavigateFLMenu(',DDE')


def insertSpacePlaylist(e):
    helpers.NavigateFLMenu(',D,R,U,R,DDDDDDDDDDDDDDDDE')


def deleteSpacePlaylist(e):
    helpers.NavigateFLMenu(',D,R,U,R,DDDDDDDDDDDDDDDDDE')


def insertSpacePianoRoll(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDDDDDDDDDDE')


def deleteSpacePianoRoll(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDDDDDDDDDDDE')


def quick_legato(e):
    helpers.NavigateFLMenu(',R,D,R,DDE')


def quick_staccato(e):
    helpers.NavigateFLMenu(',R,R,DDDDDDDDDDDDDE')


def select_all(e):
    helpers.NavigateFLMenu(',R,D,D,D,D,D,R,DE')


def invert_selection(e):
    helpers.NavigateFLMenu(',R,D,D,D,D,D,R,DDDDDDDDDE')
