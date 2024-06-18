#!/home/ryott/.local/share/virtualenvs/storytime-G_79txi2 python
"""A Rogue-like game in Python"""
from __future__ import annotations
import attrs
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset
import g
import game.states
import game.world_tools


# @attrs.define(eq=False)
# class ExampleState:
#     """Example State with a hard-coded player position."""
#     player_x: int
#     """Player X position, left-most position is zero"""
#     player_y: int
#     """Player Y position, top-most position is zero"""
# 
#     def on_draw(self, console: tcod.console.Console) -> None:
#         """Draw the player glyph"""
#         console.print(self.player_x, self.player_y, "@")
# 
# 
#     def on_event(self, event: tcod.event.Event) -> None:
#         """Move the player on events and handle"""
#         match event:
#             case tcod.event.Quit():
#                 raise SystemExit()
#             case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
#                 self.player_x -= 1
#             case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
#                 self.player_x += 1
#             case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
#                 self.player_y -= 1
#             case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
#                 self.player_y +=1



def main() -> None:
    """Load a tileset and open a window using it,
    this window will immediately close"""
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png",
        columns=16,
        rows=16,
        charmap=tcod.tileset.CHARMAP_CP437
        )
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80, 50, order="F")  # size of console
    state = game.states.InGame()
    g.world = game.world_tools.new_world()
    with tcod.context.new(console=console, tileset=tileset) as g.context:
        while True:  # Main loop
            console.clear()  # Clear the console before any drawing
            state.on_draw(console)  # Draw current state
            g.context.present(console)  # Render the console to the window and show it
            for event in tcod.event.wait():  # Event loop, blocks until pending events exist
                print(event)
                state.on_event(event) # This passes the events to the state


if __name__ == "__main__":
    main()
