""" 
Main app
"""

import sys
import argparse
import logging
from logging.handlers import RotatingFileHandler

# from pyfiglet import Figlet


def main():
    """
    Provides CLI
    """
    # welcome()
    args = get_args()

    logging.basicConfig(
        handlers=[
            RotatingFileHandler('logs/logs.log', maxBytes=100000, backupCount=10),
            logging.StreamHandler()],  # send log messages to console
        format='%(asctime)s %(levelname)s %(message)s',
        encoding='utf-8', 
        level=args.loglevel.upper()
    )

    while True:
        print("Type (exit) to exit")
        q = input("Query: \n")
        if q == "exit":
            sys.exit(0)
        else:
            print(f"You typed: {q}")

def get_args():
    parser = argparse.ArgumentParser(description='Cool Project')
    parser.add_argument( '-log',
                        '--loglevel',
                        default='info',
                        help='Provide logging level. Example --loglevel debug, default=warning' )
    args = parser.parse_args()
    return args

# def command(args):
#     """
#     Executes workflow for the given command
#     """
#     if args.command == "thing":
#         do_thing()
#     elif args.command == "other":
#         do_other()
#     else:
#         raise ValueError("Invalid Command. Valid options are 'thing' and 'other.")

# def welcome():
#     f = Figlet(font='slant')
#     print(f.renderText('Cool Project'))


###############################################
if __name__ == '__main__':
    main()
