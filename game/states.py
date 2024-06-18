"""A collection of game states"""
from __future__ import annotations
from typing import Final
import attrs
import tcod.console
import tcod.event
from tcod.event import KeySym as key
import g
from game.components import *
from game.tags import *


DIRECTION_KEYS: Final = {
    # Arrow Keys
    key.LEFT: (-1, 0),
    key.RIGHT: (1, 0),
    key.UP: (0, -1),
    key.DOWN: (0, 1),
    # Diags
    key.END: (-1, 1),
    key.HOME: (-1, -1),
    key.PAGEUP: (1, -1),
    key.PAGEDOWN: (1, 1),
    # Keypad
    # Keypad
    key.KP_4: (-1, 0),
    key.KP_6: (1, 0),
    key.KP_8: (0, -1),
    key.KP_2: (0, 1),
    key.KP_7: (-1, -1),
    key.KP_1: (-1, 1),
    key.KP_9: (1, -1),
    key.KP_3: (1, 1),
    # VI keys
    key.h: (-1, 0),
    key.l: (1, 0),
    key.k: (0, -1),
    key.j: (0, 1),
    key.y: (-1, -1),
    key.b: (-1, 1),
    key.u: (1, -1),
    key.n: (1, 1),
}


@attrs.define(eq=False)
class InGame:
    """Primare in-game state"""

    def on_event(self, event: tcod.event.Event) -> None:
        """Handle events for the in-game state"""
        (player,) = g.world.Q.all_of(tags=[IsPlayer])
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=sym) if sym in DIRECTION_KEYS:
                player.components[Position] += DIRECTION_KEYS[sym]
                # Auto Pickup Gold
                for gold in g.world.Q.all_of(
                        components=[Gold],
                        tags=[player.components[Position], IsItem]
                ):
                    player.components[Gold] += gold.components[Gold]
                    text = f"Picked up {gold.components[Gold]} gold, TOTAL GOLD: {player.components[Gold]} Gold"
                    g.world[None].components[("Text", str)] = text
                    gold.clear()


    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the standard screen"""
        for entity in g.world.Q.all_of(components=[Position, Graphic]):
            pos = entity.components[Position]
            if not (0 <= pos.x < console.width and 0 <= pos.y < console.height):
                continue
            graphic = entity.components[Graphic]
            console.rgb[["ch", "fg"]][pos.x, pos.y] = graphic.ch, graphic.fg

        if text := g.world[None].components.get(("Text", str)):
            console.print(x=0, y=console.height - 1, string = text, fg=(255,255,255), bg=(0,0,0))

