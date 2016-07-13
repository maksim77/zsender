try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup


setup(name='ZabbixSender',
      version='0.2.7',
      description='Simple zabbix sender',
      long_description=open('README.rst', 'r').read() + '\n\n' + open(
          'CHANGELOG.rst', 'r').read(),
      author='Maksim Syomochkin',
      author_email='maksim77ster@gmail.com',
      url='https://github.com/maksim77/zsender',
      packages=['ZabbixSender'],
      include_package_data=True,
      package_data={'tests': ['*']},
      keywords='zabbix sender monitoring',
      license='Apache Software License',
      test_suite='tests',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Intended Audience :: System Administrators',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Networking :: Monitoring',
          'Topic :: System :: Systems Administration'
      ]
      )
