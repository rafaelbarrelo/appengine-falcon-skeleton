import falcon

class HelloResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nHello Falcon!!\n')

# falcon.API instances are callable WSGI apps
app = falcon.API()
# Resources are represented by long-lived class instances
hello = HelloResource()
# hello will handle all requests to the '/' or '/hello' URL path
app.add_route('/', hello)
app.add_route('/hello', hello)
