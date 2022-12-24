import time

import pytermgui as ptg


def macro_time(fmt: str) -> str:
    return time.strftime(fmt)


ptg.tim.define("!time", macro_time)


with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(
        ptg.Window("[bold]The current time is:[/]\n\n[!time 25]%c[/]\n\n[78 @34;123;255]My name is: [inverse] Amin [/]", box="EMPTY")
    )
