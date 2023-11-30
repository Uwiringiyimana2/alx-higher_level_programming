#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
    """Prints all the names defined by the compiles module hidden_4.pyc"""
    import hidden_4

    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    names.sort()

    for name in names:
        print(name)
