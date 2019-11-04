# ex46 搭建项目骨架

# 关于virtualenv的一些琐事
# [python - Virtualenv Command Not Found - Stack Overflow](https://stackoverflow.com/questions/31133050/virtualenv-command-not-found)
# sudo /usr/bin/easy_install virtualenv❌行不通
# /usr/local/bin/virtualenv ✅行得通 晕

# 懒人备用：. ~/.venvs/lpthw/bin/activate

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
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)