# -*- coding: utf-8 -*-
# Copyright (C) 2018-2020 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sys import stderr
from lxml import etree


def yes_or_no(question):
    """Asks the user to proceed or not in a gvmtools script

    Arguments:
        question (str): The condition the user should answer
    """
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == ('y'):
        return True
    if reply[0] == ('n'):
        return False
    else:
        return yes_or_no("Please enter 'y' or 'n'")


def error_and_exit(msg):
    """Prints an error message and quits the gvmtools script

    Arguments:
        msg (str): The error message, that will be printed
    """
    print("\nError: {}\n".format(msg), file=stderr)
    quit(1)


def create_xml_tree(xml_doc):
    """Creates an XML tree that can be read by an gvmtools script

    Arguments:
        xml_doc (str): Path to the xml document
    """
    try:
        xml_tree = etree.parse(xml_doc)
        xml_tree = xml_tree.getroot()
    except IOError as err:
        error_and_exit("Failed to read xml_file: {} (exit)".format(str(err)))
    except etree.Error as err:
        error_and_exit("Failed to parse xml_file: {} (exit)".format(str(err)))

    if len(xml_tree) == 0:
        error_and_exit("XML file is empty (exit)")

    return xml_tree
