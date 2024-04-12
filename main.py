import os
import time
import asyncio
import aiohttp
import nest_asyncio

session_counter = 0
total_correct_urls = []
os.makedirs("/ArchiveBate/ArchiveBate_10000", exist_ok=True)

while session_counter != 10:
  try:
    start = (session_counter * 10000) + 1
    end = start + 9999
    urls = []
    correct_urls = []
    for num in range(start, end):
      urls.append(f'https://www.archivebate.com/watch/{num:08d}')

    async def fetch(session, url):
        async with session.get(url) as response:
            if response.status == 200:
                correct_urls.append(url)
                return await response.text()


    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.ensure_future(fetch(session, url)) for url in urls]
            responses = await asyncio.gather(*tasks)

    nest_asyncio.apply()

    loop = asyncio.get_event_loop()
    s = time.perf_counter()
    loop.run_until_complete(main())
    elapsed = time.perf_counter() - s
    print(f"executed in {elapsed:0.2f} seconds.")
    print(len(correct_urls))
    correct_urls.sort()
    # print((correct_urls))
    with open(f"/ArchiveBate/ArchiveBate_10000/archiveBate_Urls_{session_counter}.txt", 'w') as file:
      for url in correct_urls:
        file.write(f"{url}\n")
    session_counter += 1
    print(session_counter)
    total_correct_urls.extend(correct_urls)
    print(len(total_correct_urls))
  except:
    pass
