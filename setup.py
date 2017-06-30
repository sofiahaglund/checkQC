from setuptools import setup, find_packages
from qc_gate import __version__


setup(
    name='qc_gate',
    version=__version__,
    description="A simple program to parse Illumina NGS data and check it for quality criteria.",
    long_description="A simple program to parse Illumina NGS data and check it for quality criteria.",
    keywords='bioinformatics',
    author='SNP&SEQ Technology Platform, Uppsala University',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['qc_gate = qc_gate.app:start']
    },
)