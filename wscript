#!/bin/env python
from waflib.Utils import subprocess
import os
from waflib import Options, Node, Build, Configure
import re

out = 'build'

def configure(conf):
    join = os.path.join
    isabs = os.path.isabs
    abspath = os.path.abspath
    
    opts = vars(conf.options)
    conf.load('compiler_cxx python')
    conf.load('etest', tooldir='waftools')

    conf.check(header_name='stdio.h', features='cxx cxxprogram', mandatory=True)
    
    #Set correct data and input data directories for extended tests (etest)
    for dd in conf.path.ant_glob("test/testdata/correct/*"):
        pth = dd.relpath()
        conf.path.make_node(pth)
        print(pth)
    
    for dd in conf.path.ant_glob("test/testdata/in/*"):
        pth = dd.relpath()
        conf.path.make_node(pth)
        print(pth)

def options(ctx):
    ctx.load('compiler_cxx')
    ctx.load('etest', tooldir='waftools')

def build(bld):
    bld.load('etest', tooldir='waftools')
    bld.recurse('src')
