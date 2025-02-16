from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import University, Major, Personnel, AdmissionPeriod
from .serializers import UniversitySerializer, MajorSerializer, PersonnelSerializer, AdmissionPeriodSerializer

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

class AdmissionPeriodViewSet(viewsets.ModelViewSet):
    queryset = AdmissionPeriod.objects.all()
    serializer_class = AdmissionPeriodSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)