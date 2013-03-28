#!/usr/bin/env python

from setuptools import setup


def get_version(fname='latexmake.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])

setup(
      name='latexmk.py',
      version=get_version(),
      description=('Latexmk.py completely automates the process of '
                   'generating a LaTeX document.'),
      long_description=('Latexmk.py completely automates the process of '
                        'generating a LaTeX document. Given the source files '
                        'for a document, latexmk.py issues the appropriate '
                        'sequence of commands to generate a .dvi or .pdf '
                        'version of the document.'),
      author='Marc Schlaich',
      author_email='marc.schlaich@googlemail.com',
      url='http://github.com/schlamar/latexmk.py',
      license='MIT',
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Printing',
                   'Topic :: Text Processing :: Markup :: LaTeX'],

      py_modules=['latexmake'],
      entry_points={'console_scripts': ['latexmk.py = latexmake:main']},
      )
