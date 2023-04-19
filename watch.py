#!/usr/bin/env python3
# 	= ^ . ^ =

# Andrés Hernández - tonejito
# This script is released under the terms of the BSD license

# https://pythonhosted.org/watchdog/quickstart.html
# https://github.com/dloureiro/pandoc-watch/blob/master/pandocwatch.py

"""
Watch the 'CONTENT_DIR' directory for filesystem events and rebuild the site
"""

import sys
import time
import logging
import subprocess

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

COMMAND = "make"
CONTENT_DIR = "content"


class EventHandler(FileSystemEventHandler):
    """
    Handle filesystem events
    """

    # Perform action when a file is modified
    def on_modified(self, event):
        """
        Rebuild the site if a file is modified
        """
        # Run 'COMMAND' when a file is modified
        output = subprocess.run(
            COMMAND,
            stdin=None,
            input=None,
            capture_output=True,
            shell=False,
            check=True,
            text=True,
        )
        # Print STDOUT, STDERR and return code if neccessary
        if len(output.stdout) > 0:
            print(output.stdout.strip(), file=sys.stdout)
        if len(output.stderr) > 1:
            print(output.stderr.strip(), file=sys.stderr)
        if output.returncode != 0:
            print(str(output.returncode))


def main():
    """
    Set up and start watch logic
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Set directory to be watched for filesystem events
    path = CONTENT_DIR
    if len(sys.argv) > 1:
        path = sys.argv[1]

    # Set up observer watch logic
    logging_handler = LoggingEventHandler()
    filesystem_handler = EventHandler()
    observer = Observer()
    observed_watch = observer.schedule(filesystem_handler, path, recursive=True)
    observer.add_handler_for_watch(logging_handler, observed_watch)

    # Start observer loop
    logging.info(f"Watching files in '{path}'…")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
