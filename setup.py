from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(name='ZabbixSender',
      version='0.1.9',
      description='Simple zabbix sender',
      long_description=readme,
      author='Maksim Syomochkin',
      author_email='maksim77ster@gmail.com',
      url='https://github.com/maksim77/zsender',
      py_modules=['ZabbixSender'],
      keywords='zabbix sender monitoring',
      license='Apache Software License',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Networking :: Monitoring',
          'Topic :: System :: Systems Administration'
      ]
      )
