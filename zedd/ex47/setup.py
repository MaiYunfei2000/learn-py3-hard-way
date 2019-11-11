# ex47 自动化测试
# 运行没问题，但各种没搞明白，先挂着，以后再说。

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email: 572353500@qq.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)