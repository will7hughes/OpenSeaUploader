is_debug = False

def debug(message, title="Debug - "):
    if is_debug:
        print("\t" + title + message)