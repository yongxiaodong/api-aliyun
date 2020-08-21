# 获取阿里云云监控中RDS监控数据和redis监控数据，并暴露出来供Prometheus使用

## 运行依赖
    python3
    

## clone代码、安装阿里云sdk
    git clone https://github.com/yongxiaodong/api-aliyun.git
    pip3 install -r required.txt


## 配置阿里云的秘钥信息
    vim conf/settings.py
   
## 启动
    python3 bin/start.py
    > 默认日志会输出到logs目录中
    

## web访问
    http://{{ IP }}:9091/metrics
