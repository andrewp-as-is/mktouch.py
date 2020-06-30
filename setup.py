import setuptools

setuptools.setup(
    name='mktouch',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/mktouch']
)
