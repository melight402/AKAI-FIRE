import channels
import ui
import transport

import helpers


def TransposeOctaveUp(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDDE')
    e.handled = True


def TransposeOctaveDown(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDDDE')
    e.handled = True


def TransposeToneUp(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDE')
    e.handled = True


def TransposeToneDown(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDE')
    e.handled = True


def ShowScriptOutputWindow(e):
    ui.showWindow(1)  # make CR the active window, so it pulls up the main menu
    helpers.NavigateFLMenu(',LLLLDDDDDDDDDDE')  # series of keys to pass
    e.handled = True


def Articulate(e):
    helpers.NavigateFLMenu(',R,DR,DDDE,')
    e.handled = True


def insertSpacePlaylist(e):
    helpers.NavigateFLMenu(',D,R,U,R,DDDDDDDDDDDDDDDDE')
    e.handled = True


def deleteSpacePlaylist(e):
    helpers.NavigateFLMenu(',D,R,U,R,DDDDDDDDDDDDDDDDDE')
    e.handled = True


def insertSpacePianoRoll(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDDDDDDDDDDE')
    e.handled = True


def deleteSpacePianoRoll(e):
    helpers.NavigateFLMenu(',RR,DDDDDDDDDDDDDDDDDDDDE')
    e.handled = True


def quick_legato(e):
    ui.showWindow(3)
    helpers.NavigateFLMenu(',R,D,R,DDE')
    e.handled = True


def quick_staccato(e):
    ui.showWindow(3)
    helpers.NavigateFLMenu(',R,R,DDDDDDDDDDDDDE')
    e.handled = True


def select_all(e):
    helpers.NavigateFLMenu(',R,D,D,D,D,D,R,DE')
    e.handled = True


def invert_selection(e):
    helpers.NavigateFLMenu(',R,D,D,D,D,D,R,DDDDDDDDDE')
    e.handled = True
