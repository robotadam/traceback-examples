"""Example 3

cgitb can be considered a level on top of traceback; this uses the undocumented
function text() to print an extra bit of detail. it also prints out details on
the exception object itself, including any arguments. This can be useful if you
add any details.

"""
import cgitb
import sys


def whatever():
    try:
        foo = 'bar'
        baz = 1/0
    except Exception:
        print cgitb.text(sys.exc_info())


if __name__ == '__main__':
    whatever()
