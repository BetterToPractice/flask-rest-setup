from . import core


@core.get("/foo")
def foo_view():
    return {
        'message': 'foo_bar',
    }
