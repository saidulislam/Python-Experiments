import aiohttp # don't forget to pip install aiohttp
import asyncio
import async_timeout
import time


async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with async_timeout.timeout(10):
            # wait max 10 sec for the response
            async with session.get(url) as response:
                print(f'Response Tiime: {time.time() - page_start} >>>> Status: {response.status} >>>> {url}')
                return response.status


loop = asyncio.get_event_loop()

if __name__ == '__main__':
    URL = input("Enter a URL to hit: ")
    thread_count = int(input("How many threads: "))

    tasks = [fetch_page(URL) for i in range(thread_count)]
    start = time.time()
    loop.run_until_complete(asyncio.gather(*tasks))

    print(f'Total Execution Time : {time.time() - start}')