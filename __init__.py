# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Thematic
                                 A QGIS plugin
 Plugin for the evaluation of thematic accuracy on vector cartography
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-08-09
        copyright            : (C) 2021 by Harold Mercado LLanos
        email                : hmercado78@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Thematic class from file Thematic.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Thematic_accuracy import Thematic
    return Thematic(iface)
