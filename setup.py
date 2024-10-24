from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='dm-aioinfluxdb',
    version='0.0.0',
    author='dimka4621',
    author_email='mismartconfig@gmail.com',
    description='This is my custom aioinfluxdb client',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://pypi.org/project/dm-aioinfluxdb',
    packages=find_packages(),
    install_requires=[
        'dm-logger~=0.5.2',
        'aiohttp>=3.9.2, <4.0.0',
        'aiocsv>=1.2.5, <2.0.0',
        'influxdb-client~=1.39.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='dm aioinfluxdb',
    project_urls={
        'GitHub': 'https://github.com/MykhLibs/dm-aioinfluxdb'
    },
    python_requires='>=3.8'
)
