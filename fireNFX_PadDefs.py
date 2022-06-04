from fireNFX_Colors import *
from fireNFX_Utils import *
from fireNFX_Classes import TnfxMacro
from fireNFX_DEFAULTS import DEFAULT_DIM_BRIGHT, DEFAULT_DIM_FACTOR

# defines the pads when used as a set from 0..63
pdAllPads = [0 for i in range(64)] 

pdBankA = [48, 49, 50, 51,
          32, 33, 34, 35, 
          16, 17, 18, 19,
           0,  1,  2,  3]

pdBankB = [52, 53, 54, 55,
          36, 37, 38, 39,
          20, 21, 22, 23,
           4,  5,  6,  7]

pdBankC = [ 8,  9, 10, 11,
           24, 25, 26, 27,
           40, 41, 42, 43,
           56, 57, 58, 59 ]

pdBankD = [12, 13, 14, 15, 
           28, 29, 30, 31,
           44, 45, 46, 47,
           60, 61, 62, 63 ]

pdPatternStripA = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]      # top row, first 12
pdPatternStripB = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]      # second row, first 12
pdChanStripA    = [ 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]     # third row, first 12
pdChanStripB    = [ 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]     # fourth row, first 12

pdPlaylistStripA = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]      # top row, first 12
pdPlaylistMutesA = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]      # second row, first 12
pdPlaylistStripB = [ 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]     # third row, first 12
pdPlaylistMutesB = [ 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]     # fourth row, first 12

#full size for alt mode
pdPlaylistSelStripA = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]     
pdPlaylistSelMutesA = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
pdMarkers  = [ 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
pdProgress = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63] 

# these are defined in "FPC" order. Bottom Left FPC Pad is first value in index
# so I define them bottom to top order for each set.
pdFPCA = pdBankA
         #   [48, 49, 50, 51,
         # 32, 33, 34, 35, 
         # 16, 17, 18, 19,
         #  0,  1,  2,  3]

pdFPCB = pdBankB 
           # [52, 53, 54, 55,
          #36, 37, 38, 39,
         # 20, 21, 22, 23,
          # 4,  5,  6,  7]

# quick slect FPC channels in drum mode
pdFPCChannels = pdBankC
                # [ 8,  9, 10, 11,
                # 24, 25, 26, 27,
                # 40, 41, 42, 43,
                # 56, 57, 58, 59 ]

pdChordBar =   [ 0, 1, 2,  3,  4,  5,  6 ]

pdChordFuncs     = [ 7,  8, 9, 10, 11 ] 
pd7th       = 7
pdNormal    = 8
pdInv1      = 9
pdInv2      = 10

#pdChordFuncNames = [ "", "Normal", "1st Inv", "2nd Inv", "7th"]                
#colChordFuncs    = [cOff, cOff, cOff, cOff, cYellow ]
           
pdWorkArea = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11,
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
              32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
              48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59 ]

pdMacros = [ 12, 13, 14, 15, 28, 29, 30, 31]
#colMacros = [ cGreen, cCyan, cBlue, cPurple, cRed, cOrange, cYellow, cWhite ]


# thx to "a candle" for the tab idea
pdShiftTab = 44
pdEsc = 45
pdUp = 46
pdEnter = 47
pdTab = 60
pdLeft = 61
pdDown = 62
pdRight = 63
pdUDLR = [pdShiftTab, pdEsc, pdUp, pdEnter, pdTab, pdLeft, pdDown, pdRight]

# for modes that need channel specific window control - ie Note mode, FPC, etc
pdShowChanEditor = 44
pdShowChanPianoRoll = 60
pdShowChanPads = [pdShowChanEditor, pdShowChanPianoRoll]
colShowChanPads = [cWhite, cWhite]

dimDim = 4
dimDefault = DEFAULT_DIM_FACTOR
dimBright = DEFAULT_DIM_BRIGHT
dimFull = 0

#navigation
pdNav = [ 44, 45, 46, 47,
          60, 61, 62, 63]

pdVelocityUp = 44
pdVelocityDown = 60
pdVelocityNav = [pdVelocityUp, pdVelocityDown]
colPresetNav  = [cWhite, cDimWhite]

#nav for PATTERNS and DRUMS
pdPresetPrev = 47
pdPresetNext = 63
pdPresetNav = [pdPresetPrev, pdPresetNext]
colPresetNav = [cWhite, cDimWhite]

pdNoteRepeat = 46
colNoteRepeat = cOrange
pdNoteRepeatLength = 62
colNoteRepeatLength = getShade(cOrange, shLight)


pdSnapUp = 45
pdSnapDown = 61
pdSnapNav = [pdSnapUp, pdSnapDown]
colSnapUp = getShade(cYellow, shNorm)
colSnapDown = getShade(cYellow, shDark)

#nav for NOTES
pdRootNotePrev = 45
pdRootNoteNext = 61
pdOctavePrev = 46
pdOctaveNext = 62
pdScalePrev = 47
pdScaleNext = 63
pdNoteFuncs = [pdScalePrev, pdScaleNext, pdRootNotePrev, pdRootNoteNext, pdOctavePrev, pdOctaveNext]
colNoteFuncs = [getShade(cGreen, shLight), cGreen, getShade(cPurple, shLight), cPurple, 
    getShade(cBlue, shLight), cBlue]




