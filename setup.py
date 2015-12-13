from setuptools import setup

setup(
    name="toutf8",
    version="1.3.0",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="A tool to change all files in specified folder to utf-8 encoding",
    author='1e0n',
    author_email='i@leons.im',
    keywords='utf8 encoding gbk gb2312 shiftjis ascii gb18030',
    url='https://github.com/liangsun/toutf8',
    packages=['toutf8'],
    install_requires=['chardet'],
    entry_points={
        'console_scripts': [
            'toutf8=toutf8:main',
        ],
    },
)
