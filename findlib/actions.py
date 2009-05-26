#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    autotools.rawConfigure("-bindir %(root)s/usr/bin/ -mandir %(root)s/usr/share/man -config %(root)s/etc -sitelib %(root)s/usr/lib/ocaml/site-lib/" % {"root": get.installDIR()})

def build():
    autotools.make()

def install():
    shelltools.makedirs("%s/etc" % get.installDIR())
    autotools.rawInstall()
