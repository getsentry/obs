from __future__ import absolute_import

from time import time


class Hook(object):
    def __init__(self, path, name=None):
        self.path = path
        self.name = name or path.rsplit('.', 1)[-1]

    def patch(self):
        """
        Patch the target path to hijack calls.
        """
        raise NotImplementedError

    def unpatch(self):
        """
        Remove the patch, if applied.
        """
        raise NotImplementedError

    def execute(self, *args, **kwargs):
        """
        Execute the original function.
        """
        raise NotImplementedError

    def on_call(self, instrument, *args, **kwargs):
        with instrument.record():
            self.call_original(*args, **kwargs)
