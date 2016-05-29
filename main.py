import sys, getopt
import api
from bot import Cal

def main(argv):
    _reloadbrain = False
    _offline = False
    try:
      opts, args = getopt.getopt(argv, "hro", ["help", "reload", "offline"])
    except getopt.GetoptError:
        print 'worng input, try: cal.py -r'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'cal.py\t-r\t\t:reload bot brain\n\t-o\t\t:run in offline'
            sys.exit()
        elif opt in ("-r", "--reload"):
            _reloadbrain = True
        elif opt in ("-o", "--offline"):
            _offline = True

    print 'reload:', _reloadbrain
    bot = Cal()
    bot.loadkernel(_reloadbrain)

    if _offline:
        # Press CTRL-C to break this loop
        while True:
            # print kernel.respond(raw_input("Enter your message >> "))
            message = raw_input("Enter your message to the bot: ")
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
        runner.run()

if __name__ == "__main__":
    main(sys.argv[1:])

