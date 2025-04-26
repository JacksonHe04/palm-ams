from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.utils import timezone  # 添加这行导入
from .models import File
from ..apply.models import Apply
import os
import uuid
import mimetypes
import zipfile
import tempfile
import urllib

# 创建文件存储目录
# 在文件顶部的导入语句后添加新的目录常量
FILE_STORAGE_PATH = os.path.join(settings.STATIC_ROOT, 'uploads')
RESUME_STORAGE_PATH = os.path.join(settings.STATIC_ROOT, 'resumes')  # 新增简历存储路径

# 创建必要的目录
os.makedirs(FILE_STORAGE_PATH, exist_ok=True)
os.makedirs(RESUME_STORAGE_PATH, exist_ok=True)  # 创建简历目录

@csrf_exempt
def upload_file(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持POST请求'}, status=405)

    try:
        file = request.FILES.get('file')
        applicant_id = request.headers.get('X-Applicant-ID', None)

        if not file:
            return JsonResponse({'error': '未找到上传文件'}, status=400)

        # 使用原始文件名
        file_ext = os.path.splitext(file.name)[1]
        new_filename = file.name
        
        # 直接保存文件
        file_path = os.path.join(FILE_STORAGE_PATH, new_filename)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        file_size = file.size
        file_type = file.content_type

        # 创建文件记录
        file_record = File.objects.create(
            applicant_id=applicant_id,
            name=new_filename,
            original_name=file.name,
            file_path=file_path,
            file_size=file_size,
            file_type=file_type,
            uploader=request.user.username if request.user.is_authenticated else None
        )

        return JsonResponse({
            'message': '文件上传成功',
            'file_id': file_record.id,
            'file_name': file_record.original_name
        })

    except Exception as e:
        return JsonResponse({'error': f'文件上传失败：{str(e)}'}, status=500)

def download_file(request, file_id):
    try:
        file_record = File.objects.get(id=file_id, is_deleted=False)
        if not os.path.exists(file_record.file_path):
            return JsonResponse({'error': '文件不存在'}, status=404)

        content_type, _ = mimetypes.guess_type(file_record.file_path)
        response = FileResponse(
            open(file_record.file_path, 'rb'),
            content_type=content_type or 'application/octet-stream'
        )
        
        # 使用 name 作为下载文件名，并进行 URL 编码以支持中文
        filename = urllib.parse.quote(file_record.name)
        response['Content-Disposition'] = f'attachment; filename="{filename}"; filename*=UTF-8\'\'{filename}'
        return response

    except File.DoesNotExist:
        return JsonResponse({'error': '文件记录不存在'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'文件下载失败：{str(e)}'}, status=500)

@csrf_exempt
def delete_file(request, file_id):
    if request.method != 'DELETE':
        return JsonResponse({'error': '仅支持DELETE请求'}, status=405)

    try:
        file_record = File.objects.get(id=file_id, is_deleted=False)
        file_record.delete()  # 使用软删除
        return JsonResponse({'message': '文件删除成功'})

    except File.DoesNotExist:
        return JsonResponse({'error': '文件不存在'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'文件删除失败：{str(e)}'}, status=500)

def get_file_info(request, file_id):
    try:
        file_record = File.objects.get(id=file_id, is_deleted=False)
        return JsonResponse({
            'id': file_record.id,
            'name': file_record.original_name,
            'size': file_record.file_size,
            'type': file_record.file_type,
            'upload_time': file_record.upload_time,
            'uploader': file_record.uploader
        })

    except File.DoesNotExist:
        return JsonResponse({'error': '文件不存在'}, status=404)

def list_files(request):
    if request.method != 'GET':
        return JsonResponse({'error': '仅支持GET请求'}, status=405)

    try:
        applicant_id = request.GET.get('applicant_id')
        if not applicant_id:
            return JsonResponse({'error': '缺少applicant_id参数'}, status=400)

        files = File.objects.filter(applicant_id=applicant_id, is_deleted=False)
        file_list = [{
            'id': file.id,
            'name': file.original_name,
            'file_type': file.file_type,
            'upload_time': file.upload_time,
            'file_path': file.file_path
        } for file in files]

        return JsonResponse(file_list, safe=False)

    except Exception as e:
        return JsonResponse({'error': f'获取文件列表失败：{str(e)}'}, status=500)


@csrf_exempt
def upload_resume(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持POST请求'}, status=405)

    try:
        file = request.FILES.get('file')
        applicant_id = request.headers.get('X-Applicant-ID', None)

        if not file:
            return JsonResponse({'error': '未找到上传文件'}, status=400)

        # 检查文件类型
        if not file.content_type == 'application/pdf':
            return JsonResponse({'error': '只能上传PDF格式的简历'}, status=400)

        # 检查文件大小（10MB）
        if file.size > 10 * 1024 * 1024:
            return JsonResponse({'error': '文件大小不能超过10MB'}, status=400)

        # 删除该申请人之前上传的简历
        File.objects.filter(
            applicant_id=applicant_id,
            is_resume=True,
            is_deleted=False
        ).update(is_deleted=True)

        # 使用原始文件名，但添加时间戳避免重名
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        file_ext = os.path.splitext(file.name)[1]
        new_filename = f"resume_{applicant_id}_{timestamp}{file_ext}"
        
        # 保存文件到简历目录
        file_path = os.path.join(RESUME_STORAGE_PATH, new_filename)  # 使用简历专用目录
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # 创建文件记录
        file_record = File.objects.create(
            applicant_id=applicant_id,
            name=new_filename,
            original_name=file.name,
            file_path=file_path,
            file_size=file.size,
            file_type=file.content_type,
            is_resume=True,
            uploader=request.user.username if request.user.is_authenticated else None
        )

        return JsonResponse({
            'message': '简历上传成功',
            'file_id': file_record.id,
            'file_name': file_record.original_name,
            'file_path': f'/static/resumes/{new_filename}'  # 修改返回路径
        })

    except Exception as e:
        return JsonResponse({'error': f'简历上传失败：{str(e)}'}, status=500)