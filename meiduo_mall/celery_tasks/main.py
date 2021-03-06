from celery import Celery
import os

# 加载 django 配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.development")

# 创建 Celery 对象
celery_object = Celery('meiduo')

# 加载 celery 配置
celery_object.config_from_object('celery_tasks.config')

# 注册 celery 任务 (加载 url 下的 tasks.py 文件, 所以路径中必须有 tasks 文件)
celery_object.autodiscover_tasks(['celery_tasks.sms', 'celery_tasks.email'])
