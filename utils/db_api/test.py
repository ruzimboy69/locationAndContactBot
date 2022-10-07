# import asyncio
# from utils.db_api.postgresql import Database
#
#
# # from postgresql import Database
#
#
# async def test():
#     dbtest = Database()
#     await dbtest.create()
#
#     # print("Users jadvalini yaratamiz")
#     # await dbtest.create_table_users()
#     # print("Yaratildi")
#     # print("Foydalanuvchilarni qoshamiz")
#     await dbtest.add_user("anvawefwr", "sariqfwefw dev", 12340)
#     await dbtest.add_user("ruzimboy", "royholmswefw", 123)
#     await dbtest.add_user("anvar1wef", "sariq1wef", 1238)
#     await dbtest.add_user("anvar3wef", "sariq2wefw", 1237)
#     print("Qoshildi")
#     users = await dbtest.select_all_user()
#     print(f"Barcha foydalanuvchilar: {users}")
#     user = await dbtest.select_user(id=4)
#     print(f"Foydalanuvchi {user}")
# asyncio.run(test())
