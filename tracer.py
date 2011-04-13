"""Example 1

This is what not to do; casting the exception to str will give you a tiny bit
of information, but not enough to do anything with.

"""

def whatever():
    try:
        foo = 'bar'
        baz = 1/0
    except Exception as e:
        print str(e)


if __name__ == '__main__':
    whatever()
