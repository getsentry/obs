from __future__ import absolute_import

from .call import Call, CallContext


class Instrument(object):
    name = 'instrument'

    def __init__(self):
        self.calls = []

    def get_hooks(self):
        return []

    def enable(self):
        """
        Enables the instrument by injecting any hooks.
        """
        raise NotImplementedError

    def disable(self):
        """
        Disables the instrument by removing any hooks, if they exist.
        """

    def record(self, instrument, *args, **kwargs):
        """
        Returns a context manager for capturing calls.

        >>> with instrument.record('optional description'):
        >>>     make_function_call()
        """
        call = Call(*args, **kwargs)

        self.calls.append(call)

        return CallContext(call, *args, **kwargs)
