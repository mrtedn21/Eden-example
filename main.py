import uvloop
import asyncio
from users import controllers
from chats import controllers
from martin_eden.core import Backend


if __name__ == '__main__':
    uvloop.install()
    backend = Backend()
    asyncio.run(backend.main(), debug=True)
