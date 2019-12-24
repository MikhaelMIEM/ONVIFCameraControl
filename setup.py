import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [l.strip() for l in file]

setuptools.setup(
    name="ONVIFCameraControl",
    version="1.0.6",
    author="Mikhael",
    author_email="mikhail-miem@yandex.ru",
    description="Simple camera controls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MikhaelMIEM/ONVIFCameraControl",
    packages=setuptools.find_packages(exclude=['example']),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)