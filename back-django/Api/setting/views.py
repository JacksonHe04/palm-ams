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
        # 处理批量创建、更新和删除人员数据
        data = request.data
        response_data = []
        errors = []

        # 获取现有人员记录
        existing_personnel = {person.name: person for person in Personnel.objects.all()}

        for item in data:
            try:
                person_name = item.get('name')
                if not person_name:
                    errors.append({'error': '人员名称不能为空'})
                    continue

                # 将recruitmentType转换为recruitment_type
                if 'recruitmentType' in item:
                    item['recruitment_type'] = item.pop('recruitmentType')

                # 检查是否存在同名人员
                existing_person = existing_personnel.get(person_name)

                if existing_person:
                    # 更新现有人员
                    serializer = self.get_serializer(existing_person, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    response_data.append(serializer.data)
                else:
                    # 创建新人员
                    serializer = self.get_serializer(data=item)
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