# views.py
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from Api.apply.models import Apply
from Api.files.models import File
from django.forms.models import model_to_dict

@api_view(['GET'])
def get_students(request):
    """
    获取所有学生信息的视图函数
    返回所有学生的详细信息，包括其关联的文件信息
    """
    try:
        # 获取所有学生记录
        students = Apply.objects.all()
        
        # 序列化结果并添加文件信息
        response_data = []
        for student in students:
            student_dict = model_to_dict(student)
            # 查找该学生对应的所有文件
            student_files = File.objects.filter(applicant_id=str(student.id), is_deleted=False)
            
            # 初始化简历和证明材料字段
            student_dict['resume_file_name'] = None
            student_dict['resume_file_path'] = None
            student_dict['proof_file_name'] = None
            student_dict['proof_file_path'] = None
            
            # 遍历所有文件，根据文件类型分别设置
            for file in student_files:
                if file.file_type in ['application/zip', 'application/x-zip-compressed']:
                    student_dict['resume_file_name'] = file.name
                    student_dict['resume_file_path'] = f'/api/files/download/{file.id}'
                elif file.file_type == 'application/pdf':
                    student_dict['proof_file_name'] = file.name
                    student_dict['proof_file_path'] = f'/api/files/download/{file.id}'
            
            response_data.append(student_dict)

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    