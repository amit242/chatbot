import web
import json
import urllib
import urllib2
import base64

urls = (
    '/', 'hello',
    '', 'hello',
    '/bot/conversation', 'conversation',
    '/webhook', 'Webhook'
)

token = "EAAYnMQzpL0EBAFbEEXNxTn4u2uj63XpQgdbJZAngGmxcMz8gYmpWQZBfpPZBvQY1hfbu9RCyEzFeE707F0ZC9slzOp297DXeWHhsf6gDpGzo0ogR5pL9e2ZA1dO2dHTyTKVH5ItQY7ZCx0SJljH2adKIwJTbcMnBCEpkZAVSDQ2PwZDZD"

base_fb_url = "https://graph.facebook.com/v2.6/me/messages?access_token=" + token

headers = {"Content-Type": "application/json"}


_bot = None
verify_token = 'i_solemnly_swear_that_i_have_verified_this'

def addbot(bot):
    global _bot
    _bot = bot
    print 'adding bot', _bot


class Webhook:
    def GET(self):
        print 'get is called'
        print web.input()
        if web.input()['hub.verify_token'] == verify_token:
            return web.input()['hub.challenge']
        return 'Error, wrong validation token'

    def POST(self):
        print 'post is called'
        print 'input', web.input()

        print 'data', web.data()
        print 'data', type(web.data())

        data = json.loads(web.data())
        if data['object'] == 'page':
            for entry in data['entry']:
                for messaging_event in entry['messaging']:
                    if messaging_event.get('message'):
                        receive_message (messaging_event)





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

    def get_wsgi(self):
        return self.app.wsgifunc()

    def run(self, port=8080, val=False):
        print 'running...', port, val
        return web.httpserver.runsimple(self.app.wsgifunc(), ('0.0.0.0', port))


def receive_message(msg_event):
    sender_id = msg_event['sender']['id']
    msg_txt = msg_event['message']['text']
    fb_client = FBApiClient()
    fb_client.send_text_msg(sender_id, msg_txt)


class FBApiClient():

    def send_text_msg(self, recipient_id, msg_txt):
        message_data = {'recipient': {
                              'id': recipient_id
                            },
                            'message': {
                              'text': msg_txt
                            }
                        }
        self.call_send_api(message_data)

    def call_send_api(self, message_data):

        print message_data

        data = urllib.urlencode(message_data)
        request = urllib2.Request(base_fb_url, data)
        for key, value in headers.items():
            request.add_header(key, value)

        response = urllib2.urlopen(request)
        res = response.read()
        print 'call_send_api response:', res


if __name__ == "__main__":
    app = ApiRunner()
    app.run(port=8080)
