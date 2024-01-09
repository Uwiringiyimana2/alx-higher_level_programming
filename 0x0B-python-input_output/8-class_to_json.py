#!/usr/bin/python3
""" return dictionary description for JSON serialization"""


def class_to_json(obj):
    """return dictionary description for JSON serialization"""
    return obj.__dict__
