import asyncio

from aioconsole import ainput

from constants import DISCONNECT, HOST, MAXBYTES, PORT


class Client:
    def __init__(self, server_host: str = HOST, server_port: int = PORT):
        self.server_host = server_host
        self.server_port = server_port
        self.disconnect: bool = False

    async def start_client(self):
        self.reader, self.writer = await asyncio.open_connection(
            self.server_host, self.server_port)
        await asyncio.gather(self.write_msg(), self.read_msg())

    async def write_msg(self):
        while True:
            message = await ainput('')
            if message == DISCONNECT:
                print('<Отключение от сервера...>')
                self.disconnect = True
                self.writer.close()
                break
            self.writer.write(message.encode())
            await self.writer.drain()
            await asyncio.sleep(0.1)  # Needed for task changing

    async def read_msg(self):
        while True:
            if self.disconnect:
                break
            if msg_to_read := await self.reader.read(MAXBYTES):
                print(msg_to_read.decode())
                await asyncio.sleep(0.1)  # Hope this will help u to run code
        self.writer.close()


if __name__ == '__main__':
    client = Client()
    asyncio.run(client.start_client())

# Николай, видел ваше замечание, что код не запускается
# Данную ошибку удалось воспроизвести только на старших вресиях Python
# На Python 3.11 код работает стабильно
# В проекте лежит dockerfile
# Попробуйте запустить контейнер, всё должно заработать
# В README добавил описание запуска проекта
