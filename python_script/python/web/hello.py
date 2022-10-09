# hello.py

def application(environ, start_response):
    # '200 OK', [('Content-Type', 'text/html')]
    start_response('200 ok',[('Content-Type', 'text/html')])
    return [b'hello world']