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
import time
import json
from django.http import HttpResponse
from datetime import datetime

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

        # 生成带时间戳的文件名
        timestamp = timezone.localtime().strftime("%Y%m%d%H%M%S")
        file_name, file_ext = os.path.splitext(file.name)
        new_filename = f"{file_name}_{timestamp}{file_ext}"
        
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
        
        # 生成格式化的时间戳 (年月日时分秒)
        # timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        timestamp = timezone.localtime().strftime("%Y%m%d%H%M%S")
        file_name, file_ext = os.path.splitext(file.name)  # 正确地解构文件名和扩展名
        new_filename = f"{file_name}_{timestamp}{file_ext}"  # 加入扩展名
        print(new_filename)
        
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

import io
@csrf_exempt
def batch_download_files(request):
    """
    批量下载文件并打包成zip
    请求参数示例：
    {
        "file_ids": [1, 2, 3],  # 文件ID列表
        "application_type": "博士生"  # 申请类型，用于zip文件命名
    }
    """
    try:
        # 获取请求参数
        data = json.loads(request.body)
        file_ids = data.get('file_ids', [])
        application_type = data.get('application_type', '')
        
        if not file_ids:
            return JsonResponse({'error': '未提供文件ID'}, status=400)
            
        # 创建内存中的zip文件
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # 创建文件夹
            resume_folder = '简历文件/'  # 简历文件夹
            proof_folder = '证明文件/'    # 证明文件夹
            
            # 获取所有文件记录
            files = File.objects.filter(id__in=file_ids, is_deleted=False)
            
            for file_record in files:
                if not os.path.exists(file_record.file_path):
                    continue
                    
                # 根据is_resume字段决定存放的文件夹
                target_folder = resume_folder if file_record.is_resume else proof_folder
                
                # 读取文件内容
                with open(file_record.file_path, 'rb') as f:
                    # 将文件添加到zip中
                    zip_file.writestr(
                        target_folder + file_record.name,
                        f.read()
                    )
        
        # 准备响应
        zip_buffer.seek(0)
        response = HttpResponse(
            zip_buffer.getvalue(),
            content_type='application/zip'
        )
        
        # 设置下载文件名
        filename = f'申请材料_{application_type}_{datetime.now().strftime("%Y%m%d")}.zip'
        encoded_filename = urllib.parse.quote(filename)
        response['Content-Disposition'] = f'attachment; filename="{encoded_filename}"; filename*=UTF-8\'\'{encoded_filename}'
        
        return response
        
    except Exception as e:
        return JsonResponse({'error': f'打包下载失败：{str(e)}'}, status=500)