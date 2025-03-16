from setuptools import setup, find_packages

setup(
    name='tidyfs',
    version='1.0.0',
    author='DOSSEH Shalom',
    author_email='dossehdosseh14@gmail.com',
    description='tidyfs is a simple CLI tool to organize files in a directory',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AnalyticAce/tidyfs',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'typer',
        'cron-validator',
    ],
    entry_points={
        'console_scripts': [
            'tidyfs=tidyfs.cli:app',
        ],
    }
)
