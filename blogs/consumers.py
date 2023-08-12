# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
#
#
# class MessageConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         pass
#
#     async def receive(self, text_data):
#         pass
#
#     async def notify_new_message(self, event):
#         message = event['message']
#
#         # Отправка уведомления в браузер
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
