from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='bytecode_tools',
      version='0.0.1',
      description="Python bytecode tools",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/gsb-eng/bytecode_tools',
      author='Srinivas Garlapati',
      author_email='gsb@gsb-eng.com',
      packages=find_packages(exclude=['contrib', 'docs', 'tests', 'bin']),
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
)


