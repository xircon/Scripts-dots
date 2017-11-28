#!/usr/bin/env python
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init("App Name")
Notify.Notification.new("\nHi\n").show()
