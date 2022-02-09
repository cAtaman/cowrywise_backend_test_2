from src.admin.wsgi import app as admin_app
from src.client.wsgi import app as client_app

#
# if __name__ == '__main__':
#     from werkzeug.middleware.dispatcher import DispatcherMiddleware
#     from werkzeug.serving import run_simple
#
#     # this next block mounts admin_app at the "/admin" route
#     # on client_app
#     application = DispatcherMiddleware(client_app, {
#         '/admin': admin_app
#     })
#
#     # this runs the combined app
#     run_simple(
#         hostname='0.0.0.0',
#         port=1759,
#         application=application,
#         use_reloader=True,
#         use_debugger=True,
#         use_evalex=True
#     )
