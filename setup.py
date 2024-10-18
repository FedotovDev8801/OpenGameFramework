from setuptools import setup, find_packages

setup(
    name="GameSimulation-Engine",
    version="SDK1.0",
    packages=find_packages(),
    install_requires=[
        'Pygame>=2.6.1'
        'ABC>=2.0.0'
    ],
    author="FedotovDev",
    author_email="email@example.com",
    description="Game engine like XNA but on Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FedotovDev8801/GameSimulation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
