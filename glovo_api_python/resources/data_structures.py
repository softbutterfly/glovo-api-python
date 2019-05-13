from dataclasses import dataclass
from typing import Any


class AddressType:
    """Addresss type choices.
    PICKUP or DELIVERY depending on what the courier is expected to do at this
    address."""
    PICKUP = 'pickup'
    DELIVERY = 'delivery'


@dataclass
class Address:
    """Each of the points that are part of the order. Right now you can only
    create two-point orders.

    FIELD           DESCRIPTION
    lat             Latitude of the address.
    lon             Longitude of the address.
    type            PICKUP or DELIVERY depending on what the courier is
                    expected to do at this address.
    label           Street and number (e.g. 21 Baker St).
    details         Floor / appartment (e.g. 2nd Floor or blue button of the
                    intercom). Optional.
    contactPhone    Phone of the sender / recipient at that address. Optional.
    contactPerson   Name of the sender / recipient at that address. Optional."""

    lat: float
    lon: float
    type: str
    label: str
    details: str
    contactPhone: str
    contactPerson: str


class OrderType:
    """State of the order

    STATE           DESCRIPTION
    SCHEDULED       The order will be activated on scheduleTime.
    ACTIVE          The order is either being delivered or about to be.
    DELIVERED       The delivery has finished succesfully.
    CANCELED        The order is canceled and it wont be delivered."""

    SCHEDULED = 'scheduled'
    ACTIVE = 'active'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'


@dataclass
class Order:
    """Order

    FIELD           DESCRIPTION
    id              Id of the order.
    description     Description detailing the package to be delivered
    creationTime    Unix time in seconds of the order creation time.
    scheduleTime    Unix time in seconds of the scheduled activation time of
                    the order. Optional.
    addresses       Ordered list of addresses(pickups and deliveries) of the
                    order. Usually your orders will have one PICKUP address
                    and one DELIVERY address.
    state           Current state of the order (one of SCHEDULED, ACTIVE,
                    DELIVERED, CANCELED)."""

    id: str
    description: str
    creationTime: int
    scheduleTime: int
    addresses: Address
    state: str


@dataclass
class WorkingTime:
    """WorkingTimes specify the activity hours of a WorkingArea,

    FIELD           DESCRIPTION
    opening         Starting time of the active time range.
    duration        Duration in minutes of the time range.
    """

    opening: int
    duration: int


@dataclass
class WorkingArea:
    """The WorkingArea is the geographical space where Glovo can pick-up and
    deliver an order during certain hours of the day. Cross-WorkingArea orders
    are not supported.

    FIELD           DESCRIPTION
    code            Id of the delivery area(e.g. BCN, MAD, BUE).
    polygons        List of encoded polylines where a package can be picked-up or delivered.
    workingTime     WorkingTime during which this area is active.

    """
    code: str
    polygons: Any
    workingTime: WorkingTime
