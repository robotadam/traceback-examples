import cgitb
import os
import sys
import webbrowser


def whatever():
    try:
        foo = 'bar'
        baz = 1/0
    except Exception:
        open('error.html', 'w').write(cgitb.html(sys.exc_info()))
        webbrowser.open(
            'file:///%s' % os.path.join(os.getcwd(), 'error.html'))


if __name__ == '__main__':
    whatever()




