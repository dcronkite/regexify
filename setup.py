from distutils.core import setup
import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setup(name='regexify',
      version='0.1.1',
      description='Regular expression containers and helper functions',
      long_description=long_description,
      url='https://github.com/dcronkite/regexify',
      author='dcronkite',
      author_email='dcronkite+pypi@gmail.com',
      license='MIT',
      classifiers=[  # from https://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3 :: Only',
          'License :: OSI Approved :: MIT License',
      ],
      entry_points={
          'console_scripts':
              [
              ]
      },
      install_requires=[],
      package_dir={'': 'src'},
      packages=setuptools.find_packages('src'),
      zip_safe=False,
      python_requires='>=3.7',
      )
