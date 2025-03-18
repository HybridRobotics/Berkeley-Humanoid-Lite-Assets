"""Installation script for the 'air_assets' python package."""

from setuptools import setup

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    # NOTE: Add dependencies
    "psutil",
]

# Installation operation
setup(
    name="air_assets",
    packages=["air_assets"],
    author="-T.K.-",
    maintainer="-T.K.-",
    url="",
    version="0.0.1",
    description="",
    keywords=["extension", "isaaclab"],
    install_requires=INSTALL_REQUIRES,
    license="MIT",
    include_package_data=True,
    python_requires=">=3.10",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Isaac Sim :: 4.5.0",
    ],
    zip_safe=False,
)
