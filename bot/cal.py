import aiml
import os

package_directory = os.path.dirname(os.path.abspath(__file__))
brainfile = package_directory + "/bot_brain.brn"
startupxmlfile = package_directory + "/aiml/std-startup.xml"

class Cal:
    def __init__(self):
        self.kernel = None

    def savebrain(self):
        self.kernel.saveBrain(brainfile)

    def reply(self, message):
        if self.kernel is not None:
            bot_response = self.kernel.respond(message)
            return bot_response
        else:
            print 'no kernel is set...'

    def loadkernel(self, _reloadbrain):
        print 'cal', package_directory
        self.kernel = aiml.Kernel()
        if os.path.isfile(brainfile) and not _reloadbrain:
            print('loading brain...')
            self.kernel.bootstrap(brainFile=brainfile)
        else:
            print ('learning and making brain again...', startupxmlfile)
            self.kernel.bootstrap(learnFiles=startupxmlfile, commands="reload aiml")
            self.kernel.saveBrain(brainfile)

