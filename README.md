# py3status-modules

Modules for py3status

![screenshot](/pics/py3status-modules-1.png)  
![screenshot](/pics/py3status-modules-2.png)

## Requirements

All of these modules require `python-requests`.

#### on archlinux
`# pacman -S python-requests`


## reddit.py
Displays your reddit link and comment karma.  
On left click, it opens your reddit overview page.

#### usage:
Before using this module, you need to set your reddit username in the `self.user` variable like:  
`self.user='l4than-d3vers'`

## bitcoin.py
Displays the current exchange value of bitcoin in USD from [bitstamp.net](https://www.bitstamp.net/)
On left click, it opens [bitcoinity.org/markets](http://bitcoinity.org/markets)

## btcd-conncount.py
Displays the total connection count for bitcoind.
On click, switches between displaying total and displaying inbound and outbound connections.
