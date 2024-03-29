import aiohttp # don't forget to pip install aiohttp
import asyncio
import async_timeout
import time

async def fetch_page(session, url):
    start = time.time()
    async with async_timeout.timeout(10):
        # wait max 10 sec for the response
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return response.status

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


if __name__ == '__main__':

    def main():
        loop = asyncio.get_event_loop()
        urls = [
            'http://google.com',
            'http://example.com',
            'http://cnn.com'
        ]
        start = time.time()
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        print(f'Total took {time.time() - start}')
        for page in pages:
            print(page)

    main()