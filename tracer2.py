import traceback


def whatever():
    try:
        foo = 'bar'
        baz = 1/0
    except Exception:
        print traceback.format_exc()


if __name__ == '__main__':
    whatever()

