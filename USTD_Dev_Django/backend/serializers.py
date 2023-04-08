from rest_framework import serializers
from .models import Student, GraduationRequirement, Early_Warning, Score, Knowledge, \
    Innovation, majorTechnology, manage, ComprehensiveDevelopment, shenhe


class StudentSerializer(serializers.ModelSerializer):   # 学生信息表序列化器
    class Meta:
        model = Student
        fields = '__all__'


class GraduationRequirementSerializer(serializers.ModelSerializer):  # 毕业要求表
    class Meta:
        model = GraduationRequirement
        fields = '__all__'


class EarlyWarningSerializer(serializers.ModelSerializer):  # 学业预警信息表
    class Meta:
        model = Early_Warning
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):  # 学生课程分数表
    class Meta:
        model = Score
        fields = '__all__'


class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'


class InnovationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Innovation
        fields = '__all__'


class MajorTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = majorTechnology
        fields = '__all__'


class ManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = manage
        fields = '__all__'


class ComprehensiveDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprehensiveDevelopment
        fields = '__all__'


class ShenHeSerializer(serializers.ModelSerializer):
    class Meta:
        model = shenhe
        fields = '__all__'


