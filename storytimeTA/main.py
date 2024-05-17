# Copyright © 2024 H. Ryott Glayzer <h.ryott.glayzer@ryott.gay>
#
# STORYTIME TEXT ADVENTURE RPG
# -----------------------------------------------------------------------------
# This will be used both as a standalone game and to aid in development of
# Storytime Rogue-Like RPG.
#
#
#


###############################################################################
#   IMPORT STATEMENTS
###############################################################################
import os


###############################################################################
#   Functions
###############################################################################


def pregameSetup():
    termCols, termRows = os.get_terminal_size()
    print(f'Terminal Dimensions (rows x columns): {termRows} x {termCols}. ')
    return 0

pregameSetup()
