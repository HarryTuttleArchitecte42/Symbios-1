from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="symbios-1",
    version="0.1.0-alpha",
    author="HarryTuttleArchitecte42",
    description="RBE conceptual kernel managed by 4-agent AI federation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HarryTuttleArchitecte42/Symbios-1",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        "crewai>=0.28.0",
        "anthropic>=0.18.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
    ],
)
