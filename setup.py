from setuptools import setup, find_packages
setup(name='urly-twirly',
        version='1.0',
        author='Cory Westropp',
        author_email='cory@crwest.com',
        url='crwest.com',
        packages = find_packages(),
        install_requires=['Flask','Gunicorn']
        )