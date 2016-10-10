from setuptools import find_packages, setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='xfoliate',
    version='0.0.1',
    license='MIT',
    packages=find_packages(),
    install_requires=['facebook-sdk', 'requests'],  # TODO
    author='Jorden Kreps',
    author_email='jk788@nau.edu',
    description='xfoliate your facebook with this one simple click!',
    long_description=long_description,
    url='https://github.com/jakereps/xfoliate'
)
