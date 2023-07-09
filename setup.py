from setuptools import find_packages, setup
import subprocess


def get_latest_git_tag():
    try:
        version = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
        version = version.strip().decode(
            "utf-8"
        )  # Remove trailing newline and decode bytes to string

        # Remove the 'v' from the tag
        if version.startswith("v"):
            version = version[1:]

        return version
    except Exception as e:
        print(f"An exception occurred while getting the latest git tag: {e}")
        return None


VERSION = get_latest_git_tag() or "0.0.1"  # Fallback version
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/yazdipour/OmnivoreX/issues",
    "Source Code": "https://github.com/yazdipour/OmnivoreX",
}

setup(
    name="omnivorex",
    version=VERSION,
    description="Omnivore Terminal App - Text User Interface",
    author="Shahriar Yazdipour",
    author_email="git@yazdipour.com",
    packages=["src.omnivorex"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="omnivore cli terminal readlater client tui rich textualize textual",
    url=PROJECT_URLS["Source Code"],
    project_urls=PROJECT_URLS,
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "python-dotenv",
        "omnivoreql>=0.2.1",
        "textual==0.29.0",
    ],
    entry_points={
        "console_scripts": [
            "omnivorex=src.omnivorex.__main__:main",
        ],
    },
)
