from distutils.core import setup

setup(name='ZabbixSender',
      version='0.1.1',
      description='Simple zabbix sender',
      author='Maksim Syomochkin',
      author_email='maksim77ster@gmail.com',
      url='https://github.com/maksim77/zsender',
      py_modules=['ZabbixSender'],
	  keywords='zabbix sender monitoring',
	  classifiers=[
			  'Development Status :: 2 - Pre-Alpha',
			  'License :: OSI Approved :: Apache Software License',
			  'Programming Language :: Python :: 3',
			  'Topic :: System :: Monitoring',
			  'Topic :: System :: Networking :: Monitoring',
			  'Topic :: System :: Systems Administration'
			  ]
      )
