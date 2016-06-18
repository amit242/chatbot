import main
import sys


def get_app():
    return main.main(sys.argv[1:], True)


wsgiapp = get_app()