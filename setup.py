from setuptools import setup, find_packages

setup(
    name="gee_export_utils",
    version="0.1",
    packages=find_packages(),
    install_requires=["earthengine-api", "geemap"],
    author="Your Name",
    description="Utilities for exporting Earth Engine images",
    url="https://github.com/yourusername/gee_export_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
