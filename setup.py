from setuptools import setup

setup(name='thonny-syntax-dark-high-contrast-flinti',
      version='0.1',
      description='Higher contrast than the Default Dark theme',
      author='flinti',
      author_email='flinti@flinti.de',
      license='WTFPL',
      url='https://github.com/flinti/thonny-syntax-dark-high-contrast',
      packages=['thonnycontrib.thonny-syntax-dark-high-contrast-flinti'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        ],
      install_requires = [
            "thonny >=3.0",
        ],
      python_requires='>=3.6',
      )
