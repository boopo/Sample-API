# CUMT-
中国矿业大学南湖校区CUMT微生活电费查询 Nginx+Flask+gunicorn
一个简单的爬虫，通过request请求，re处理，flask-restful封装
接口文档在apidoc/index.html  由apidoc生成


本地：
   pip install -r requirements.txt
   
   python manage.py runserver -r -d  
Linux：
   pip3 install -r requirements.txt
   pip3 install gunicorn
   gunicorn -w 4 -b 127.0.0.1:5000 app:app  //w指定线程数 -b绑定端口
   用nginx做转发
