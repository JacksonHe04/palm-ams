from django.db import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse
from .models import Apply
from django.core.exceptions import ObjectDoesNotExist
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def apply_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # 提取基本字段
            id = data.get('id')
            name = data.get('name')
            graduationYear = data.get('graduationYear')
            gender = data.get('gender')
            birthDate = data.get('birthDate')
            photo = data.get('photo')
            university = data.get('university')
            major = data.get('major')
            majorCount = data.get('majorCount')
            rank = data.get('rank')
            percentage = data.get('percentage')
            masterUniversity = data.get('masterUniversity')
            masterMajor = data.get('masterMajor')
            tutor = data.get('tutor')
            phone = data.get('phone')
            email = data.get('email')
            applicationType = data.get('applicationType')
            firstChoice = data.get('firstChoice')
            secondChoice = data.get('secondChoice')
            thirdChoice = data.get('thirdChoice')
            isAdjustable = data.get('isAdjustable')
            proofs = data.get('proofs')
            status = data.get('status')

            # 提取 papers 数组
            papers = data.get('papers', [])
            paper1 = papers[0] if len(papers) > 0 else {}
            paper2 = papers[1] if len(papers) > 1 else {}
            paper3 = papers[2] if len(papers) > 2 else {}

            # 提取 awards 数组
            awards = data.get('awards', [])
            award1 = awards[0] if len(awards) > 0 else {}
            award2 = awards[1] if len(awards) > 1 else {}
            award3 = awards[2] if len(awards) > 2 else {}

            # 创建或更新 apply 对象
            apply_obj, created = Apply.objects.update_or_create(
                id=id,
                defaults={
                    'name': name,
                    'graduationYear': graduationYear,
                    'gender': gender,
                    'birthDate': birthDate,
                    'photo': photo,
                    'university': university,
                    'major': major,
                    'majorCount': majorCount,
                    'rank': rank,
                    'percentage': percentage,
                    'masterUniversity': masterUniversity,
                    'masterMajor': masterMajor,
                    'tutor': tutor,
                    'phone': phone,
                    'email': email,
                    'applicationType': applicationType,
                    'firstChoice': firstChoice,
                    'secondChoice': secondChoice,
                    'thirdChoice': thirdChoice,
                    'isAdjustable': isAdjustable,
                    'proofs': proofs,
                    'status': status,

                    # papers 字段
                    'paper1_publicationTime': paper1.get('publicationTime'),
                    'paper1_journalConference': paper1.get('journalConference'),
                    'paper1_paperName': paper1.get('paperName'),
                    'paper1_ccfLevel': paper1.get('ccfLevel'),
                    'paper1_awardCategory': paper1.get('awardCategory'),

                    'paper2_publicationTime': paper2.get('publicationTime'),
                    'paper2_journalConference': paper2.get('journalConference'),
                    'paper2_paperName': paper2.get('paperName'),
                    'paper2_ccfLevel': paper2.get('ccfLevel'),
                    'paper2_awardCategory': paper2.get('awardCategory'),

                    'paper3_publicationTime': paper3.get('publicationTime'),
                    'paper3_journalConference': paper3.get('journalConference'),
                    'paper3_paperName': paper3.get('paperName'),
                    'paper3_ccfLevel': paper3.get('ccfLevel'),
                    'paper3_awardCategory': paper3.get('awardCategory'),

                    # awards 字段
                    'award1_isLeader': award1.get('isLeader'),
                    'award1_awardTime': award1.get('awardTime'),
                    'award1_awardName': award1.get('awardName'),
                    'award1_levelRanking': award1.get('levelRanking'),
                    'award1_awardRanking': award1.get('awardRanking'),

                    'award2_isLeader': award2.get('isLeader'),
                    'award2_awardTime': award2.get('awardTime'),
                    'award2_awardName': award2.get('awardName'),
                    'award2_levelRanking': award2.get('levelRanking'),
                    'award2_awardRanking': award2.get('awardRanking'),

                    'award3_isLeader': award3.get('isLeader'),
                    'award3_awardTime': award3.get('awardTime'),
                    'award3_awardName': award3.get('awardName'),
                    'award3_levelRanking': award3.get('levelRanking'),
                    'award3_awardRanking': award3.get('awardRanking'),

                    'universityLevel': data.get('universityLevel'),
                    'masterUniversityLevel': data.get('masterUniversityLevel'),
                }
            )

            response_data = {
                'message': '申请表单提交成功',
                'data': {
                    'id': apply_obj.id,
                    'status': apply_obj.status
                }
            }

            return JsonResponse(response_data, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def test_get(request):
    return JsonResponse({'message': 'This is a test GET request'})