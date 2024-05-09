from wsgiref.simple_server import make_server
from spyne.server.wsgi import WsgiApplication
from spyne.application import Application
from spyne.protocol.soap import Soap11
from service import CurrencyConverterService

def simple_cors_middleware(application):
    def wrapped(environ, start_response):
        def custom_start_response(status, response_headers, exc_info=None):
            response_headers.extend([
                ('Access-Control-Allow-Origin', '*'),
                ('Access-Control-Allow-Methods', 'POST, GET, OPTIONS'),
                ('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            ])
            return start_response(status, response_headers, exc_info)

        return application(environ, custom_start_response)
    return wrapped

# Define your SOAP application
application = Application(
    [CurrencyConverterService],
    'urn:currency_converter',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Wrap the application with the CORS middleware
wsgi_application = WsgiApplication(application)
wsgi_application_with_cors = simple_cors_middleware(wsgi_application)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, wsgi_application_with_cors)
    print("SOAP server starting...")
    server.serve_forever()
