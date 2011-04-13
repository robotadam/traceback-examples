import cgitb
import sys


def whatever():
    try:
        foo = 'bar'
        baz = 1/0
    except Exception:
        import pdb;pdb.set_trace()
        print cgitb.text(sys.exc_info())


if __name__ == '__main__':
    whatever()


