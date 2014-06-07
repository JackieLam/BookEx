BookEx
======

Second-hand books exchange platform for Sun Yat-sen University, based on Web 2.0.

传送门-><a href="http://sysubookex.sinaapp.com/">http://sysubookex.sinaapp.com/</a>

##本地开发环境配置
- MySQL
- Python MySQLdb
- Tornado 

##SAE部署说明
- index.wsgi为SAE自动识别并且启动的文件，SAE会自动识别index.wsgi中的application实例开启Web Application，并提供进程守护等功能。
- server.py为本地开发而设，本地开发需输入指令python server.py 8080开启本地服务，访问http://localhost:8080。