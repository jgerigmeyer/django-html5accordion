from os.path import join, dirname

from setuptools import setup

here = dirname(__file__)

long_description = open(join(here, "README.rst")).read()

setup(
    name="django-html5accordion",
    version="0.1.1",
    description="A Django packaging of jquery-html5accordion.js",
    long_description=long_description,
    author="Jonny Gerig Meyer",
    author_email="jonny@oddbird.net",
    url="https://github.com/jgerigmeyer/django-html5accordion/",
    packages=[
        "html5accordion"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
    ],
    zip_safe=False,
)