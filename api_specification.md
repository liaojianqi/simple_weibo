# 接口规范

## 用户相关 /user

### 1. /user/login
描述 | 请求方法 | 参数 | 返回值
----|---------|-----|-----
用户登录 | POST | username、password | code=0表示登录成功

### 2. /user/register
描述 | 请求方法 | 参数 | 返回值
----|---------|-----|-----
用户注册 | POST | username、password | code=0表示注册成功

### 3. /user/follow
描述 | 请求方法 | 参数 | 返回值
----|---------|-----|-----
关注了某个用户 | GET | from_name, to_name | code=0表示关注成功

### 4. /user/cancel_follow
描述 | 请求方法 | 参数 | 返回值
----|---------|-----|-----
取关了某个用户 | GET | from_name, to_name | code=0表示取关成功

### 5. /user/list_follow
描述 | 请求方法 | 参数 | 返回值
----|---------|-----|-----
列出某个用户关注的人的数量 | GET | username | {code:0, data:[{},{},...]}
列出某个用户关注的人 | POST | username,offset,limit | {code:0, data:[{},{},...]}

### 6. /user/list_follower
描述 | 请求方法 | 参数 | 返回值
----|---------|-----|-----
列出某个用户的粉丝的数量 | GET | username | {code:0, data:[{},{},...]}
列出某个用户的粉丝 | POST | username,offset,limit | {code:0, data:[{},{},...]}