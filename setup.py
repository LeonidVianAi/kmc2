# MIT License
#
# Copyright (c) 2016 Olivier Bachem
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# import numpy as np
import numpy as np
from setuptools import setup, Extension

module1 = Extension(
    'kmc2',
    sources=['kmc2.c'],
    extra_compile_args=['-O3'],
    define_macros=[
        ('exc_traceback', 'curexc_traceback'),
        ('exc_value', 'curexc_value'),
        ('exc_type', 'curexc_type'),
        ('tp_print', 'tp_vectorcall_offset'),
        ('NPY_NO_DEPRECATED_API', '1'),
    ],
    include_dirs=[np.get_include(),"."]
)

setup(
    name='kmc2',
    version='0.1',
    description='Cython implementation of k-MC2 and AFK-MC2 seeding',
    url="http://www.olivierbachem.ch/",
    author='Olivier Bachem',
    author_email='olivier.bachem@inf.ethz.ch',
    license='MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    keywords='machine learning clustering kmeans',
    install_requires=["numpy", "scipy", "scikit-learn", "nose"],
    ext_modules=[module1]
)
