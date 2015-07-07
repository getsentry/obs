# Obs

An observer.

## Goals

- Plugged in via a WSGI middleware or a basic command (which would just look for the middleware).
- Local instrumentation for various network calls.
- Ability to capture data from instrumented code when an AJAX call (or in theory, a remote RPC) happens.
- Pluggable remote storage for instrumented data (in-memory, memcache, redis).

### Future

- Deeper introspection with things such as memory and other machine data.

## Instrument Spec

```python

# Create a basic Hook which is responsible for
# recording the description of calls
class RedisHook(Hook):
    def on_call(self, instrument, *args, **kwargs):
        with instrument.record('description'):
            self.execute(*args, **kwargs)


# Create an instrument which is responsible for
# describing hooks
class RedisInstrument(Instrument):
    name = 'redis'

    def get_hooks(self):
        return [
            RedisHook('redis.Client.execute'),
        ]

# Wrap your application
obs = Obs(application)

# register the Instrument with the Obs instance
obs.register(RedisInstrument)
```
