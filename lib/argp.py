#!/usr/bin/env python

import argparse


class VariableDestAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, choices=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        if choices is not None:
            raise ValueError("choices not allowed")
        if "dests" not in kwargs:
            raise ValueError("dests is required")
        dests = kwargs.pop("dests")
        choices = set(v for dest in dests.values() for v in dest)
        self._dests = dests
        kwargs.setdefault("default", None)
        kwargs["nargs"] = "?"
        super(VariableDestAction, self).__init__(option_strings, dest, choices=choices, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        for k, v in self._dests.items():
            if values in v:
                setattr(namespace, k, values)
