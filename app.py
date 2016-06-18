import web


urls = (
    '/', 'hello',
    '', 'hello'
)

class hello:
    def GET(self):
        return {'msg': 'it works'}


app = web.application(urls, globals())



def myapp():
    print 'here i am'
    wsgiapp = app.wsgifunc()
    return wsgiapp


xx = myapp()