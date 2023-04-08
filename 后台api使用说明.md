## api使用说明
1. `/login`  判断用户名和密码是否正确
   * 请求方法：POST
   * 是否需要登录：否
   * 请求参数：json格式数据 `{stu_id: xxx, pwd: xxx}`
   * 响应的json数据格式：`{'code': xxx, 'msg': xxx, 'status': xxx}`
     * 学号和密码正确：`code=200, msg='登录成功！', status=1`
     * 学号或密码错误：`code=200, msg='学号或密码错误！', status=2`
     * 学号中不全是数字：`code=200, msg='学号必须全为数字！', status=3`
     * 使用了GET方法：`code=405, msg='操作失败，请使用POST方法！', status=0`
2. `/login/index`    获取登录后的主页面中的数据
   
   * 请求方法：GET/POST
   * 是否需要登录：是
   * 请求参数：无
   * 响应的json数据格式： 
   ``` json
   {
        "code": xxx,
        "msg": 'xxx',
        "data": {
            "m1": xxx, // 专业技术能力最高分
            "m2": xxx, // 创新创业能力最高分
            "m3": xxx, // 知识学习能力最高分
            "m4": xxx, // 管理实践能力最高分
            "m5": xxx, // 综合发展能力最高分
            "ans": xxx // 学业预警情况：'满足/不满足毕业最低要求'
        }
    }
   ```
   * 返回数据的可能情况：
     * 用户没登录： `code=403, msg='用户没有登录', 无data`
     * 没有学业预警信息： `code=500, msg='该学生在学业预警信息表中无记录', 无data`
     * 成功返回： `code=200, msg='获取数据成功', data={...}`
3. `/login/infor`   获取用户个人信息
   
   * 请求方法：GET/POST
   * 是否需要登录：是
   * 请求参数：无
   * 响应的json数据格式：
   ``` json
   {
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'age': age, // 年龄
            'sp': sp,   // 
            'pwd': pwd  // 密码
        }
   }
   ```
   * 返回数据的可能情况：
     * 用户没有登录： `code=403, msg='获取数据失败，没有登录'`
     * 用户不存在： `code=500, msg='用户不存在'`
     * 成功返回： `code=200, msg='获取数据成功', data={...}`
4. `/shenhe_delete`   删除审核材料数据
   
   * 请求方法：GET
   * 是否需要登录：是
   * 请求参数：id
   * 响应的json数据格式：
   ``` json
   {
        'code': xxx,
        'msg': xxx,
        'status': xxx
    }
   ```
   * 返回数据的可能情况：
     * 用户没有登录： `code=403, msg='操作失败，没有登录'`
     * 请求参数不符合要求：`code=501, msg='请求参数为空或不符合要求'`
     * 请求方法错误： `code=405, msg='请使用GET方法', status=0`
     * 删除失败：`code=500, msg='删除审核材料失败，没有该id对应的审核材料', status=2`
     * 成功返回： `code=200, msg='删除审核材料成功', status=1`
5. `/login/form-editors`   # 评分准则页面调用
   
   * 请求方法：GET/POST
   * 是否需要登录：是
   * 请求参数：无
   * 响应的json数据格式：
   ``` json
   {
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'name': name
        }
    }
   ```
   * 只有一种情况
6. `/login/shenhe_upload`   上传审核材料接口
   
   * 请求方法：POST
   * 是否需要登录：是
   * 请求参数：json数据  `{'miaoshu': xxx(描述信息), 'leibie': xxx(类别), 'extra_points': xxx(加分值), 'image': xxx(图片)}`
   * 响应的json数据格式：
   ``` json
    {
        'code': xxx,
        'msg': xxx,
        'status': xxx
    }
   ```
   * 返回数据的可能情况：
     * 用户没有登录： `code=403, msg='操作失败，没有登录'`
     * 请求方法不对： `code=405, msg='请使用POST方法', status=0`
     * 请求参数不符合要求： `code=501, msg='请求参数为空或不符合要求！'`
     * 图片文件格式不对： `code=200, msg='文件上传错误，文件为空或文件格式不正确', status=2`
     * 成功返回： `code=200, msg='上传审核材料成功', status=1`
7. `/login/shenhe_get`   获取审核材料数据交口
    
    * 请求方法：GET/POST
    * 是否需要登录：是
    * 请求参数：无
   * 响应的json数据格式：
   ``` json
    {
        'code': xxx,
        'msg': 'xxx',
        'data': {
            'shenhe_list': [// 审核材料列表
                {
                    "id": xxx,
                   "no": xxx,
                   "miaoshu": "xxx",
                   "leibie": "xxx",
                   "extra_points": xxx,
                   "image": xxx(url),
                   "zhuangtai": "xxx"
                },
                ...
            ],  
            'stu_id': xxx, // 学号
            'name': xxx    // 姓名
        }
    }
   ```
   * 返回数据的可能情况：
     * 用户没有登录： `code=403, msg='操作失败，没有登录'`
     * 成功返回： `code=200, msg='获取审核材料数据成功', data={...}`
8. `/login/Academic_Early_Warning`   学业预警功能接口
   
   * 请求方法：GET/POST
   * 是否需要登录：是
   * 请求参数：无
   * 响应的json数据格式：
    ``` json
    {
        'code': xxx,
        'msg': 'xxx',
        'data': {
            'num_all': xxx, // 总人数
            'num_pass': xxx, // 总达标人数
            'rate': xxx, // 达标率
            'minimum': xxx, // 该学生已修学分
            'compulsory': xxx, // 该学生必修课成绩
            'elective': xxx, // 该学生选修课成绩
            'physical': xxx, // 体测成绩
            'cet4': xxx, // 四级成绩
            'mandarin': xxx, // 普通话成绩
            'graduation_req': { // 该学生所在专业的学业要求
                'id': xxx,
                'credit': xxx, // 专业学分要求
                'compulsory': xxx, // 必修课成绩要求
                'elective': xxx, // 选修课成绩要求
                'physical': xxx, // 体侧成绩要求
                'cet4': xxx, // 四级成绩要求
                'mandarin': xxx // 普通话成绩要求
            }
        }
    }
    ```
   * 返回数据的可能情况：
     * 用户没有登录： `code=403, msg='msg': '操作失败，没有登录'`
     * 没有学业预警信息： `code=500, msg='msg': '该学生没有学业预警信息'`
     * 成功返回： `code=200, msg='获取数据成功', data={...}`
     * 
9. `/login/password_change_form`   更改密码的接口
   
   * 请求方法：POST
   * 是否需要登录：是
   * 请求参数：json格式数据： `{'old_password': xxx, 'new_password1': xxx, 'new_password2': xxx}`
   * 响应的json数据格式：
    ``` json
    {
        'code': xxx,
        'msg': xxx,
        'status': xxx
    }
    ```
   * 返回数据的可能情况：
     * 没有登录： `code=403, msg='操作失败，没有登录'`
     * 用户不存在： `code=500, msg='用户不存在'`
     * 请求方法错误： `code=405, msg='请使用POST方法', status=0`
     * 请求参数不符合要求： `code=501, msg='请求参数为空或不符合要求！'`
     * `code=200, msg="您的新密码与确认密码存在空值，请仔细检查重新输入", status=1`
     * `code=200, msg="您的新密码与旧密码一致，请仔细检查重新输入", status=2`
     * `code=200, msg="密码修改成功，请您重新登录！", status=3`
     * `code=200, msg="您的新密码与确认密码不一致，请仔细检查重新输入", status=4`
     * `code=200, msg="您的旧密码输入错误，请仔细检查重新输入", status=5`
10. `/login/suggestion/<int:p1>`   发展方向建议接口
    
    * 请求方法：GET/POST
    * 是否需要登录：是
    * 不同的p1对应的返回数据：
    ```text
    p1=1:  专业技术能力
    p1=2:  创新创业能力
    p1=3:  知识学习能力
    p1=4:  管理实践能力
    p1=5:  综合发展能力
    ```
    * 请求参数：无
    * 响应的json数据格式：
    ``` json
    {
        'code': xxx,
        'msg': 'xxx',
        'data': {
            'grade': xxx, // 对应能力等级
            'name': xxx // 学生姓名
        }
    }
    ```
    * 返回数据的可能情况：
      * 用户不存在： `code=500, msg='用户不存在'`
      * 成功返回： `code=200, msg='获取数据成功', data={...}`
11. `/api/get_score_std`   获取五大方面的详情数据接口
    
    * 请求方法：GET/POST
    * 是否需要登录：否
    * 请求参数：无
    * 响应的json数据格式：
    ``` json
    {
        'code': 200,
        'msg': '获取数据成功',
        'data': {
            'num_all': num_all, // 总人数
            'num_pass': num_pass, // 总达标人数
            'rate': rate, // 达标率
            'zy': zy, // 专业技术能力达标人数
            'cx': cx, // 创新创业能力达标人数
            'zs': zs, // 知识学习能力达标人数
            'gl': gl, // 管理实践能力达标人数
            'zh': zh  // 综合发展能力达标人数
        }
    }
    ```
    * 只有上述一种情况