import asyncio
import string
from collections import deque

from prompt_toolkit import prompt_async  # $ pip install prompt_toolkit
from prompt_toolkit.shortcuts import Keys, Registry

BACKWARDS, STOP, FORWARD = 1, 0, -1


async def interactive_prompt(direction):
    registry = Registry()

    @registry.add_binding('q')
    @registry.add_binding(Keys.ControlC)
    def stop(event):
        direction[0] = STOP
        event.cli.set_return_value(False)  # exit

    @registry.add_binding(Keys.Up)
    def backwards(event):
        direction[0] = BACKWARDS

    @registry.add_binding(Keys.Down)
    def forward(event):
        direction[0] = FORWARD

    await prompt_async('Press Up/Down/Ctrl-C/q> ',
                       patch_stdout=True,  # show prompt
                       key_bindings_registry=registry)


async def print_chars(direction, chars=deque(string.ascii_lowercase)):
    while direction[0]:
        print(chars[0])
        await asyncio.sleep(1)
        chars.rotate(direction[0])

loop = asyncio.get_event_loop()
direction = [FORWARD]
loop.create_task(interactive_prompt(direction))
loop.run_until_complete(print_chars(direction))