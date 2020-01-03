from setuptools import find_packages, setup


requires = ["prompt_toolkit"]

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="xrandr_manager",
    version="0.1.0",
    description="Xrandr manager",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="deresmos",
    author_email="deresmos@gmail.com",
    url="https://github.com/deresmos/xrandr-manager",
    python_requires=">=3.7",
    packages=find_packages(),
    include_package_data=False,
    keywords=["tools"],
    license="MIT License",
    install_requires=requires,
    entry_points={"console_scripts": ["xrandr-manager = xrandr_manager.console:run"]},
)
