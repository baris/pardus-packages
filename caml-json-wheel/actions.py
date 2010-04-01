#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

WorkDir="json-wheel-1.0.6"

def setup():
    pass

def build():
    autotools.make("-j1 all")
    autotools.make("-j1 opt")

def install():
    install_dir = get.installDIR() + "/usr/lib/ocaml/site-lib"
    usr_dir = get.installDIR() + "/usr"
    shelltools.export("OCAMLFIND_DESTDIR", install_dir)
    shelltools.export("OCAMLFIND_LDCONF", "ignore")

    shelltools.makedirs(install_dir)
    shelltools.makedirs(usr_dir+"/bin")
    autotools.rawInstall("DESTDIR=%s PREFIX=%s" % (install_dir, usr_dir))
