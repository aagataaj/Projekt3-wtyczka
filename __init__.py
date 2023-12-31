# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wtyczka_projekt_3
                                 A QGIS plugin
 Wtyczka liczy różne rzeczy. To jest przewyższenie między dwoma punktami i pole wieloboku opartego na wskazanych puntkach
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-08
        copyright            : (C) 2023 by Agata Jakubiak
        email                : 01159913@pw.edu.pl
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
    """Load wtyczka_projekt_3 class from file wtyczka_projekt_3.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .wtyczka_proj_3 import wtyczka_projekt_3
    return wtyczka_projekt_3(iface)
