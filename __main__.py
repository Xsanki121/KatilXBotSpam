# KatilXSpam || @KatilXSupport

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from KatilXSpam.utils import load_plugins
import logging
from telethon import events
from . import Kat, Kat2, Kat3, Kat4, Kat5, Kat6, Kat7, Kat8, Kat9, Kat10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "KatilXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Katil X BotSpam Successfully Deployed !!")
print("Enjoy..!  Do Visit @KatilXSupport")

if __name__ == "__main__":
    Kat.run_until_disconnected()
    
if __name__ == "__main__":
    Kat2.run_until_disconnected()

if __name__ == "__main__":
    Kat3.run_until_disconnected()
    
if __name__ == "__main__":
    Kat4.run_until_disconnected()

if __name__ == "__main__":
    Kat5.run_until_disconnected()
    
if __name__ == "__main__":
    Kat6.run_until_disconnected()
    
if __name__ == "__main__":
    Kat7.run_until_disconnected()

if __name__ == "__main__":
    Kat8.run_until_disconnected()
    
if __name__ == "__main__":
    Kat9.run_until_disconnected()

if __name__ == "__main__":
    Kat10.run_until_disconnected()    
