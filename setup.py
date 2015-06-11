from setuptools import setup

setup(
    name='ChannelWorm',
    long_description=open('README.md').read(),
    install_requires=[
        'cypy',
        'sciunit',
        'PyOpenWorm',
        'PyNeuroML>=0.0.5'
    ],
    dependency_links=[
        'git+https://github.com/scidash/sciunit.git#egg=sciunit',
        'git+https://github.com/openworm/PyOpenWorm.git#egg=PyOpenWorm',
        'git+https://github.com/NeuroML/pyNeuroML.git#egg=PyNeuroML'
    ]
)
