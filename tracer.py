def whatever():
    try:
        foo = 'bar'
        baz = 1/0
    except Exception as e:
        print str(e)


if __name__ == '__main__':
    whatever()
