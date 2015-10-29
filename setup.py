"""
This is a setup.py script generated by py2exe

Usage:
    python setup.py py2exe
"""


from distutils.core import setup

import sys
import os

def tree(src):
    return [(root, map(lambda f: os.path.join(root, f), files)) for (root, dirs, files) in os.walk(os.path.normpath(src))]


APP = ['Traktor Librarian.py']
DATA_FILES = tree('static') + tree('templates')
OPTIONS_OSX = {'argv_emulation': False,
               'strip': True,
           'iconfile': 'icon.icns',
           'includes': ['WebKit', 'Foundation', 'webview', 'psutil']}

OPTIONS_WIN32 = {
    'bundle_files': 3,
    'compressed': False,
    'includes': ['win32gui', 'win32con', 'win32api', 'win32ui', 'ctypes', 'comtypes', 'webview']}

if sys.platform == "darwin":
    import py2app

    setup(
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS_OSX},
        setup_requires=['py2app'],
    )
elif sys.platform == "win32":
    import py2exe

    # ModuleFinder can't handle runtime changes to __path__, but win32com uses them
    try:
        # py2exe 0.6.4 introduced a replacement modulefinder.
        # This means we have to add package paths there, not to the built-in
        # one.  If this new modulefinder gets integrated into Python, then
        # we might be able to revert this some day.
        # if this doesn't work, try import modulefinder
        try:
            import py2exe.mf as modulefinder
        except ImportError:
            import modulefinder
        import win32com, sys
        for p in win32com.__path__[1:]:
            modulefinder.AddPackagePath("win32com", p)
        for extra in ["win32com.shell"]: #,"win32com.mapi"
            __import__(extra)
            m = sys.modules[extra]
            for p in m.__path__[1:]:
                modulefinder.AddPackagePath(extra, p)
    except ImportError:
        # no build path setup, no worries.
        pass

    setup(
        data_files=DATA_FILES,
        options={'py2exe': OPTIONS_WIN32},
        setup_requires=['py2exe'],
        windows=[{
            'script': 'Traktor Librarian.py',
            'icon_resources': [(1, 'icon.ico')]
        }],
        zipfile=None
        )