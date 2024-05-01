from setuptools import setup, find_packages

setup(
    name='website_checker',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        website_checker=check_sites.main:check_sites
    ''',
)
