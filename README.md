# IP-Info
Python module to get information on an IP address using [whatismyipaddress.com](https://whatismyipaddress.com).

## Installation

```
pip install git+https://github.com/DrGFreeman/IP-Info
```

## Usage

Basic usage with the `ipinfo.ipinfo` function:
```python
>>> from ipinfo import ipinfo
>>> ipinfo('172.217.1.174')
{'Hostname:': 'yyz10s04-in-f14.1e100.ne', 'ASN:': 15169, 'ISP:': 'Google', 'Organization:': 'Google', 'Type:': 'Corporate', 'Continent:': 'North America', 'Country:': 'United States', 'State/Region:': 'Not available', 'City:': 'Not available', 'Latitude:': 37.751, 'Longitude:': -97.822}
```

Using the `IpWimia` class allows to access the different fields as class attributes:
```python
>>> from ipinfo import IpWimia
>>> ip = IpWimia('89.238.154.250')
>>> ip.hostname
'no-mans-land.m247.com'
>>> ip.isp
'M247 L'
>>> ip.country
'United Kingdom'
>>> ip.state_region
'England'
>>> ip.city
'London'
>>> ip.latitude, ip.longitude
(51.5426, -0.2449)
>>> ip.ip
'89.238.154.250'
```

The complete dictionary is available in the `info` class attribute:
```python
>>> ip.info
{'Hostname:': 'no-mans-land.m247.com', 'ASN:': 9009, 'ISP:': 'M247 L', 'Organization:': 'M247 L', 'Type:': 'Not available', 'Continent:': 'Europe', 'Country:': 'United Kingdom', 'State/Region:': 'England', 'City:': 'London', 'Latitude:': 51.5426, 'Longitude:': -0.2449}
```