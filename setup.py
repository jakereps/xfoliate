from setuptools import find_packages, setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='xfoliate',
    version='0.0.1',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click', 'facebook-sdk', 'nltk', 'requests'],
    author='Jorden Kreps',
    author_email='jk788@nau.edu',
    description='xfoliate your facebook with this one simple click!',
    long_description=long_description,
    url='https://github.com/jakereps/xfoliate',
    entry_points='''
        [console_scripts]
        xfoliate=xfoliate.__main__:run
    ''',
)
