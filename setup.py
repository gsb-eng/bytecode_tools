from setuptools import find_packages, setup


setup(name='bytecode_tools',
      version='0.1',
      description='Python Bytecode tools.',
      url='',
      author='Srinivas Garlapati',
      author_email='gsb@gsb-eng.com',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)


