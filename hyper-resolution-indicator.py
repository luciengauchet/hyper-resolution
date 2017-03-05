#!/usr/bin/env python3

import os
import signal
from subprocess import call
from gi.repository import Gtk
from gi.repository import AppIndicator3 as AppIndicator

APPINDICATOR_ID = "hyper-resolution-indicator"
resolutionState = "default"
xres = int(os.popen("xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f1").read().strip("\n"))
yres = int(os.popen("xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f2").read().strip("\n"))
output = os.popen("xrandr --current | grep ' connected' | uniq | awk '{print $1}' | cut -d ' ' -f1").read().strip("\n")

def main():
    indicator = AppIndicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('/home/lucien/Applications/scripts/hyper-resolution-indicator/icon.svg'), AppIndicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    Gtk.main()

def build_menu():
    menu = Gtk.Menu()
    #default
    item_default = Gtk.MenuItem('Default')
    item_default.connect('activate', reset_default)
    menu.append(item_default)
    #brightness
    item_scale_110 = Gtk.MenuItem('Scale 110%')
    item_scale_110.connect('activate', scale_110)
    menu.append(item_scale_110)
    item_scale_115 = Gtk.MenuItem('Scale 115%')
    item_scale_115.connect('activate', scale_115)
    menu.append(item_scale_115)
    item_scale_125 = Gtk.MenuItem('Scale 125%')
    item_scale_125.connect('activate', scale_125)
    menu.append(item_scale_125)
    item_scale_150 = Gtk.MenuItem('Scale 150%')
    item_scale_150.connect('activate', scale_150)
    menu.append(item_scale_150)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #quit
    item_quit = Gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def scale_110(source):
    r = 1.1
    nxres = int(xres*r)
    nyres = int(yres*r)
    call(["xrandr", "-d",":0", "--output", output, "--mode", str(xres)+'x'+str(yres), "--crtc", "1", "--scale-from" ,str(nxres)+'x'+str(nyres), "--panning", str(nxres)+'x'+str(nyres)])

def scale_115(source):
    r = 1.15
    nxres = int(xres*r)
    nyres = int(yres*r)
    call(["xrandr", "-d",":0", "--output", output, "--mode", str(xres)+'x'+str(yres), "--crtc", "1", "--scale-from" ,str(nxres)+'x'+str(nyres), "--panning", str(nxres)+'x'+str(nyres)])

def scale_120(source):
    r = 1.2
    nxres = int(xres*r)
    nyres = int(yres*r)
    call(["xrandr", "-d",":0", "--output", output, "--mode", str(xres)+'x'+str(yres), "--crtc", "1", "--scale-from" ,str(nxres)+'x'+str(nyres), "--panning", str(nxres)+'x'+str(nyres)])

def scale_125(source):
    r = 1.25
    nxres = int(xres*r)
    nyres = int(yres*r)
    call(["xrandr", "-d",":0", "--output", output, "--mode", str(xres)+'x'+str(yres), "--crtc", "1", "--scale-from" ,str(nxres)+'x'+str(nyres), "--panning", str(nxres)+'x'+str(nyres)])

def scale_150(source):
    r = 1.5
    nxres = int(xres*r)
    nyres = int(yres*r)
    call(["xrandr", "-d",":0", "--output", output, "--mode", str(xres)+'x'+str(yres), "--crtc", "1", "--scale-from" ,str(nxres)+'x'+str(nyres), "--panning", str(nxres)+'x'+str(nyres)])

def reset_default(source):
    r = 1
    nxres = int(xres*r)
    nyres = int(yres*r)
    call(["xrandr", "-d",":0", "--output", output, "--mode", str(xres)+'x'+str(yres), "--crtc", "1", "--scale-from" ,str(nxres)+'x'+str(nyres), "--panning", str(nxres)+'x'+str(nyres)])


if __name__ == "__main__":
    #keyboard interrupt handler
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
