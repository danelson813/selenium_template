# from fake_useragent import UserAgent

# # Creating an object
# ua = UserAgent()

# # Printing examples 
# for i in range(10):
#     print(ua.random)

from fake_useragent import UserAgent
import re

def create_header(referer='https://google.com'):
    """Return a header that matches user-agent, platform and version
    referer --address that user was before the request
    """   
 
    ua=UserAgent()
    user_a = ua.random 
    # Try to find a user-agent windows user
    for n in range(200):
        user_a2 = ua.random
        if re.search('Windows',user_a2):
            user_a = user_a2
            break
            
    # Try to find the Windows version
    system_version = re.findall('Windows NT *(\d*.\d*)',user_a)
    if len(system_version) == 0:
        version ='10.0.0' 
    else:
        version = system_version[0] + '.0'
    
    header = {'Sec-Ch-Ua-Platform':'Windows',
              'Sec-Ch-Ua-Platform-Version':version,
              'Referer':referer, 
              'User-Agent':user_a}
    
    return header

hed = create_header()
print(hed)


# run asynchronously

import aiohttp
import asyncio
from bs4 import BeautifulSoup
from time import perf_counter


# Coroutines can be declared with the async/await syntax for asyncio applications
async def asynchronous_request(n):
    """Run n requests to the same site (asynchronously)
    * http://books.toscrape.com/ is a Web Scraping Sandbox, for learning and practice purpose
    
    n -- qnt. of requests
    """

    t_start = perf_counter()
    # Declare a ClientSession and execute the requests through it
    async with aiohttp.ClientSession() as session:
        # n requests to the same site 
        for i in range(n):
            async with session.get('http://books.toscrape.com/') as resp:
                # Any object returned by calling a coroutine function, needs to be awaited. 
                html = await resp.text()
                bs = BeautifulSoup(html, 'html.parser')
                print(f'Request {i+1} - Status Code: {resp.status}')
    
    t_end = perf_counter()
    print(f'\nTotal Time: {t_end-t_start:.2f}')
   
   
if __name__ == '__main__':
    # Run the coroutine function
    # With jupyter notebooks use: await asynchronous_request(50)
    asyncio.run(asynchronous_request(50))