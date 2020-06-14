from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def handler(request):
    return web.Response(text='Async server is running')


@routes.get('/{name}/')
async def ask_name(request):
    name = request.match_info.get('name', '')
    age = request.rel_url.query.get('age', 0)
    return web.Response(text=f'Your name is {name} and age is {age}')


@routes.post('/{name}/')
async def add_name(request):
    data = await request.post()
    like = data.get('like')
    return web.Response(text=f'You like {like}')


async def initialization():
    app = web.Application()
    app.add_routes(routes)
    return app


web.run_app(initialization())
