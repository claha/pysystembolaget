# pysystembolaget
Python wrapper for Systembolaget API. An API key is needed to use this library, get it through the link https://api-portal.systembolaget.se/products/Open%20API. Right now it is only possible to get information about a product through its product id, the wrapper will in time include the complete API provided by Systembolaget.

## Install
```
python3 setup.py install
```

## Coverage
```
coverage erase
coverage run -m pytest
coverage xml
coverage report
```

## Example
```
import pysystembolaget
import pprint

pysystembolaget.set_ocp_apim_subscription_key(key)
response = pysystembolaget.Product.get(508314)

pprint.pprint(response)
```

## Create TAGS
```
find ./pysystembolaget -type f -name '*.py' | xargs etags
```