""""""
import sys


# HELLO_WORLD = """<html>
# <head>
#     <title>PythonAnywhere hosted web application</title>
# </head>
# <body>
# <h1>Hello, World!</h1>
# <p>
#     This is the default welcome page for a
#     <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>
#     hosted web application.
# </p>
# <p>
#     Find out more about how to configure your own web application
#     by visiting the <a href="https://www.pythonanywhere.com/web_app_setup/">web app setup</a> page
# </p>
# </body>
# </html>"""


# def application(environ, start_response):
#     if environ.get('PATH_INFO') == '/':
#         status = '200 OK'
#         content = HELLO_WORLD
#     else:
#         status = '404 NOT FOUND'
#         content = 'Page not found.'
#     response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
#     start_response(status, response_headers)
#     yield content.encode('utf8')


path = '/home/rueben/flask_stonk_dash'
if path not in sys.path:
   sys.path.append(path)

from flask_app import app as application
