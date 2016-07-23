#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (C) 2014, William Edwards <shadowapex@gmail.com>
#
# This file is part of Tuxemon.
#
# Tuxemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tuxemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Tuxemon.  If not, see <http://www.gnu.org/licenses/>.
#
# Contributor(s):
#
# Adam Chevalier <chevalierAdam2@gmail.com>
# 
from __future__ import absolute_import

import logging

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)


class Common(object):
    def set_character_attribute(self, character, attribute, value):
        """Set's a character's (npc or player) attribute.

        :param character: The Player object to modify.
        :param attribute: The attribute to modify.
        :param value: The value to set the attribute to, as a string.

        :type character: core.Player
        :type attribute: String
        :type value: String

        :rtype: None
        :returns: None
        """

        # check for valid inputs
        # trigger an AttributeError if the attribute doesn't already exist
        attr = None
        try:
            attr = getattr(character, attribute)
        except:
            logger.warning("Player attribute '{0}' specified does not exist.", attribute)
            return

        val = None
        try:
            val = type(attr)(value)
        except:
            logger.warning("The value given cannot be parsed into the correct type for '{0}'", attribute)
            return

        setattr(player, attribute, val)

    def modify_character_attribute(self, character, attribute, modifier):
        """Modifyies a character's (npc or player) attribute. Default behavior is to add
        the given mod to the attribute, but prepending a percent (%) symbol will 
        cause the mod to be used as a multiplier.

        :param character: The Player object to modify.
        :param attribute: The attribute to modify.
        :param mod: The modifier to apply the attribute by.

        :type character: core.Player
        :type attribute: String
        :type modifier: string

        :rtype: None
        :returns: None
        """

        # check for valid inputs
        # trigger an AttributeError if the attribute doesn't already exist
        attr = None
        try:
            attr = getattr(character, attribute)
        except:
            logger.warning("Player attribute '{0}' specified does not exist.", attribute)
            return

        type(attr) x = None
        if '%' in modifier:
            mod = float(modifier.replace('%',''))
            attr = attr * mod
        else:
            mod = float(modifier)
            attr = attr + mod


        setattr(player, attribute, attr)

        