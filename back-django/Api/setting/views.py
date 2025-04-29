from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import University, Major, Personnel, Award, Year
from .serializers import UniversitySerializer, MajorSerializer, PersonnelSerializer, AdmissionPeriodSerializer, AwardSerializer, YearSerializer

# 大学
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def create(self, request, *args, **kwargs):
        # 处理批量创建、更新和删除院校数据
        data = request.data
        response_data = []
        errors = []

        # 获取现有院校记录
        existing_universities = {university.name: university for university in University.objects.all()}
        
        # 获取请求中的所有院校名称
        new_university_names = {item.get('name') for item in data if item.get('name')}
        
        # 删除不在新数据中的院校
        for university_name, university in existing_universities.items():
            if university_name not in new_university_names:
                university.delete()

        for item in data:
            try:
                university_name = item.get('name')
                if not university_name:
                    errors.append({'error': '院校名称不能为空'})
                    continue

                # 检查是否存在同名院校
                existing_university = existing_universities.get(university_name)

                if existing_university:
                    # 更新现有院校
                    serializer = self.get_serializer(existing_university, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)
                else:
                    # 创建新院校
                    serializer = self.get_serializer(data=item)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)

            except Exception as e:
                errors.append({'name': university_name, 'error': str(e)})

        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response_data, status=status.HTTP_201_CREATED)

# 专业
class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

    def create(self, request, *args, **kwargs):
        # 处理批量创建、更新和删除专业数据
        data = request.data
        response_data = []
        errors = []

        # 获取现有专业记录
        existing_majors = {major.name: major for major in Major.objects.all()}
        
        # 获取请求中的所有专业名称
        new_major_names = {item.get('name') for item in data if item.get('name')}
        
        # 删除不在新数据中的专业
        for major_name, major in existing_majors.items():
            if major_name not in new_major_names:
                major.delete()

        for item in data:
            try:
                major_name = item.get('name')
                if not major_name:
                    errors.append({'error': '专业名称不能为空'})
                    continue

                # 检查是否存在同名专业
                existing_major = existing_majors.get(major_name)

                if existing_major:
                    # 更新现有专业
                    serializer = self.get_serializer(existing_major, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)
                else:
                    # 创建新专业
                    serializer = self.get_serializer(data=item)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)

            except Exception as e:
                errors.append({'name': major_name, 'error': str(e)})

        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response_data, status=status.HTTP_201_CREATED)

# 人员
class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        response_data = []
        errors = []

        existing_personnel = {person.name: person for person in Personnel.objects.all()}
        new_personnel_names = {item.get('name') for item in data if item.get('name')}
        
        for person_name, person in existing_personnel.items():
            if person_name not in new_personnel_names:
                person.delete()

        for item in data:
            try:
                person_name = item.get('name')
                if not person_name:
                    errors.append({'error': '人员名称不能为空'})
                    continue

                # 处理字段映射
                processed_item = {
                    'name': item.get('name'),
                    'recruitment_type': item.get('recruitment_type'),
                    'department': item.get('department'),  # 添加部门字段
                    'research_direction': item.get('research_direction')  # 添加研究方向字段
                }

                existing_person = existing_personnel.get(person_name)

                if existing_person:
                    serializer = self.get_serializer(existing_person, data=processed_item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)
                else:
                    serializer = self.get_serializer(data=processed_item)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)

            except Exception as e:
                errors.append({'name': person_name, 'error': str(e)})

        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response_data, status=status.HTTP_201_CREATED)

# 奖项
class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        response_data = []
        errors = []

        existing_awards = {award.name: award for award in Award.objects.all()}
        new_award_names = {item.get('name') for item in data if item.get('name')}

        for award_name, award in existing_awards.items():
            if award_name not in new_award_names:
                award.delete()

        for item in data:
            try:
                award_name = item.get('name')
                if not award_name:
                    errors.append({'error': '奖项名称不能为空'})
                    continue

                existing_award = existing_awards.get(award_name)

                if existing_award:
                    serializer = self.get_serializer(existing_award, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)
                else:
                    serializer = self.get_serializer(data=item)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)

            except Exception as e:
                errors.append({'name': award_name, 'error': str(e)})

        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response_data, status=status.HTTP_201_CREATED)

# 年份
class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

    def list(self, request, *args, **kwargs):
        """
        获取当前年份
        返回格式: {"year": 2023}
        """
        year = Year.objects.first()
        if year:
            return Response({"year": year.year})
        return Response({"year": None})

    def create(self, request, *args, **kwargs):
        """
        更新年份配置
        接收格式:
        1. 直接数字: 2023
        2. 对象格式: {"year": 2023}
        3. 嵌套对象格式: {"year": [{"year": 2023}]}
        """
        data = request.data
        
        # 处理直接传递数字的情况
        if isinstance(data, (int, float)):
            year_value = int(data)
        # 处理对象格式的情况
        elif isinstance(data, dict):
            if 'year' in data:
                # 处理嵌套列表的情况
                if isinstance(data['year'], list) and len(data['year']) > 0:
                    if isinstance(data['year'][0], dict) and 'year' in data['year'][0]:
                        year_value = int(data['year'][0]['year'])
                    else:
                        return Response(
                            {"error": "无效的年份格式"}, 
                            status=status.HTTP_400_BAD_REQUEST
                        )
                # 处理直接年份值的情况
                else:
                    year_value = int(data['year'])
            else:
                return Response(
                    {"error": "无效的年份格式"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"error": "无效的年份格式"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not year_value:
            return Response(
                {"error": "年份不能为空"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
        # 清空原有年份数据
        Year.objects.all().delete()
        
        # 创建新年份记录
        Year.objects.create(year=year_value)
        
        return Response({"year": year_value})