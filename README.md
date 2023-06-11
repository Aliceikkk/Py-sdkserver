# Py-sdkserver
从gio的docker项目中摘出来的

Only applicable to a certain anime game


只是出于兴趣爱好才维护此项目 并且本人只是一个新手 有任何问题请联系我Aliceikkk@outlook.com


------
依赖库
------
pip3 install --no-cache-dir werkzeug==2.2.3 flask==2.2.4 requests rsa geoip2 bcrypt

-----
run
-----
python3 ./main.py serve

记得初始化数据库

python3 ./main.py initdb 

如果显示已存在表 需要自行链接sdk.db清除所有表
