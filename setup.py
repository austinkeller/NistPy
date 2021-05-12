from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='nistpy',
    version='0.1.0',
    description='module for interfacing with NIST Webbook',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sabidhasan/NistPy',
    author='Abid Hasan',
    author_email='abidhasan@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=[
        'beautifulsoup4',
        'matplotlib',
        'pandas',
        'requests',
    ],
    extras_require={
        'dev': [
            'black',
            'check-manifest',
        ],
        'test': [
            'coverage',
            'pytest',
        ],
    },
    package_data={
        'species.txt': ['species.txt'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    #entry_points={
    #    'console_scripts': [
    #        'nistpy=nistpy:main',
    #    ],
    #},
)
