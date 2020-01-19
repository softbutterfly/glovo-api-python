[![Python Versions](https://img.shields.io/pypi/pyversions/glovo-api-python.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI Version](https://img.shields.io/pypi/v/glovo-api-python.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/glovo-api-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/glovo-api-python.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/glovo-api-python/)

[![Build Status](https://travis-ci.org/softbutterfly/glovo-api-python.svg?branch=master)](https://travis-ci.org/softbutterfly/glovo-api-python)
[![codecov](https://codecov.io/gh/softbutterfly/glovo-api-python/branch/master/graph/badge.svg)](https://codecov.io/gh/softbutterfly/glovo-api-python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1787644ed8524433b9466f74d24b44d2)](https://www.codacy.com/gh/softbutterfly/glovo-api-python?utm_source=github.com&utm_medium=referral&utm_content=softbutterfly/glovo-api-python&utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/1787644ed8524433b9466f74d24b44d2)](https://www.codacy.com/gh/softbutterfly/glovo-api-python?utm_source=github.com&utm_medium=referral&utm_content=softbutterfly/glovo-api-python&utm_campaign=Badge_Coverage)

[![Stars](https://img.shields.io/github/stars/softbutterfly/glovo-api-python?logo=github)](https://github.com/softbutterfly/glovo-api-python/)
[![License](https://img.shields.io/pypi/l/glovo-api-python.svg?color=blue)](https://github.com/softbutterfly/glovo-api-python/blob/master/LICENSE.txt)

# Glovo Python Business API

Create, retrieve and track your Glovo orders trough their Business API.

## Requirements

This package requires at least

- requests 2.21.0
- python 3.7

This package was not tested with prior versions of these packages but it can works as well.

## Install

You can install via pip. Run the following command:

```bash
pip install glovo-api-python
```

## Credentials

Create an account in Glovo (it can be created from the App). This api **needs a credit card associated to your account**. You can add one from your app and it will be used automatically for any order. In order to get your API credentials you should login in the desired environment and go to _Credentials_ section on your profile.

- [B2B Production](https://business.glovoapp.com/dashboard/profile)
- [B2B Sandbox/Test](https://business.testglovo.com/dashboard/profile)

Example `ApiKey` & `ApiSecret`:

```python
api_key = '155761234946286'
api_secret = '767b4e2f48e4412d95a6eb1234bdc78b'
```

## Usage

Simple usage looks like:

### Initialize client

```python
from glovo_api_python.client import Client

api_key = 'sample_api_key'
api_secret = 'sample_api_secret'

client = Client(api_key, api_secret)
```

### Get working areas

From [glovo docs](https://api-docs.glovoapp.com/b2b/index.html#getworkingareas)

```python
woking_areas = client.working_area.list()
print(working_areas)
# Will show this
# {
#     'status': 200,
#     'data': {
#         'workingAreas': [
#             {
#                 'code': 'ABJ',
#                 'polygons': [
#                     '<ENCODED POLYLINE>',
#                     '<ENCODED POLYLINE>'
#                 ],
#                 'workingTime': {
#                     'from': '09:00',
#                     'duration': 120
#                 }
#             }
#             <OTHER WORKING AREAS>
#         ]
#     }
# }
```

### Estimate order price

From [glovo docs](https://api-docs.glovoapp.com/b2b/index.html#estimateorderprice)

```python
pickup_address = {
    "lat": -12.0563673,
    "lon": -76.9733736,
    "type": "PICKUP",
    "label": "Avenida los Cipreses, 140",
    "details": "Edificio Orbes, Piso 3, Oficina de Productos Angel Breña",
    "contactPhone": None,
    "contactPerson": None
}

delivery_address = {
    "lat": -12.055013,
    "lon": -77.03845849999999,
    "type": "DELIVERY",
    "label": "Avenida Inca Garcilaso de la Vega, 1250",
    "details": "Oficina 511",
    "contactPhone": None,
    "contactPerson": None
}

estimates_order_price = client.order.estimate({
    "scheduleTime": None,
    "description": "Some useful description",
    "addresses": [
        pickup_address,
        delivery_address
    ]
})
print(estimates_order_price)
# Will show this
# {
#     'status': 200,
#     'data': {
#         'total': {
#             'amount': 1260,
#             'currency': 'PEN'
#         }
#     }
# }
```

### Create order

From [glovo docs](https://api-docs.glovoapp.com/b2b/index.html#createorder)

```python
pickup_address = {
    "lat": -12.0563673,
    "lon": -76.9733736,
    "type": "PICKUP",
    "label": "Avenida los Cipreses, 140",
    "details": "Edificio Orbes, Piso 3, Oficina de Productos Angel Breña",
    "contactPhone": None,
    "contactPerson": None
}

delivery_address = {
    "lat": -12.055013,
    "lon": -77.03845849999999,
    "type": "DELIVERY",
    "label": "Avenida Inca Garcilaso de la Vega, 1250",
    "details": "Oficina 511",
    "contactPhone": None,
    "contactPerson": None
}

placed_order = client.order.create({
    "scheduleTime": 12344566, # Set to None for immediate order
    "description": "Some useful description",
    "addresses": [
        pickup_address,
        delivery_address
    ]
})

print(placed_order)
# Will show this
# {
#     'status': 200,
#     'data': {
#         "id": 123456789,
#         "state": "SCHEDULED",
#         "scheduleTime": 12344566,
#         "description": "A 30cm by 30cm box",
#         "addresses": [
#             <PICKUP ADDRESS>,
#             <DELIVERY ADDRESS>,
#         ]
#     }
# }
```

### Retrieve order

From [glovo docs](https://api-docs.glovoapp.com/b2b/index.html#retrieveorder)

```python
order_id = 32678866
placed_order = client.order.read(order_id)

print(placed_order)
# Will show this
# {
#     'status': 200,
#     'data': {
#         'scheduleTime': None,
#         'description': 'Necesito enviar una llave',
#         'addresses': [
#             <PICKUP ADDRESS>,
#             <DELIVERY ADDRESS>,
#         ],
#         'id': '32678866',
#         'state': 'DELIVERED',
#         'reference': None
#     }
# }
```

### Get order tracking

From [glovo docs](https://api-docs.glovoapp.com/b2b/index.html#getordertracking)

```python
order_id = 32678866
tracking = client.order.tracking(order_id)
print(tracking)
# Will show this
# {
#     "status": 200,
#     "data": {
#         "lat": -12.0704984,
#         "lon": -76.9816546
#     }
# }
```

### Get courier contact

From [glovo docs](https://api-docs.glovoapp.com/b2b/index.html#getcouriercontact)

```python
order_id = 32678866
courier_contact = client.order.courier_contact(order_id)
print(courier_contact)
# Will show this
# {
#     "status": 200,
#     "data": {
#         "courierName": "Courier names",
#         "phone": "+99999999999"
#     }
# }
```

### Get orders

From [glovo docs](https://api-docs.glovoapp.com/b2b/index.html#getorders)

```python
start=12344566
end=12544566
order_list = client.order.list(data={'from': start, 'to': end})
print(order_list)
# Will show this
# {
#     "status": 200,
#     "data": [
#         {
#             "scheduleTime": null,
#             "description": "Useful description!",
#             "addresses": [
#                 <PICKUP ADDRESS>,
#                 <DELIVERY ADDRESS>,
#             ],
#             "id": "40304538",
#             "state": "DELIVERED",
#             "reference": null
#         },
#         <OTHER ORDERS>
#     ]
# }
```

### Cancel order

From [glovo docs](https://api-docs.glovoapp.com/b2b/index.html#cancelorder)

```python
order_id = 32678866
canceled_order = client.order.cancel(order_id)
print(courier_contact)
# Will show this
# {
#     status: 200,
#     data: {
#         "id": 32678866,
#         "state": "CANCELED",
#         "scheduleTime": 12344566,
#         "description": "A 30cm by 30cm box",
#         "addresses": [
#             <PICKUP ADDRESS>,
#             <DELIVERY ADDRESS>,
#         ]
#     }
# }
```
