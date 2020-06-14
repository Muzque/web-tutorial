import aiohttp
import asyncio

url = 'http://localhost:8080/myname/'


async def post_like(url):
    async with aiohttp.ClientSession() as session:
        data = {'like': 'Test'}
        post_data = await session.post(url, data=data)
        print(await post_data.text())


asyncio.run(post_like(url))
