#Topic -Consumer
from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):

    def wedsocket_connect(self, event):
        # This handler is called when client initially opens a connection
        print('Websocket Connected .....')

    def websocket_receieve(self, event):
        # this handler is called when data recieved form client
        print('Message Receieved .....')


    def websocket_disconnect(self, event):
          # This handler is called when either one loses connection
        print('websocket disconnnected ....')

    
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket Connected ....')

    async def websocket_recieve(self, event):
        print('Message Receieved .....')


    async def websocket_disconnect(self, event):
        print('websocket disconnnected ....')
