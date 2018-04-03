import orm
from models import User,Blog,Comment
import asyncio
import sys

async def test(loop):
    db_dict={'user':'root','password':'password','db':'awesome'}
    await orm.create_pool(loop=loop,**db_dict)
    u =User(name='Test',email='test@example.com',passwd='12345',image='about:blank',id='123')
    await u.save()
    await orm.close_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()



    
