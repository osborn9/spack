# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Egret(PythonPackage):
    """EGRET."""

    git      = "https://github.com/osborn9/Egret.git"
    maintainers = ['osborn9']

    version('develop', branch='acorn-updates')

    depends_on('python@3.7:')

    depends_on('py-pyomo', type=('build', 'run'))
