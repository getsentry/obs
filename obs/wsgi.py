from __future__ import absolute_import


class Obs(object):
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        iterable = None

        try:
            iterable = self.application(environ, start_response)
            for event in iterable:
                yield event
        finally:
            self._close(iterable)

    def _close(self, iterable):
        # wsgi spec requires iterable to call close if it exists
        # see http://blog.dscpl.com.au/2012/10/obligations-for-calling-close-on.html
        if not hasattr(iterable, 'close'):
            return
        if not callable(iterable.close):
            return
        iterable.close()
