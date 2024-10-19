# ApplicationSystem/wsgi.py
"""
这个文件东西是老的，但是没什么用，好吧？
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ApplicationSystem.settings')

application = get_wsgi_application()
