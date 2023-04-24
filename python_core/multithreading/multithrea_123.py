from threading import Thread


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon)
        self._return = None

    def run(self):
        try:
            if self._target:
                self._return = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

    def join(self,timeout=None):
        Thread.join(self,timeout)
        return self._return