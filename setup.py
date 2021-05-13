from setuptools import setup


setup(
    name='pycalltrace',
    version='0.1',
    url='https://github.com/kwsy/calltrace',
    license='BSD',
    author='dongsheng zhang',
    author_email='xigongda200608@163.com',
    description='record and trace the function call chain',
    py_modules= ['calltrace',],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)