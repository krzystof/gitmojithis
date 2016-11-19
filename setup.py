from distutils.core import setup

setup(
    name='gitmojithis',
    packages=['gitmojithis'],
    include_package_data=True,
    install_requires=[
        'gitmojithis',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)