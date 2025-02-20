from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import File
from ..apply.models import Apply
import os
import uuid
import mimetypes
import zipfile
import tempfile

# 创建文件存储目录
FILE_STORAGE_PATH = os.path.join(settings.STATIC_ROOT, 'uploads')
os.makedirs(FILE_STORAGE_PATH, exist_ok=True)

@csrf_exempt
def upload_file(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持POST请求'}, status=405)

    try:
        file = request.FILES.get('file')
        applicant_id = request.POST.get('applicant_id')

        if not file:
            return JsonResponse({'error': '未找到上传文件'}, status=400)
        if not applicant_id:
            return JsonResponse({'error': '未提供申请者ID'}, status=400)

        # 获取申请者信息
        try:
            apply = Apply.objects.get(id=applicant_id)
        except Apply.DoesNotExist:
            return JsonResponse({'error': '未找到对应的申请信息'}, status=404)

        # 生成文件名
        file_ext = os.path.splitext(file.name)[1]
        applicant_info = f"{apply.applicationType or '未知类型'}_{apply.name or '未知姓名'}_{apply.university or '未知本科'}_{apply.masterUniversity or '未知硕士'}_{apply.year or '未知年份'}"
        new_filename = f"{applicant_info}{file_ext}"
        
        # 如果是需要压缩的文件类型
        if file_ext.lower() in ['.doc', '.docx', '.pdf', '.jpg', '.jpeg', '.png']:
            # 创建临时目录
            with tempfile.TemporaryDirectory() as temp_dir:
                # 保存原始文件
                temp_file_path = os.path.join(temp_dir, file.name)
                with open(temp_file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                
                # 创建ZIP文件
                zip_filename = f"{applicant_info}.zip"
                zip_path = os.path.join(FILE_STORAGE_PATH, zip_filename)
                
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(temp_file_path, file.name)
                
                # 更新文件信息
                file_path = zip_path
                new_filename = zip_filename
                file_size = os.path.getsize(zip_path)
                file_type = 'application/zip'
        else:
            # 对于其他类型的文件，直接保存
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
        response['Content-Disposition'] = f'attachment; filename="{file_record.original_name}"'
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