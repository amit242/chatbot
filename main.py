import sys, getopt
import api
from bot import Cal


def main(argv, isServer=False):
    _reloadbrain = False
    _offline = False
    try:
        opts, args = getopt.getopt(argv, "hro", ["help", "reload", "offline"])

    except getopt.GetoptError:
        print 'worng input, try: cal.py -r'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'main.py\t-r\t\t:reload bot brain\n\t-o\t\t:run in offline mode'
            sys.exit()
        elif opt in ("-r", "--reload"):
            _reloadbrain = True
        elif opt in ("-o", "--offline"):
            _offline = True

    #print 'reload:', _reloadbrain
    bot = Cal()
    bot.loadkernel(_reloadbrain)

    if _offline:
        # Press CTRL-C to break this loop
        while True:
            # print kernel.respond(raw_input("Enter your message >> "))
            message = raw_input("You: ")
            sys.stdout.write('cal:')
            if message == "quit":
                exit()
            elif message == "save":
                bot.savebrain()
            else:
                bot_response = bot.reply(message)
                print bot_response
    else:
        runner = api.ApiRunner()
        api.addbot(bot)
        if not isServer:
            runner.run(8081, True)
        else:
            return runner.get_api()

print 'module name XX:', __name__
if __name__ == "__main__" or __name__ == "main":
    main(sys.argv[1:])


def run_gunicorn():
    return main(sys.argv[1:], True)

