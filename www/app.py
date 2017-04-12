# -*- coding: utf-8 -*-
import asyncio

from models import User

import orm

loop = asyncio.get_event_loop()


#创建实例
async def test():
    await orm.create_pool(loop=loop, host='localhost', port=3306, user='fq', password='fq', db='fq')

    # 创建一位用户:
    # new_user = User(name='sytu', email='imsytu@163.com', passwd='123456', admin=True, image='about:about')
    # await new_user.save()
    r = await User.findAll()
    print(r)

loop.run_until_complete(test())
