from __future__ import absolute_import

from time import time


class CallContext(object):
    def __init__(self, call):
        self.call = call

    def __enter__(self):
        self.call.start()

    def __exit__(self, *exc_info):
        self.call.finish()


class CallResult(object):
    no_result = -1
    error = 1


class CallState(object):
    not_started = 0
    started = 1
    finished = 2


class Call(object):
    def __init__(self):
        self.start_time = None
        self.finish_time = None
        self.result = CallResult.no_result
        self.state = CallState.not_started

    def start(self):
        """
        Mark a call as started.
        """
        assert not self.state is CallState.finished

        self.state = CallState.started
        self.start_time = time()

    def finish(self, result=CallResult.no_result):
        """
        Mark a call as finished.
        """
        assert not self.state is CallState.finished

        self.state = CallState.finished
        self.finish_time = time()
        self.result = result
