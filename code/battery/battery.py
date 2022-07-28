

from xmlrpc.client import boolean
from abc import abstractmethod

class battery():

    @abstractmethod
    def needs_service(self):
        pass
