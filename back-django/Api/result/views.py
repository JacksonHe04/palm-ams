from django.http import JsonResponse
from rest_framework.decorators import api_view
from Api.apply.models import Apply
from Api.setting.models import Major, Award, Year
from Api.percent.models import Percent
from Api.files.models import File
from django.forms.models import model_to_dict

# 论文和奖项可以破格的筛选
def filter_talent(student):
    # 检查论文条件
    if student.paper1_isFirst and student.paper1_ccfLevel in ['A', 'B']:
        student.isPaperCondition = True
    elif student.paper2_isFirst and student.paper2_ccfLevel in ['A', 'B']:
        student.isPaperCondition = True
    elif student.paper3_isFirst and student.paper3_ccfLevel in ['A', 'B']:
        student.isPaperCondition = True
    else:
        student.isPaperCondition = False

    # 检查奖项条件
    student.isAwardCondition = False
    awards = [
        (student.award1_isLeader, student.award1_awardName, student.award1_awardRanking),
        (student.award2_isLeader, student.award2_awardName, student.award2_awardRanking),
        (student.award3_isLeader, student.award3_awardName, student.award3_awardRanking)
    ]

    for is_leader, award_name, award_ranking in awards:
        if is_leader:
            award = Award.objects.filter(
                name=award_name,
                category='限制奖项'
            ).first()
            if award and award_ranking in ['特等奖', '金奖']:
                student.isAwardCondition = True
                break

    return student.isPaperCondition or student.isAwardCondition

# 检查专业
def filter_major(student):
    # 检查本科专业
    major_exists = Major.objects.filter(
        name=student.major,
        category='可录取专业'
    ).exists()
    if major_exists:
        return True

    return False

# 筛选学生
@api_view(['GET'])
def filter_students(request):
    try:
        # 获取当前年份
        curr_year = Year.objects.first().year

        # 获取百分比设置
        percent = Percent.objects.first()
        if not percent:
            return JsonResponse({'error': '未找到百分比设置'}, status=400)

        result = []
        failed_ids = []  # 新增：存储未通过筛选的学生ID
        students = Apply.objects.filter(year=curr_year)
        # 打印所有学生的姓名和数量
        student_names = [student.name for student in students]
        print('所有学生数量：', len(student_names))
        print('所有学生姓名：', student_names)

        # 新增：用于存储直接通过筛选的学生姓名
        direct_pass_students = []

        for student in students:
            # 如果是博士 直博 考研硕士，直接通过筛选
            if student.applicationType in ['博士', '直博', '考研硕士']:
                student.isFilterCondition = True
                result.append(student)
                direct_pass_students.append(student.name)  # 新增：添加到直接通过名单
                continue
        
        # 对硕士进行筛选
            # 转换百分比为数字
            try:
                p = float(student.percentage.rstrip('%'))
            except (ValueError, AttributeError):
                continue

            passed_filter = False  # 新增：标记是否通过筛选

            # 检查A类院校条件
            if student.universityLevel == 'A' or student.masterUniversityLevel == 'A':
                if p <= percent.pOfA:
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    print(f'学生{student.name}未通过A类院校基本条件筛选：百分比{p}% > {percent.pOfA}%')
                if student.isTopClass and p <= percent.pOfATop:
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    if student.isTopClass:
                        print(f'学生{student.name}未通过A类院校拔尖班条件筛选：百分比{p}% > {percent.pOfATop}%')
                if filter_talent(student) and p <= percent.pOfATalent:
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    if filter_talent(student):
                        print(f'学生{student.name}未通过A类院校人才计划条件筛选：百分比{p}% > {percent.pOfATalent}%')
                    else:
                        print(f'学生{student.name}未通过A类院校人才计划条件筛选：未满足论文或奖项要求')

            # 检查B类院校条件
            elif student.universityLevel == 'B' or student.masterUniversityLevel == 'B':
                if p <= percent.pOfB and filter_major(student):
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    if p > percent.pOfB:
                        print(f'学生{student.name}未通过B类院校基本条件筛选：百分比{p}% > {percent.pOfB}%')
                    if not filter_major(student):
                        print(f'学生{student.name}未通过B类院校基本条件筛选：专业{student.major}不在可录取专业列表中')
                if student.isTopClass and p <= percent.pOfBTop:
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    if student.isTopClass:
                        print(f'学生{student.name}未通过B类院校拔尖班条件筛选：百分比{p}% > {percent.pOfBTop}%')
                if filter_talent(student) and p <= percent.pOfBTalent:
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    if filter_talent(student):
                        print(f'学生{student.name}未通过B类院校人才计划条件筛选：百分比{p}% > {percent.pOfBTalent}%')
                    else:
                        print(f'学生{student.name}未通过B类院校人才计划条件筛选：未满足论文或奖项要求')

            # 检查C类院校条件
            elif student.universityLevel == 'C' or student.masterUniversityLevel == 'C':
                if p <= percent.pOfC and filter_major(student):
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    if p > percent.pOfC:
                        print(f'学生{student.name}未通过C类院校基本条件筛选：百分比{p}% > {percent.pOfC}%')
                    if not filter_major(student):
                        print(f'学生{student.name}未通过C类院校基本条件筛选：专业{student.major}不在可录取专业列表中')
                if student.isTopClass and p <= percent.pOfCTop:
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    if student.isTopClass:
                        print(f'学生{student.name}未通过C类院校拔尖班条件筛选：百分比{p}% > {percent.pOfCTop}%')
                if filter_talent(student) and p <= percent.pOfCTalent:
                    student.isFilterCondition = True
                    result.append(student)
                    passed_filter = True
                    continue
                else:
                    if filter_talent(student):
                        print(f'学生{student.name}未通过C类院校人才计划条件筛选：百分比{p}% > {percent.pOfCTalent}%')
                    else:
                        print(f'学生{student.name}未通过C类院校人才计划条件筛选：未满足论文或奖项要求')

            # 如果学生没有通过任何筛选条件，将其ID添加到failed_ids数组中
            if not passed_filter:
                failed_ids.append(str(student.id))

        # 序列化结果并添加文件信息
        response_data = []
        for student in result:
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
                if file.file_type == 'application/zip':
                    student_dict['resume_file_name'] = file.name
                    student_dict['resume_file_path'] = f'/api/files/download/{file.id}'
                elif file.file_type == 'application/pdf':
                    student_dict['proof_file_name'] = file.name
                    student_dict['proof_file_path'] = f'/api/files/download/{file.id}'
            
            response_data.append(student_dict)

        # 返回筛选通过的学生信息和未通过筛选的学生ID
        # 在控制台打印通过的学生的姓名的数组
        # 新增：打印直接通过筛选的学生姓名
        print('直接通过筛选的学生姓名（博士、直博、考研硕士）：', direct_pass_students)
        passed_students = [student.name for student in result]
        print('通过的学生姓名：', passed_students)
        # 打印未通过筛选的学生的姓名的数组
        failed_students = Apply.objects.filter(id__in=failed_ids)
        failed_students_names = [student.name for student in failed_students]
        print('未通过筛选的学生姓名：', failed_students_names)


        return JsonResponse({
            'passed_students': response_data,
            'failed_student_ids': failed_ids
        }, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

        
@api_view(['GET'])
def get_failed_students(request):
    try:
        # 调用 filter_students 获取筛选结果
        filter_response = filter_students(request)
        
        # 如果筛选过程出错，直接返回错误
        if filter_response.status_code != 200:
            return filter_response
            
        # 获取失败的学生ID列表
        response_data = filter_response.data
        failed_ids = response_data.get('failed_student_ids', [])
        
        # 获取这些失败学生的详细信息
        failed_students = Apply.objects.filter(id__in=failed_ids)
        
        # 序列化结果并添加文件信息
        response_data = []
        for student in failed_students:
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
                if file.file_type == 'application/zip':
                    student_dict['resume_file_name'] = file.name
                    student_dict['resume_file_path'] = f'/api/files/download/{file.id}'
                elif file.file_type == 'application/pdf':
                    student_dict['proof_file_name'] = file.name
                    student_dict['proof_file_path'] = f'/api/files/download/{file.id}'
            
            response_data.append(student_dict)

        return JsonResponse({
            'failed_students': response_data
        }, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)