# -*- coding: utf-8 -*-
## PloneBooking: Online Booking Tool to allow booking on any kind of ressource
## Copyright (C)2005 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
    PloneBooking: Vocabulary
"""

__version__ = "$Revision: 1.4 $"
__author__  = ''
__docformat__ = 'restructuredtext'

from Products.Archetypes.utils import DisplayList

from Products.PloneBooking import PloneBookingFactory as _

CALENDAR_REFRESH_MODES = DisplayList((
    ('auto', _(u'label_refresh_auto', default=u'Automatic')),
    ('manual', _(u'label_refresh_manual', default=u'Manual')),
))

REQUIRED_FILTERS = DisplayList((
    ('type', _(u'label_type', default=u'Type')),
    ('category', _(u'label_category', default=u'Category')),
    ('resource', _(u'label_resource', default=u'Resource'))))

CALENDAR_VIEWS = DisplayList((
    ('day', _(u'label_day', default=u'Day')),
    ('week', _(u'label_week', default=u'Week')),
    ('month', _(u'label_month', default=u'Month'))))

LISTING_VIEWS = DisplayList((
    ('day', _(u'label_day', default=u'Day')),
    ('week', _(u'label_week', default=u'Week')),
    ('month', _(u'label_month', default=u'Month')),
    ('year', _(u'label_year', default=u'Year'))))

VIEW_MODES = DisplayList((
    ('listing', _(u'label_listing', default=u'Listing')),
    ('calendar', _(u'label_calendar', default=u'Calendar')),
))

BOOKING_REVIEW_MODES = DisplayList((
    ('default', _(u'label_default_booking_review_mode', default=u'Default (in booking center)')),
    ('review', _(u'label_review_bookings', default=u'Review bookings')),
    ('publish', _(u'label_publish_automatically_bookings', default=u'Publish automatically bookings'))))

GLOBAL_BOOKING_REVIEW_MODES = DisplayList((
    ('review', _(u'label_review_bookings', default=u'Review bookings')),
    ('publish', _(u'label_publish_automatically_bookings', default=u'Publish automatically bookings'))))
