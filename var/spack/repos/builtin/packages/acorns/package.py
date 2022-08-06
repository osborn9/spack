# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Acorns(CMakePackage):
    """The acorns of Squirrel."""

    git      = "https://lc.llnl.gov/gitlab/squirrel/acorns.git"

    maintainers = ['osborn9']

    version('develop', branch='install-exes-for-ui')

    depends_on('squirrel')
    depends_on('boost')
    depends_on('egret')

    def cmake_args(self):
        spec = self.spec
        cmake_args = []

        cmake_args.extend([
          '-DSQUIRREL_WITH_MPI=ON',
          '-DMPI_CXX_COMPILER=%s' % spec['mpi'].mpicxx,
          '-DSquirrel_DIR=%s' % spec['squirrel'].prefix.include,
          '-DACORNS_BUILD_ACORN_NS3=ON',
          '-DACORNS_BUILD_ACORN_EGRET=ON',
        ])

        return cmake_args
