"""Example 4

A final example, using the html() function in cgitb. This outputs an HTML
formatted exception page. It's much simpler than Django or Werkzeug's debug
pages, but it can be useful if you're sending HTML email or working on a tiny
script.

NOTE: cgitb.html() is also undocumented; cgitb.handler() will do the same
thing, and is documented, and doesn't require passing sys.exc_info().

"""

import cgitb
import os
import sys
import webbrowser


def whatever():
    try:
        foo = 'bar'
        baz = 1/0
    except Exception:
        html_output = cgitb.html(sys.exc_info())

        # Write a file so we can look at it
        open('error.html', 'w').write(html_output)
        # open a webbrowser to look at it
        webbrowser.open(
            'file:///%s' % os.path.join(os.getcwd(), 'error.html'))


if __name__ == '__main__':
    whatever()
