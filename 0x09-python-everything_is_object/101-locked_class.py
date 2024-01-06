#!/usr/bin/python3


class LockedClass:
    """
    Prevent user from instantiating new LockedClass attributes
    for anything else but attributes called 'first_name'
    """
    __slots__ = ["first_name"]
