 <img src="https://www.ul.se/Static/gfx/ul-logo.jpg" width="200">

# About

Unofficial python client for travel information regarding [UL](https://ul.se).

For public transport around Uppsala.


# Installation

```python
pip3 install git+https://github.com/Adddrian/ul-api-python-client#egg=ul_api_client

```

# Usage

### import lib
```python
from ul_api_client import UlClient

```

### all_stops

Get a list of all stops

```python
UlClient.all_stops()
```


### stop_search

Search for a stop

```python
UlClient.stop_search("kantorsgatan")
```

### journey_search

```python
UlClient.journey_search()
```

### journey_parts

```python
UlClient.journey_parts()
```
