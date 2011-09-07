"""
ProgressBar
author: Russell Miller
date: Sep 7 2011

Simply show progress during a test or script
"""

import sys

HEADING = ("** {title} **\n"
           "%:  10  20  30  40  50  60  70  80  90  100\n"
           "  +") 

class ProgressBar(object):
    def __init__(self, title):
        """
        :parameters:
         - title: Something to print out above the progress bar
        """
        self.title=title
        self.percent = 0

    def start(self):
        """
        Just get the title and heading onto the screen
        """
        sys.stdout.write(HEADING.format(title=self.title))

    def move_ten(self):
        """
        Increment the 'progress' by 10% visually.
        If the bar is full do nothing.
        """
        if self.percent < 90:
            sys.stdout.write("====")
            sys.stdout.flush()
            self.percent += 10
        elif self.percent == 90:
            sys.stdout.write("====+\n")
            sys.stdout.flush()
            self.percent += 10
