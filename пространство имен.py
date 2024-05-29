def test_function(x):
    a = x * 4

    def inner_function(x):
        nonlocal a
        a = x / 2
        if a % 2 == 0:
            print('Я в области видимости функции тест функтион')
        else:
            print('неправильно')

    inner_function(x)
    return a


test_function(4)
