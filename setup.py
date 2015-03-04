from setuptools import setup, find_packages


setup(
    name='helga-stfu',
    version='0.1.0',
    description=("A helga plugin that can be used to store responses "
                 "that can be returned from a question"),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Framework :: Twisted',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='helga stfu silencer',
    author="Shaun Duncan",
    author_email="shaun.duncan@gmail.com",
    url="https://github.com/shaunduncan/helga-stfu",
    packages=find_packages(),
    py_modules=['helga_stfu'],
    include_package_data=True,
    zip_safe=True,
    entry_points=dict(
        helga_plugins=[
            'stfu = helga_stfu:stfu',
        ],
    ),
)
