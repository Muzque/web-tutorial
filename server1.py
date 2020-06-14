from aiohttp import web


async def handler(request):
    return web.Response(text='Async server is running')


async def initialization():
    app = web.Application()
    app.add_routes([web.get('/', handler)])
    return app


web.run_app(initialization())
