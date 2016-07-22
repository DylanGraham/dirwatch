import logging
import inotify.adapters
import sys
import os


program_name = os.path.basename(__file__)
watch_dir = ''
_DEFAULT_LOG_FORMAT = '%(asctime)s ' + program_name + ' %(levelname)s - %(message)s'
_LOGGER = logging.getLogger(__name__)


def _usage():
    print('Usage: ' + program_name + ' /directory/to/watch')
    sys.exit(1)


def _configure_watch(args):
    global watch_dir

    if len(args) != 2:
        _usage()

    if os.path.isdir(args[1]):
        watch_dir = args[1].encode('utf-8')
    else:
        print('Not a directory: ' + args[1])
        _usage()


def _configure_logging():
    _LOGGER.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()

    formatter = logging.Formatter(_DEFAULT_LOG_FORMAT)
    ch.setFormatter(formatter)

    _LOGGER.addHandler(ch)


def _main():
    global watch_dir
    i = inotify.adapters.Inotify()

    i.add_watch(watch_dir)

    try:
        for event in i.event_gen():
            if event is not None:
                if event[1][0] == 'IN_CLOSE_WRITE':
                    (header, type_names, watch_path, filename) = event
                    _LOGGER.info("MASK->NAMES=%s WATCH-PATH=[%s] FILENAME=[%s]",
                                 type_names, watch_path.decode('utf-8'), filename.decode('utf-8'))
    finally:
        i.remove_watch(watch_dir)

if __name__ == '__main__':
    _configure_watch(sys.argv)
    _configure_logging()
    _main()
