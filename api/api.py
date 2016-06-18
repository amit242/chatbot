import web


urls = (
    '/', 'hello',
    '', 'hello',
    '/bot/conversation', 'conversation',
    'bot/save'
)

_bot = None


def addbot(bot):
    global _bot
    _bot = bot
    print 'adding bot', _bot


class hello:
    def GET(self):
        return {'msg': 'it works'}


class conversation:
    def POST(self):
        #print web.ctx.env.get('HTTP_AUTHORIZATION')
        # TODO: basic security
        #print web.data()
        human_msg = web.input()
        print 'human:', human_msg.msg
        global _bot
        output = _bot.reply(human_msg.msg)
        print 'bot:', output
        return output


class ApiRunner(web.application):
    def __init__(self):
        self.app = web.application(urls, globals())

    def get_api(self):
        return self.app

    def run(self, port=8080, val=False):
        print 'running...', port, val
        return web.httpserver.runsimple(self.app.wsgifunc(), ('0.0.0.0', port))


if __name__ == "__main__":
    app = ApiRunner()
    app.run(port=8080)
