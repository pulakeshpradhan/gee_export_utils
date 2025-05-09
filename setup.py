from setuptools import setup, find_packages

setup(
    name="gee_export_utils",  # package name
    version="0.1.0",  # follow semantic versioning
    packages=find_packages(),
    install_requires=[
        "earthengine-api>=0.1.0",
        "geemap>=0.20.0"
    ],
    author="Pulakesh Pradhan",
    author_email="your_email@example.com",  # optional but recommended
    description="Utility functions for exporting Earth Engine images to Drive or downloading locally",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pulakeshpradhan/gee_export_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
