from distutils.core import setup
setup(
  name = 'PyFarsi-TBot',        
  packages = ['PyFTBot'],  
  version = '1.0',     
  license='MIT',     
  description = 'Telegram Proxy API Handler', 
  author = 'Javad Rajabzade',                
  author_email = 'ja7adr@gmail.com',  
  url = 'https://github.com/BlackRouter/PyFTBot',  
  download_url = 'https://github.com/BlackRouter/PyFTBot/archive/1.0.zip',   
  keywords = ['Telegram', 'TelegramBot', 'Proxy'],  
  install_requires=[           
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)