# views.py
from django.shortcuts import render
from django.http import JsonResponse
from Api.apply.models import Apply

# Create your views here.



def get_students(request):
    applies = Apply.objects.all()
    students_data = []

    for apply in applies:
        student_data = {
            "id": apply.id,
            "name": apply.name,
            "graduationYear": apply.graduationYear,
            "gender": apply.gender,
            "birthDate": apply.birthDate,
            "photo": apply.photo.url if apply.photo else None,
            "university": apply.university,
            "major": apply.major,
            "majorCount": apply.majorCount,
            "rank": apply.rank,
            "percentage": apply.percentage,
            "masterUniversity": apply.masterUniversity,
            "masterMajor": apply.masterMajor,
            "tutor": apply.tutor,
            "phone": apply.phone,
            "email": apply.email,
            "applicationType": apply.applicationType,
            "firstChoice": apply.firstChoice,
            "secondChoice": apply.secondChoice,
            "thirdChoice": apply.thirdChoice,
            "isAdjustable": apply.isAdjustable,
            "papers": [
                {
                    "publicationTime": apply.paper1_publicationTime,
                    "journalConference": apply.paper1_journalConference,
                    "paperName": apply.paper1_paperName,
                    "ccfLevel": apply.paper1_ccfLevel,
                    # "awardCategory": apply.paper1_awardCategory
                },
                {
                    "publicationTime": apply.paper2_publicationTime,
                    "journalConference": apply.paper2_journalConference,
                    "paperName": apply.paper2_paperName,
                    "ccfLevel": apply.paper2_ccfLevel,
                    # "awardCategory": apply.paper2_awardCategory
                },
                {
                    "publicationTime": apply.paper3_publicationTime,
                    "journalConference": apply.paper3_journalConference,
                    "paperName": apply.paper3_paperName,
                    "ccfLevel": apply.paper3_ccfLevel,
                    # "awardCategory": apply.paper3_awardCategory
                }
            ],
            "awards": [
                {
                    "isLeader": apply.award1_isLeader,
                    "awardTime": apply.award1_awardTime,
                    "awardName": apply.award1_awardName,
                    "levelRanking": apply.award1_levelRanking,
                    "awardRanking": apply.award1_awardRanking
                },
                {
                    "isLeader": apply.award2_isLeader,
                    "awardTime": apply.award2_awardTime,
                    "awardName": apply.award2_awardName,
                    "levelRanking": apply.award2_levelRanking,
                    "awardRanking": apply.award2_awardRanking
                },
                {
                    "isLeader": apply.award3_isLeader,
                    "awardTime": apply.award3_awardTime,
                    "awardName": apply.award3_awardName,
                    "levelRanking": apply.award3_levelRanking,
                    "awardRanking": apply.award3_awardRanking
                }
            ],

            "universityLevel": apply.universityLevel,
            "masterUniversityLevel": apply.masterUniversityLevel,
            "resume": None,  # 假设没有 resume 字段，如果有请添加
            "proofs": apply.proofs,
            "status": apply.status
        }
        students_data.append(student_data)

    return JsonResponse(students_data, safe=False)
