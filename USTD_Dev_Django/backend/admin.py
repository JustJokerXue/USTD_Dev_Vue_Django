from backend.models import Early_Warning
# Register your models here.
from backend.models import Innovation, majorTechnology, manage, ComprehensiveDevelopment, responsible, \
    administrator
from backend.models import Knowledge
from backend.models import Score
from backend.models import Student
from backend.models import shenhe
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe


@admin.register(Early_Warning)
class Early_WarningAdmin(admin.ModelAdmin):  # 学业预警成绩表后台布局设计
    list_display = ('id', 'minimum', 'compulsory', 'elective', 'physical', 'cet4', 'mandarin')
    list_display_links = ("id",)
    search_fields = ('id',)  # 查找
    list_per_page = 20
    list_editable = ('minimum', 'compulsory', 'elective', 'physical', 'cet4', 'mandarin')
    # list_filter = ("id", "sp")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):  # 学生用户信息表后台布局设计
    list_display = ('id', 'name', 'age', 'sp', 'pwd')
    list_display_links = ("id",)
    search_fields = ('id', 'name')  # 查找
    list_per_page = 20
    list_editable = ('name', 'age', 'sp', 'pwd')
    list_filter = ("id", "sp")


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):  # 学生五大方面评分表后台布局设计
    list_display = ('id', 'zy', 'cx', 'zs', 'gl', 'zh')
    list_display_links = ("id",)
    search_fields = ('id',)  # 查找
    list_per_page = 20
    list_editable = ('zy', 'cx', 'zs', 'gl', 'zh')


@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):  # 学生知识学习评分表后台布局设计
    list_display = ('name', 'sno', 'java', 'dataStructure', 'Gaverage')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'java', 'dataStructure', 'Gaverage')


@admin.register(Innovation)
class InnovationAdmin(admin.ModelAdmin):  # 学生创新创业评分表后台布局设计
    list_display = ('name', 'sno', 'ContestRating', 'PatentRcoring', 'EntrepreneurialAchievement')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'ContestRating', 'PatentRcoring', 'EntrepreneurialAchievement')


@admin.register(majorTechnology)
class majorTechnologyAdmin(admin.ModelAdmin):  # 学生专业技术评分白后台布局设计
    list_display = ('name', 'sno', 'ProjectPractice', 'PaperGrading', 'StudentTutor')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'ProjectPractice', 'PaperGrading', 'StudentTutor')


@admin.register(manage)
class manageAdmin(admin.ModelAdmin):  # 学生管理实践评分表后台布局设计
    list_display = ('name', 'sno', 'community', 'StudentWork', 'ProjectTeam')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'community', 'StudentWork', 'ProjectTeam')


@admin.register(ComprehensiveDevelopment)
class ComprehensiveDevelopmentAdmin(admin.ModelAdmin):  # 学生综合发展评分表后台布局设计
    list_display = ('name', 'sno', 'physical', 'Volunteer', 'Labor', 'morality')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'physical', 'Volunteer', 'Labor', 'morality')


@admin.register(responsible)
class responsibleAdmin(admin.ModelAdmin):  # 负责人用户信息表后台布局设计
    list_display = ('name', 'Employeeno', 'password')
    list_display_links = ("Employeeno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'password')


@admin.register(administrator)
class administratorAdmin(admin.ModelAdmin):  # 管理员用户信息表后台布局设计
    list_display = ('name', 'Employeeno', 'password')
    list_display_links = ("Employeeno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'password')


@admin.register(shenhe)
# admin.site.register(要写的表)  与  @admin.register(要写的表)  功能是一样的
class shenheAdmin(admin.ModelAdmin):  # 上传审核材料汇总表后台布局设计
    list_display = ('no', 'miaoshu', 'leibie', 'image', 'image_img', 'zhuangtai')
    list_display_links = ("no",)
    search_fields = ('no',)  # 查找
    list_per_page = 20
    list_filter = ("no", "leibie")
    actions = ['mak_pub', 'mak_pub1', 'operate']

    # 判断通过的
    def mak_pub(self, request, queryset):
        for item in queryset:
            print(item)
            item.zhuangtai = 'T'
            item.save()

    # 更改Action的内容为通过
    mak_pub.short_description = "通过"

    # 判断未通过的
    def mak_pub1(self, request, queryset):
        for item in queryset:
            print(item)
            item.zhuangtai = 'F'
            item.save()

    # 更改Action的内容为通过
    mak_pub1.short_description = "未通过"


admin.site.site_header = '大学生发展综合素质测评系统管理后台'  # 设置header
admin.site.site_title = '大学生发展综合素质测评系统管理后台'  # 设置title
admin.site.index_title = '大学生发展综合素质测评系统管理后台'
