#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


def setup():
    autotools.rawConfigure("-disable-gtk -disable-gtk2 -disable-tcl -disable-ssl -disable-apache -without-nethttpd -without-rpc-auth-dh -bindir /usr/bin -datadir /usr/share/ocamlnet")

def build():
    autotools.make("-j1 all")

def install():
    install_dir = get.installDIR() + "/usr/lib/ocaml/site-lib"
    shelltools.export("OCAMLFIND_DESTDIR", install_dir)
    shelltools.export("OCAMLFIND_LDCONF", "ignore")

    shelltools.makedirs(install_dir)
    autotools.rawInstall("DESTDIR=%s" % install_dir)
