# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from blogs.routing import websocket_urlpatterns
# from portfolio_backend.asgi import django_asgi_app
#
# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ),
# })
