from setuptools import setup, find_packages

setup(
    name='GitGuru',
    version='1.0.0',
    description='Intelligent git repository management and collaboration tool',
    author='mehrshud',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='git repository management collaboration tool',
    project_urls={
        'Documentation': 'https://github.com/mehrshud/GitGuru',
        'Source Code': 'https://github.com/mehrshud/GitGuru',
        'Issue Tracker': 'https://github.com/mehrshud/GitGuru/issues',
    },
)
