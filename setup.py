from setuptools import setup

setup(name='sbrl',
      version='1.1',
      description='python wrapper for R package sbrl',
      author='Hongyu Yang',
      author_email='hongyuy@mit.edu',
      license='MIT',
      packages=['sbrl'],
      install_requires=[
                        'numpy',
                        'pandas',
                        'rpy2',
                        ],
      zip_safe=False)