import web


urls = (
    '/', 'hello',
    '', 'hello'
)

class hello:
    def GET(self):
        return {'msg': 'it works'}


app = web.application(urls, globals())

wsgiapp = app.wsgifunc()