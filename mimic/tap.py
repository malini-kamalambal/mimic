"""
Twisted Application plugin for Mimic
"""
from twisted.application.strports import service
from twisted.application.service import MultiService
from twisted.web.server import Site
from twisted.python import usage
from mimic.core import MimicCore
from mimic.resource import MimicRoot


class Options(usage.Options):
    """
    Options for Mimic
    """
    optParameters = [['listen', 'l', '8900', 'The endpoint to listen on.']]


def makeService(config):
    """
    Set up the otter-api service.
    """
    s = MultiService()
    core = MimicCore()
    root = MimicRoot(core)
    site = Site(root.app.resource())
    site.displayTracebacks = False
    service(config['listen'], site).setServiceParent(s)
    return s
