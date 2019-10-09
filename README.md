# Network Scanner

MAC Network Scanner for Unix/Linux.

## The algorithm

The program sends ARP requests to the broadcast MAC address in the network, then saves all responses, parses them, and make a list of dictionaires containing both the MAC and IP of all devices in the same network.

## Clone

> Clone this repo to your local machine using https://github.com/rsoares10/network-scanner.git

## Usage
```
usage: network-scanner [-h] [-t TARGET]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Specify IP target range
```

## Example

```
# Scan entire local network
 ./network-scanner.py -t 10.0.2.1/24

# Output

IP			    MAC Address
-----------------------------------------
10.0.2.1		52:54:00:12:35:00
10.0.2.2		52:54:00:12:35:00
10.0.2.3		08:00:27:d4:64:5b
```

> _Note: It might be required root privileges for this script to work._

## Prerequisites
- Python 2.7

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Support
Reach out to me at one of the following places!
- Facebook at https://www.facebook.com/max.monteiro.520
- Gmail at rsoares.monteiro10@gmail.com