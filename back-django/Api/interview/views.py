import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Interview

class InterviewUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        try:
            file = request.FILES['file']
            df = pd.read_excel(file)

            # 清除旧数据
            Interview.objects.all().delete()

            # 保存新数据
            for _, row in df.iterrows():
                Interview.objects.create(
                    student=row.get('student') or row.get('学生'),
                    score_teacher1=float(row.get('scoreTeacher1') or row.get('老师一打分')),
                    score_teacher2=float(row.get('scoreTeacher2') or row.get('老师二打分')),
                    score_teacher3=float(row.get('scoreTeacher3') or row.get('老师三打分')),
                    resume_score=float(row.get('resumeScore') or row.get('简历分数') or 0)
                )

            return Response({'message': '数据导入成功'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

def get_normalized_scores(request):
    try:
        interviews = Interview.objects.all()
        
        # 如果没有数据，返回空列表
        if not interviews.exists():
            return JsonResponse({'data': []}, status=200)

        # 获取所有评分
        scores = [
            (interview.score_teacher1 + interview.score_teacher2 + interview.score_teacher3) / 3
            for interview in interviews
        ]

        # 计算最大最小值
        max_score = max(scores)
        min_score = min(scores)
        score_range = max_score - min_score

        # 更新归一化分数
        for interview, score in zip(interviews, scores):
            if score_range == 0:
                normalized_score = 1.0  # 如果所有分数相同
            else:
                normalized_score = (score - min_score) / score_range
            
            interview.normalized_score = normalized_score
            interview.save()

        # 返回更新后的数据
        data = [
            {
                'student': interview.student,
                'scoreTeacher1': interview.score_teacher1,
                'scoreTeacher2': interview.score_teacher2,
                'scoreTeacher3': interview.score_teacher3,
                'normalizedScore': interview.normalized_score,
                'resumeScore': interview.resume_score
            }
            for interview in Interview.objects.all().order_by('-normalized_score')
        ]

        return JsonResponse(data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)