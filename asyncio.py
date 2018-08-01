import asyncio
import pandas as pd
import time
from datetime import datetime



my_list = [['flight', 'book','book me a flight'], ['flight', 'enquiry','may i know my flight schedule'], ['flight', 'fare','looping']]
my_list2 = [['bus', 'enquiry','list bus to bangalore at morning'], ['bus', 'book','book me a bus'], ['bus', 'fare','price for two tickets']]
my_list3=[['hotel','checkin','checking in'],['hotel','lorem','ipsum'],['hotel','ipsu','lorum']]        



async def dataextraction(textdata):
        my_list1,my_list2,my_list3=[x[0] for x in textdata],[x[1]for x in textdata],[x[2] for x in textdata]
        #await asyncio.sleep(0.0001)
        df2=pd.DataFrame({'context':my_list1,'intent':my_list2,'data':my_list3,'timestamp':datetime.now()})
        await asyncio.sleep(0.0001)
        print(df2)
        
async def main():
    ext1 = loop.create_task(dataextraction(my_list))
    ext2 = loop.create_task(dataextraction(my_list2))
    ext3 = loop.create_task(dataextraction(my_list3))
    await asyncio.wait([ext1,ext2,ext3])
    

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()
