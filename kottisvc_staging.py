# uncomment the next import line to get print to show up or see early
# exceptions if there are errors then run
#   python -m win32traceutil
# to see the output
# import win32traceutil
import win32serviceutil

PORT_TO_BIND = 8080
CONFIG_FILE = 'production_staging.ini'
SERVER_NAME = 'localhost'

SERVICE_NAME = "kotti_project_staging"
SERVICE_DISPLAY_NAME = "kotti_project_staging"
SERVICE_DESCRIPTION = """This will be displayed as a description \
of the serivice in the Services snap-in for the Microsoft \
Management Console."""


class PyWebService(win32serviceutil.ServiceFramework):
    """Python Web Service."""

    _svc_name_ = SERVICE_NAME
    _svc_display_name_ = SERVICE_DISPLAY_NAME
    _svc_deps_ = None        # sequence of service names on which this depends
    # Only exists on Windows 2000 or later, ignored on windows NT
    _svc_description_ = SERVICE_DESCRIPTION

    def SvcDoRun(self):
        import cherrypy
        from cherrypy import wsgiserver
        from pyramid.paster import get_app
        from pyramid.paster import setup_logging
        import os

        path = os.path.dirname(os.path.abspath(__file__))

        os.chdir(path)

        app = get_app(CONFIG_FILE)
        setup_logging(CONFIG_FILE)

        # See http://tools.cherrypy.org/wiki/WindowsService
        # See http://stackoverflow.com/questions/11982438/cherrypy-server-errors-log
        # If you have to debug cherrypy specific errors
        # enable the following option:
        #    'log.error_file': os.path.join(path, 'cherrypy_error.log'),
        cherrypy.config.update({
            'engine.autoreload.on': False,
            })
        self.server = wsgiserver.CherryPyWSGIServer(
            ('127.0.0.1', PORT_TO_BIND), app,
            numthreads=30,
            server_name=SERVER_NAME)

        self.server.start()

    def SvcStop(self):
        self.server.stop()


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PyWebService)
