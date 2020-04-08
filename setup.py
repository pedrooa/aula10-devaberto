from setuptools import setup
setup(name='dev_aberto_pedrooa',
	  python_requires='>3.5.2',
      version='0.1',
      author='Pedro Azambuja',
      author_email='pedrooa@al.insper.edu.br',
      packages=['dev_aberto'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
       install_requires=[
        'requests' ],
        scripts=['scripts/hello.py']
      )