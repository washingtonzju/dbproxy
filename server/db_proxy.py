#!/usr/bin/python
""" Secure database query and manage based on gevent.pywsgi """

from gevent import pywsgi

def db_proxy(env, start_response):
    
    if env['PATH_INFO'] == '/':
        """ Parsing POST Method Information"""
        length= int(env['CONTENT_LENGTH'])
        start_response('200 OK', [('Content-Type', 'text/html')])
        sui = env['wsgi.input'].read(length)
        return [sui+"\n"]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return ['<h1>Not Found</h1>']

        
if __name__ == "__main__":
    
    server = pywsgi.WSGIServer(('0.0.0.0', 8443), db_proxy, keyfile='server.key', certfile='server.crt')
    
    server.serve_forever()
    
    
