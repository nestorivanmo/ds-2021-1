local url_seq_key = KEYS[1]
local rurl_base_domain_key = KEYS[2]
local rurl_seq_key = KEYS[3]

local user_id = ARGV[1]
local url = ARGV[2]
local public = ARGV[3]
local private = ARGV[4]
local category = ARGV[5]

local url_id = redis.call('incr', url_seq_key)
local url_user_key = 'url:'..url_id..':'..user_id
local rurl_base_domain = redis.call('get', rurl_base_domain_key)
local rurl_id = redis.call('incrby', rurl_seq_key, 17)
local rurl = rurl_base_domain..rurl_id

redis.call('hset', url_user_key, 'url', url, 'rurl', rurl, 'public', public, 'private', private, 'category', category)

local category_user_key = 'categories:'..user_id
redis.call('sadd', category_user_key, category)

return redis.call('hgetall', url_user_key)