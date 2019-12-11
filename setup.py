from distutils.core import setup
import setuptools

setup(name='regexify',
      version='0.1.0',
      description='Regular expression containers and helper functions',
      url='https://github.com/dcronkite/regexify',
      author='dcronkite',
      author_email='dcronkite@gmail.com',
      license='MIT',
      classifiers=[  # from https://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3 :: Only',
      ],
      entry_points={
          'console_scripts':
              [
              ]
      },
      install_requires=[],
      package_dir={'': 'src'},
      packages=setuptools.find_packages('src'),
      zip_safe=False
      )
