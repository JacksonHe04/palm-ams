# ApplicationSystem/asgi.py
"""
这个文件东西是老的，但是没什么用，好吧？
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ApplicationSystem.settings')

application = get_asgi_application()
