# pysystembolaget
Python wrapper for Systembolaget API. An API key is needed to use this library, get it through the link https://api-portal.systembolaget.se/products/Open%20API. Right now it is only possible to get information about a product through its product id, the wrapper will in time include the complete API provided by Systembolaget.

## Install
```
python3 setup.py install
```

## Example
```
import pysystembolaget
import pprint

api_key = 'YOUR API KEY'

systembolaget = pysystembolaget.Systembolaget(api_key)
response = systembolaget.product_get(508314)

pprint.pprint(response)
```

## Coverage
```
coverage erase
coverage run -m pytest
coverage xml
coverage report
```

## Create TAGS
```
find ./pysystembolaget -type f -name '*.py' | xargs etags
```