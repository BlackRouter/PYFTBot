## PyTeleBot: Telegram Proxy Bot api handler

![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)

### Install
To Install it:

    $ pip install PyFarsi-TBot
	or
	$ pip3 install PyFarsi-TBot
### Usage

```python

from PYFTBot.PYFTBot import *

Get method:

print(getbot("981962025:AAFVC7vhFg6TI7IXRHzFVO2YczBuLC_WcAg","getUpdates").decode('utf8'))
	
Post method:

print(postbot("981962025:AAFVC7vhFg6TI7IXRHzFVO2YczBuLC_WcAg","sendMessage","{\"chat_id\":\"972274985\",\"text\":\"HelloWorld\"}").decode('utf8'))
```

### Info
* Telegram Group ([PyFarsi](https://t.me/PyFarsi))
* Developer ([Javad](https://t.me/Ja7adR))


