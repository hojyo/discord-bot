import redis

def redis_connect():
    # redisと接続
    # とりあえずデータの形式はあまり変えずに，キャラ名のキーと，スキル区分のバリュー（この中にスキル名のキーと技能値のvalueを持たせる）
    # RDBMSじゃないからまとめて上書きしなくても良さそう、オンメモリだし
    # docker-composeなので内部で名前解決はしてもらう
    redis_pool = redis.ConnectionPool(host='redis', port=6379,k db=0, max_connections=4)
    connect = redis.StrictRedis(connection_pool=redis_pool)

    return connect
