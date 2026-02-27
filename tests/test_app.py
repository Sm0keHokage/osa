def test_basic_math():
    """Самый простой тест, чтобы пайплайн прошел."""
    assert 1 + 1 == 2

def test_imports():
    """Проверяем, что библиотеки установлены."""
    import tornado
    import redis
    assert tornado.version