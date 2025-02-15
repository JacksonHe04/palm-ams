from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import User
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from functools import wraps

@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({
                'success': False,
                'message': '用户名和密码不能为空'
            }, status=400)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': '用户不存在'
            }, status=401)

        if not check_password(password, user.password):
            return JsonResponse({
                'success': False,
                'message': '密码错误'
            }, status=401)

        # 生成JWT token
        payload = {
            'user_id': user.id,
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return JsonResponse({
            'success': True,
            'message': '登录成功',
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username
            }
        })

    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': '无效的请求数据格式'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

def jwt_auth_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        
        if not token:
            return JsonResponse({
                'success': False,
                'message': 'Authentication credentials were not provided.'
            }, status=403)
            
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user = payload
            return view_func(request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return JsonResponse({
                'success': False,
                'message': 'Token has expired'
            }, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid token'
            }, status=401)
            
    return wrapped_view