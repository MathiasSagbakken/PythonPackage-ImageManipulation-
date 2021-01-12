from distutils.core import setup


setup(
    name='instapy',
    version='1.0',
    install_requires = ['numba','numpy','pytest','opencv-python'],
    scripts=['bin/instapy'],
    packages=['instapyP'],
    entry_points={'console_scripts': ['instapyP=bin.instapy:main'],} 
)
