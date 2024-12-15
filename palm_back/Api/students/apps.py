from django.apps import AppConfig



class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api.students'  # 确保这里正确引用了应用路径