# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Squirrel(CMakePackage):
    """A general purpose library for the direct solution of large, sparse,
    nonsymmetric systems of linear equations on high performance machines."""

    git      = "https://lc.llnl.gov/gitlab/squirrel/squirrel.git"

    maintainers = ['osborn9']

    version('develop', branch='master')

    variant('mpi', default=True, description='Build with 64 bit integers')
    variant('shared', default=True, description='Build shared libraries')
    variant('mordor', default=False, description='Enable dimension-reduction (MORDOR) capability')

    depends_on('mpi', when="+mpi")
    depends_on('lapack')
    depends_on('metis@5:', when="+mordor")

    # We don't play nice with openmpi; use mpich instead
    #conflicts('^openmpi')

    def cmake_args(self):
        spec = self.spec
        cmake_args = []

        if  '+mpi' in spec:
          cmake_args.extend([
            '-DSQUIRREL_ENABLE_TESTING=OFF',
            '-DSQUIRREL_WITH_MPI=ON',
            '-DMPI_CXX_COMPILER=%s' % spec['mpi'].mpicxx
          ])
        else:
          cmake_args.extend([
            '-DSQUIRREL_WITH_MPI=OFF'])
        if '+mordor' in spec:
          cmake_args.extend([
            '-DSQUIRREL_ENABLE_MORDOR=ON',
            '-DSQUIRREL_WITH_METIS=%s' % spec['metis'].libs
          ])

        return cmake_args
