# CUMT微生活

中国矿业大学南湖校区CUMT微生活电费查询 Nginx+Flask+gunicorn  
目前只有一个接口


本地：

       pip install -r requirements.txt
   
       python manage.py runserver -r -d 
   
Linux：

       pip3 install -r requirements.txt
   
       pip3 install gunicorn
   
       gunicorn -w 4 -b 127.0.0.1:5000 app:app  
 
 
接口：
POST：

       https://www.lvyingzhao.cn/dianfei
example：
       
          {
            "home": "梅2楼"，
             "num":"B4222"
          }
Response：
        
         
         {
         "status": "200",
           "msg": "ok"
          "data": "["227.43"]"
          }
         
          
