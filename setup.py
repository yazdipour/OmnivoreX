from setuptools import setup, find_packages
import os

# Get version from __version__.py file
current_folder = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(current_folder, "omnivoreql", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name="omnivorex",
    version=about["__version__"],
    description='Omnivore API Client for Python',
    author='Shahriar Yazdipour',
    author_email='git@yazdipour.com',
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="omnivore cli terminal readlater client",
    url="https://github.com/yazdipour/omnivorex",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires=[
        'omnivoreql>=0.2.1',
    ],
    entry_points={
        'console_scripts': [
            'omnivorex=omnivorex.omnivorex:omnivorex',
        ],
    },
)
