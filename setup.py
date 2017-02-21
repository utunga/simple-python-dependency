from setuptools import setup, find_packages
description = 'simple dependency testing thing'
name = 'simple_python_dependency'
setup(
    name=name,
    version='0.1.0',
    namespace_packages=name.split('.')[:-1],
    description=description or name,
    author='CreditSights Inc',
    url='https://github.com/creditsightsinc/' + name,
    # lists dependencies that will be installed by pip when installing this package
    install_requires=['requests'],
    # automatically finds the simple_python_dependency package below here
    packages=find_packages()
)