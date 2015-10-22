from setuptools import setup

setup(
    name="toutf8",
    version="1.0.0",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="A tool to change all files in specified folder to utf-8 encoding",
    author='Liang Sun',
    author_email='i@liangsun.org',
    keywords='utf8 encoding gbk gb2312 shiftjis ascii gb18030',
    url='https://github.com/liangsun/toutf8',
    packages=['toutf8'],
    install_requires=['chardet'],
    entry_points={
        'console_scripts': [
            'toutf8=toutf8:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: Apache',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
