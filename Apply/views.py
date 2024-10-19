from django.shortcuts import render
from .models import PalmApplicant
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ApplicationSystem.settings import MEDIA_ROOT #导入上传文件保存路径 或 from django.conf import settings
from django.utils import timezone
import pytz
import os
# Create your views here.


def index(request):
    return render(request, 'EnrollmentWebsite.html')


def palm(request):
    #首先判断request的方式
    if request.method == "POST":
        applicant = PalmApplicant()
        #通过request的get()函数，获得提交的值
        tz = pytz.timezone('Asia/Shanghai')
        now_time = timezone.now().astimezone(tz=tz)
        applicant.submit_time = now_time.strftime("%Y.%m.%d %H.%M:%S")
        applicant.name_input = request.POST.get('name_input','') #当属性值不存在，则赋空值
        applicant.sex_input  = request.POST.get('sex_input','')
        applicant.birthday = request.POST.get('birthday','') 
        applicant.province = request.POST.get('province','') 
        applicant.city = request.POST.get('city','') 
        applicant.district = request.POST.get('district','') 
        applicant.undergraduate_university_input = request.POST.get('undergraduate_university_input','')
        applicant.major_input = request.POST.get('major_input','')
        applicant.master_university_input = request.POST.get('master_university_input','')
        applicant.mastertutor_input = request.POST.get('mastertutor_input','')
        applicant.gradepeople_input = request.POST.get('gradepeople_input','')
        applicant.grade_input = request.POST.get('grade_input','')    
        applicant.phonenumber_input = request.POST.get('phonenumber_input','') 
        applicant.email_input = request.POST.get('email_input','')
        applicant.registrationtype_input  = request.POST.get('registrationtype_input','')
        applicant.tutor_input_first = request.POST.get('tutor_input_first','') 
        applicant.tutor_input_second = request.POST.get('tutor_input_second','') 
        applicant.tutor_input_third = request.POST.get('tutor_input_third','') 
        applicant.ajustment_input = request.POST.get('ajustment_input','')
        applicant.time_paper1 = request.POST.get('time_paper1','')
        applicant.journal_name1 = request.POST.get('journal_name1','')
        applicant.paper_name1 = request.POST.get('paper_name1','')
        applicant.time_paper2 = request.POST.get('time_paper2','')
        applicant.journal_name2 = request.POST.get('journal_name2','')
        applicant.paper_name2 = request.POST.get('paper_name2','')
        applicant.time_paper3 = request.POST.get('time_paper3','')
        applicant.journal_name3 = request.POST.get('journal_name3','')
        applicant.paper_name3 = request.POST.get('paper_name3','')
        applicant.time_award1 = request.POST.get('time_award1','')
        applicant.award_grade1 = request.POST.get('award_grade1','')
        applicant.award_name1 = request.POST.get('award_name1','')
        applicant.time_award2 = request.POST.get('time_award2','')
        applicant.award_grade2 = request.POST.get('award_grade2','')
        applicant.award_name2 = request.POST.get('award_name2','')
        applicant.time_award3 = request.POST.get('time_award3','')
        applicant.award_grade3 = request.POST.get('award_grade3','')
        applicant.award_name3 = request.POST.get('award_name3','')
        applicant.time_award4 = request.POST.get('time_award4','')
        applicant.award_grade4 = request.POST.get('award_grade4','')
        applicant.award_name4 = request.POST.get('award_name4','')
        applicant.time_award5 = request.POST.get('time_award5','')
        applicant.award_grade5 = request.POST.get('award_grade5','')
        applicant.award_name5 = request.POST.get('award_name5','')
        applicant.statement_input = request.POST.get('statement_input','')
        applicant.researchplan_input = request.POST.get('researchplan_input','')
        
        pic=request.FILES['photo']
        ext = os.path.splitext(pic.name)[1]
        photoname = applicant.name_input + ext
        save_path="%s/Apply/%s"%(MEDIA_ROOT,photoname)
        with open(save_path,'wb') as f:
            for content in pic.chunks():
                f.write(content)
        applicant.photo = 'Apply/%s'%photoname

        applicant.save()
        return HttpResponseRedirect("http://palm.seu.edu.cn")

    return render(request, 'EnrollmentWebsite.html')

