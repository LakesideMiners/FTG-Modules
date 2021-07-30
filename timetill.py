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


import logging
import datetime
from .. import loader, utils
logger = logging.getLogger(__name__)
@loader.tds
class PrettyTimeTillMod(loader.Module):
    """A Pretty Time Until im 18 mod"""  # Translateable due to @loader.tds
    strings = {"cfg_doc": "This is what is said, you can edit me with the configurator",
               "name": "newtime",
               "after_sleep": "We have finished sleeping!"}

    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m))

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def TimeTillcmd(self, message):
        """Time Till I'm 18"""

        stop = datetime.datetime(2021, 12, 20, 0, 0, 0)
        logger.debug("We logged something!")
        
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        left_day = str(difference.days)
        left_hour = str(count_hours)
        left_min = str(count_minutes)
        left_second = str(count_seconds)
        
        if difference.days <= 0 and count_hours <= 0 and count_minutes <= 0 and count_seconds <= 0:
          await utils.answer(message, str("Red Kitters is 18!"))
        elif difference.days <= 7:
          countdown_pretty = left_day + " Days" + "\n" + left_hour + " Hours" + "\n" + left_min + " Minutes" + "\n" + left_second + " Seconds" + "\n" + "Until Red Kitters is 18"
          await utils.answer(message, str(countdown_pretty))
        else:
          countdown_pretty = left_day + " Days " + "Until Red Kitters is 18"
          await utils.answer(message, str(countdown_pretty))
