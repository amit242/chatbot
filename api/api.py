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


print 'module name:', __name__


class ApiRunner(web.application):

    def run(self, port=8080):
        app = web.application(urls, globals())
        return web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', port))


if __name__ == "__main__":
    app = ApiRunner()
    app.run(port=8080)
