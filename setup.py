from setuptools import setup, find_packages

setup(
    name="CBenchF",
    version="0.0.1",
    description="SDN Controller Performance Testing Framework",
    url="https://github.com/dfarrell07/CBenchF",
    author="Daniel Farrell",
    author_email="dfarrell07@redhat.com",
    # See for more classifer options: http://goo.gl/8jtDH4
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Flask",
        "Natural Language :: English",
        # TODO: Test with other versions of Python
        "Programming Language :: Python :: 2.7",
    ],
    keywords="SDN Software Defined Networking OpenDaylight controller \
              performace testing CBench WCBench OpenStack",
    packages=find_packages(),
    test_suite="tests",
    # See for more install_requires info: http://goo.gl/vCOKSw
    # See for more install_requires info: http://goo.gl/5zQKIF
    # TODO: List all known minimum requirements
    install_requires=["pyyaml"],
    # TODO: List dev and test env requirements
    extras_require={
        "dev": [],
        "test": ["tox", "flake8"],
    },
    # TODO: Do we need to specify any package data?
    # ^^See: https://github.com/pypa/sampleproject/blob/master/setup.py#L81
    # TODO: Do we need to define an entry point?
    # ^^See: https://github.com/pypa/sampleproject/blob/master/setup.py#L95
)
