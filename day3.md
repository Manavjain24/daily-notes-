## day 3 we would be talking about async await and asyncho 
--so async await function is also used in python as diffrent from the 
javascript according to which the async and await function is being used 
to it provides high performance and structured code 
--in using this library such as asyncho is being used first 
--the explaination is in such a way that the async function is being used so that the function 
calls such as an api call or the database queries could never stop the runnig code so it saves 
resources as well as memory of the code .
-- the example of some of the async await function is as follows (async file reader + api caller)
-- example - this is only async file reader
import asyncio
import aiofiles
async def read_files()
async with aiofiles.open (C:\Users\Pranvika Jain\Downloads\script.txt,mode = 'r') as file:
content = await file.read()
return content 
async def main():
content = await read_file('script.txt')
print(content)
asyncio.run(main())
this is for async file reader+ api caller
import asyncio 
import aiofiles
import httpx
async def fetch_data(client)






