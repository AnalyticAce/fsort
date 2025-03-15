from setuptools import setup, find_packages

setup(
    name='fsort',
    version='1.0.0',
    author='DOSSEH Shalom',
    author_email='dossehdosseh14@gmail.com',
    description='A simple CLI tool to organize files in a directory',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AnalyticAce/fsort',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'typer',
        'pathlib',
        'cron-validator',
    ],
    entry_points={
        'console_scripts': [
            'fsort=fsort.cli:app',
        ],
    }
)
