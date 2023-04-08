import sqlite3
import traceback

import matplotlib.pyplot as plt
import numpy as np
from django.db.models import Max
from django.views.decorators.csrf import csrf_protect
import json

from . import models

from .serializers import *
from django.http import JsonResponse

# Create your views here.


def index(request):  # 主页面功能实现及调用
    stu_id = request.session.get('ID')
    print(stu_id)
    if stu_id is None:
        return JsonResponse({
            'code': 403,
            'msg': '用户没有登录'
        })
    max_score_list = max_Score()
    m1 = max_score_list[0]
    m2 = max_score_list[1]
    m3 = max_score_list[2]
    m4 = max_score_list[3]
    m5 = max_score_list[4]
    try:
        std = Early_Warning.objects.get(id=stu_id)
    except Exception as err:
        print(err)
        return JsonResponse({
            'code': 500,
            'msg': '该学生在学业预警信息表中无记录',
        })

    graduation_req = std.grad_req_id
    if std.minimum >= graduation_req.credit and std.compulsory >= graduation_req.compulsory \
            and std.elective >= graduation_req.elective and std.physical >= graduation_req.physical \
            and std.cet4 >= graduation_req.cet4 and std.mandarin >= graduation_req.mandarin:
        ans = '满足毕业最低要求'
    else:
        ans = '不满足毕业最低要求'
    return JsonResponse({
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'm1': m1,
            'm2': m2,
            'm3': m3,
            'm4': m4,
            'm5': m5,
            'ans': ans
        }
    })


def get_score_std(request):
    num_all = Score.objects.all().count()
    num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
    rate = int((num_pass / num_all) * 100)
    zh = Score.objects.filter(zy__gte=60).count()
    ch = Score.objects.filter(cx__gte=60).count()
    know = Score.objects.filter(zs__gte=60).count()
    gl = Score.objects.filter(gl__gte=60).count()

    return JsonResponse({
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'num_all': num_all,
            'num_pass': num_pass,
            'rate': rate,
            'zh': zh,
            'ch': ch,
            'know': know,
            'gl': gl
        }
    })


def infor(request):  # 获取用户个人信息数据的接口
    stu_id = request.session.get('ID')
    print(stu_id)
    if stu_id is None:
        return JsonResponse({
            'code': 403,
            'msg': '获取数据失败，没有登录',
        })
    try:
        std = Student.objects.get(id=stu_id)
    except Exception as err:
        print(err)
        return JsonResponse({
            'code': 500,
            'msg': '用户不存在'
        })
    age = std.age
    sp = std.sp
    pwd = std.pwd
    return JsonResponse({
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'age': age,
            'sp': sp,
            'pwd': pwd
        }
    })


def password_change_form(request):  # 用户信息页面功能实现及调用
    stu_id = request.session.get('ID')
    if stu_id is None:
        return JsonResponse({
            'code': 403,
            'msg': '操作失败，没有登录',
            'data': {}
        })
    try:
        e = Student.objects.get(id=stu_id)
    except Exception as err:
        return JsonResponse({
            'code': 500,
            'msg': '用户不存在'
        })
    status = 0
    msg = '请使用POST方法'
    if request.method == 'POST':
        post_data = json.loads(request.body)
        opwd = post_data['old_password']
        npwd1 = post_data['new_password1']
        npwd2 = post_data['new_password2']
        if opwd != "":
            opwd = int(opwd)
        if npwd1 != "":
            npwd1 = int(npwd1)
        if npwd2 != "":
            npwd2 = int(npwd2)
        print(opwd, npwd1, npwd2)
        print(type(opwd))
        pwd = e.pwd
        print(id, pwd)
        print(type(pwd))
        if opwd == pwd:
            if npwd1 == '' or npwd2 == '':
                status = 1
                msg = "您的新密码与确认密码存在空值，请仔细检查重新输入"
            else:
                if npwd1 == npwd2:
                    if opwd == npwd1:
                        status = 2
                        msg = "您的新密码与旧密码一致，请仔细检查重新输入"
                    else:
                        e.pwd = npwd1
                        e.save()
                        status = 3
                        msg = "密码修改成功，请您重新登录！"
                else:
                    status = 4
                    msg = "您的新密码与确认密码不一致，请仔细检查重新输入"
        else:
            status = 5
            msg = "您的旧密码输入错误，请仔细检查重新输入"
    return JsonResponse({
        'code': 200,
        'msg': '操作成功',
        'data': {
            'status': status,
            'msg': msg
        }
    })


def shenhe_upload(request):  # 上传审核材料接口
    stu_id = request.session.get('ID')
    name = request.session.get('name')
    if stu_id is None:
        return JsonResponse({
            'code': 403,
            'msg': '操作失败，没有登录',
        })
    print(stu_id)
    code = 405
    status = 0
    msg = '请使用POST方法'
    if request.method == "POST":
        code = 200
        post_data = json.loads(request.body)
        file = post_data['image']
        file_name = str(file)
        print(file_name)
        if file and (
                file_name.lower().endswith(
                    ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))):
            models.shenhe.objects.create(no=stu_id, miaoshu=post_data['miaoshu'], leibie=post_data['leibie'],
                                         image=file)
            status = 1
            msg = '上传审核材料成功'
        else:
            status = 2
            msg = '文件上传错误，文件为空或文件格式不正确'
    return JsonResponse({
        'code': code,
        'msg': msg,
        'status': status
    })


def shenhe_get(request):
    stu_id = request.session.get('ID')
    name = request.session.get('name')
    if stu_id is None:
        return JsonResponse({
            'code': 403,
            'msg': '操作失败，没有登录',
        })
    shenhe_list_obj = models.shenhe.objects.filter(no=stu_id)
    shenhe_list = ShenHeSerializer(instance=shenhe_list_obj, many=True)

    return JsonResponse({
        'code': 200,
        'msg': '获取审核材料数据成功',
        'data': {
            'shenhe_list': shenhe_list.data,  # 需要加上.data
            'stu_id': stu_id,
            'name': name
        }
    })


def shenhe_delete(request):  # 删除审核材料功能实现
    stu_id = request.session.get('ID')
    if stu_id is None:
        return JsonResponse({
            'code': 403,
            'msg': '操作失败，没有登录',
        })
    msg = '请使用GET方法'
    status = 0
    if request.method == 'GET':
        shenhe_id = request.GET.get('id')
        models.shenhe.objects.filter(id=shenhe_id).delete()
        msg = '删除审核材料成功'
        status = 1
    return JsonResponse({
        'code': 200,
        'msg': msg,
        'status': status
    })


# @csrf_protect
# 登录界面
def login(request):  # 登录页面功能实现
    code = 405
    status = 0
    msg = '操作失败，请使用POST方法！'
    if request.method == 'POST':
        code = 200
        print("进入页面")
        post_body = json.loads(request.body)
        print(post_body)
        stu_id = post_body['stu_id']
        pwd = post_body['pwd']
        print('stu_id: ' + stu_id)
        print('pwd: ' + pwd)
        if stu_id.isdigit():
            try:
                student = Student.objects.get(id=stu_id, pwd=pwd)
                print('登录成功')
                msg = '登录成功！'
                status = 1
                request.session['ID'] = student.id
                request.session['name'] = student.name
            except Exception as err:
                print(err)
                msg = '学号或密码错误！'
                status = 2
        else:
            msg = '学号必须全为数字！'
            status = 3
    return JsonResponse({
        'code': code,
        'msg': msg,
        'status': status
    })


def academic_Early_Warning(request):  # 学业预警页面功能实现及调用
    stu_id = request.session.get('ID')
    print(stu_id)
    std = Early_Warning.objects.get(id=stu_id)
    graduation_req = std.grad_req_id
    num_all = Early_Warning.objects.all().count()
    num_pass = Early_Warning.objects.filter(minimum__gte=graduation_req.credit,
                                            compulsory__gte=graduation_req.compulsory,
                                            elective__gte=graduation_req.elective,
                                            physical__gte=graduation_req.physical,
                                            cet4__gte=graduation_req.cet4,
                                            mandarin__gte=graduation_req.mandarin).count()
    rate = int((num_pass / num_all) * 100)
    minimum = std.minimum
    compulsory = std.compulsory
    elective = std.elective
    physical = std.physical
    cet4 = std.cet4
    mandarin = std.mandarin
    return JsonResponse({
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'num_all': num_all,
            'num_pass': num_pass,
            'rate': rate,
            'minimum': minimum,
            'compulsory': compulsory,
            'elective': elective,
            'physical': physical,
            'cet4': cet4,
            'mandarin': mandarin
        }
    })


def max_Score():  # 主页面最高成绩展示功能实现
    max_score_list = list()
    m1 = Score.objects.aggregate(max1=Max("zy"))
    m2 = Score.objects.aggregate(max2=Max("cx"))
    m3 = Score.objects.aggregate(max3=Max("zs"))
    m4 = Score.objects.aggregate(max4=Max("gl"))
    m5 = Score.objects.aggregate(max5=Max("zh"))
    value1 = list(m1.values())[0]
    value2 = list(m2.values())[0]
    value3 = list(m3.values())[0]
    value4 = list(m4.values())[0]
    value5 = list(m5.values())[0]
    max_score_list.append(value1)
    max_score_list.append(value2)
    max_score_list.append(value3)
    max_score_list.append(value4)
    max_score_list.append(value5)
    print(max_score_list)
    return max_score_list


def form_editor(request):  # 评分准则页面调用
    name = request.session.get('name')
    print(name)
    return JsonResponse({
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'name': name
        }
    })


def select(i):  # 主页面雷达图成绩展示功能实现
    conn = sqlite3.connect('db.sqlite3')
    cursor0 = conn.cursor()
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor3 = conn.cursor()
    cursor4 = conn.cursor()
    S = Score.objects.get(id=i)
    avg_zy = cursor0.execute("SELECT AVG(zy) FROM Score")
    avg_cx = cursor1.execute("SELECT AVG(cx) FROM Score")
    avg_zs = cursor2.execute("SELECT AVG(zs) FROM Score")
    avg_gl = cursor3.execute("SELECT AVG(gl) FROM Score")
    avg_zh = cursor4.execute("SELECT AVG(zh) FROM Score")
    avg_zy = avg_zy.fetchone()[0]
    avg_cx = avg_cx.fetchone()[0]
    avg_zs = avg_zs.fetchone()[0]
    avg_gl = avg_gl.fetchone()[0]
    avg_zh = avg_zh.fetchone()[0]
    results = [{"专业技术": S.zy, "创新创业": S.cx, "知识学习": S.zs, "管理实践": S.gl, "综合发展": S.zh},
               {"专业技术": avg_zy, "创新创业": avg_cx, "知识学习": avg_zs, "管理实践": avg_gl, "综合发展": avg_zh}]
    data_length = len(results[0])
    angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    score = [[v for v in result.values()] for result in results]
    score_a = np.concatenate((score[0], [score[0][0]]))
    score_b = np.concatenate((score[1], [score[1][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    fig = plt.figure(figsize=(15, 6), dpi=100)
    fig.suptitle("XXXX专业")
    ax1 = plt.subplot(121, polar=True)
    ax2 = plt.subplot(122, polar=True)
    ax, data, name = [ax1, ax2], [score_a, score_b], ["个人", "平均"]
    for i in range(2):
        for j in np.arange(0, 100 + 20, 20):
            ax[i].plot(angles, 6 * [j], '-.', lw=0.5, color='black')
        for j in range(5):
            ax[i].plot([angles[j], angles[j]], [0, 100], '-.', lw=0.5, color='black')
        ax[i].plot(angles, data[i], color='b')
        # 隐藏最外圈的圆
        ax[i].spines['polar'].set_visible(False)
        # 隐藏圆形网格线
        ax[i].grid(False)
        for a, b in zip(angles, data[i]):
            ax[i].text(a, b + 5, '%.00f' % b, ha='center', va='center', fontsize=12, color='b')
        ax[i].set_thetagrids(angles * 180 / np.pi, labels)
        ax[i].set_theta_zero_location('N')
        ax[i].set_rlim(0, 100)
        ax[i].set_rlabel_position(0)
        ax[i].set_title(name[i])
    # 汉字字体，优先使用楷体，找不到则使用黑体
    plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
    # 正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # plt.show()
    plt.savefig("static\\image\\1.png", format='png')


def suggestion(request, p1):
    print(p1)
    stu_id = request.session.get('ID')
    name = request.session.get('name')
    try:
        e = Score.objects.get(id=stu_id)
    except Exception as err:
        print(err)
        return JsonResponse({
            'code': 500,
            'msg': '用户不存在'
        })
    print(stu_id)
    if p1 == 1:
        print(e.zy)
        g = grade(e.zy)
        print(g)
    elif p1 == 2:
        g = grade(e.cx)
        print(e.cx)
        print(g)
    elif p1 == 3:
        g = grade(e.zs)
        print(e.zs)
        print(g)
    elif p1 == 4:
        g = grade(e.gl)
        print(e.gl)
        print(g)
    else:
        g = grade(e.zh)
        print(e.zh)
        print(g)
    return JsonResponse({
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'grade': g,
            'name': name
        }
    })


def grade(i):

    if i >= 80:
        the_grade = 'A'
    elif i >= 60:
        the_grade = 'B'
    else:
        the_grade = 'C'

    return the_grade
