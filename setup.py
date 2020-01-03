from setuptools import find_packages, setup

__author__ = "deresmos"

setup(
    name="xrandr_manager",
    version="0.1.0",
    description="Xrandr manager",
    author="deresmos",
    author_email="deresmos@gmail.com",
    packages=find_packages(),
    include_package_data=False,
    keywords=["tools"],
    license="MIT License",
    install_requires=["dataclasses", "prompt_toolkit"],
    entry_points={"console_scripts": ["xrandr-manager = xrandr_manager.console:run"]},
)
