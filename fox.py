#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging
from .. import loader, utils
import requests
logger = logging.getLogger(__name__)

@loader.tds
class FoxMod(loader.Module):
    """Description for module"""  # Translateable due to @loader.tds
    strings = {"cfg_doc": "Getsfox",
               "name": "fox",
               "after_sleep": "a fox"}

    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m))

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def foxcmd(self, message):
        """getsfox"""
        url = "https://sheri.bot/api/fox/"
        r = requests.get(url)
        answer = r.json()
        imageurl = answer["url"]
        
        await utils.answer(message, str(imageurl))
