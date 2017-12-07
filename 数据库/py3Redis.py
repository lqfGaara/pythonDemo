from RedisTest import RedisHelper

helper = RedisHelper("localhost", 6379)
helper.setValue('name', 'syl')
print(helper.getValue('name').decode())
