#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

WorkDir="xml-light"

def setup():
    pass

def build():
    autotools.make()

def install():
    target = "%s/usr/lib/ocaml/site-lib/xml-light" % get.installDIR()
    shelltools.makedirs(target)
    autotools.rawInstall("INSTALLDIR=%s" % target)
    shelltools.chmod(target+"/*", 0644)
