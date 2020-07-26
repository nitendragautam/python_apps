import logging.handlers
import os

class PIDFileHandler(logging.handlers.WatchedFileHandler):

    def __init__(self, filename, mode ='a', encoding=None, delay=0):
        filename=self._append



    def _append_pid_to_filename(self, filename):
        pid =os.getpid()
        path, extenstion =os.path.split(filename)
        file_name_format = '{0}-{1}{2}'.format(path,pid,extenstion)
        return file_name_format