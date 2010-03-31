#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

WorkDir="pcre-ocaml-release-6.0.1"

def setup():
    pass

def build():
    autotools.make("all")

def install():
    install_dir = get.installDIR() + "/usr/lib/ocaml/site-lib"
    shelltools.export("OCAMLFIND_DESTDIR", install_dir)
    shelltools.export("OCAMLFIND_LDCONF", "ignore")

    shelltools.makedirs(install_dir)
    autotools.rawInstall("DESTDIR=%s" % install_dir)
