import web


urls = (
    '/bot/talk', 'talk',
    'bot/save'
)

_bot = None

def addbot(bot):
    global _bot
    _bot = bot
    print 'adding bot', _bot


class talk:
    def POST(self):
        #print web.ctx.env.get('HTTP_AUTHORIZATION')
        # TODO: basic security
        #print web.data()
        human_msg = web.input()
        print 'human:',human_msg.msg
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
