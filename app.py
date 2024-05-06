# write a simple aiohttp based webserver that does the following:
# 1. returns a simple hello world with the source and target ip addresses with the current timestamp

from aiohttp import web
import socket
import datetime

async def handle(request):
    source_ip = request.transport.get_extra_info('peername')[0]
    target_ip = request.transport.get_extra_info('sockname')[0]
    now = datetime.datetime.now()
    text = f'Hello World! Source IP: {source_ip}, Target IP: {target_ip}, Timestamp: {now}'
    return web.Response(text=text)

app = web.Application()

app.router.add_get('/', handle)

web.run_app(app, host='0.0.0.0', port=8080)
