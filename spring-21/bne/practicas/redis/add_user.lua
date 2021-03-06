local user_seq_key = KEYS[1]
local user_id = redis.call('incr', user_seq_key)
local user_key = 'users:'..user_id

local username = ARGV[1]
redis.call('hset', user_key, 'username', username, 'uid', user_id)

return redis.call('hgetall', user_key)