<template>
  <div>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">
    <meta content="Admin Dashboard" name="description">
    <meta content="Mannatthemes" name="author">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link href="../../static/css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <link href="../../static/css/icons.css" rel="stylesheet" type="text/css">
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css">
    <!-- Loader -->
    <!-- Navigation Bar-->
    <header id="topnav">
      <div class="topbar-main">
        <div class="container-fluid">
          <!-- Logo container-->
          <div class="logo">
            <a href="#" class="logo">
              <i class="mdi mdi-bowling text-success mr-1">
              </i>
              <span class="hide-phone">大学生发展综合素质测评系统</span>
            </a>
          </div>
          <!-- End Logo container-->
          <div class="menu-extras topbar-custom">
            <ul class="list-unstyled float-right mb-0">
              <!-- language-->
              <li class="list-inline-item dropdown notification-list hide-phone"><a
                class="nav-link dropdown-toggle arrow-none waves-effect" data-toggle="dropdown"
                href="#" role="button" aria-haspopup="false" aria-expanded="false">Chinese <img
                src="../../static/picture/chinese_fiag.jpg" class="ml-2" height="16" alt=""></a>
                <div class="dropdown-menu dropdown-menu-right language-switch"><a class="dropdown-item"
                                                                                  href="#"><img
                  src="../../static/picture/italy_flag.jpg" alt=""
                  height="16"><span>Italian </span></a><a class="dropdown-item" href="#"><img
                  src="../../static/picture/french_flag.jpg" alt="" height="16"><span>French
                        </span></a><a class="dropdown-item" href="#"><img
                  src="../../static/picture/spain_flag.jpg" alt="" height="16"><span>Spanish
                        </span></a><a class="dropdown-item" href="#"><img
                  src="../../static/picture/russia_flag.jpg" alt="" height="16"><span>Russian
                        </span></a></div>
              </li><!-- notification-->
              <li class="list-inline-item dropdown notification-list"><a
                class="nav-link dropdown-toggle arrow-none waves-effect" data-toggle="dropdown"
                href="#" role="button" aria-haspopup="false" aria-expanded="false"><i
                class="dripicons-mail noti-icon"></i><span
                class="badge badge-danger noti-icon-badge">5</span></a>
                <div class="dropdown-menu dropdown-menu-right dropdown-arrow dropdown-menu-lg border-0">
                  <!-- item-->
                  <div class="dropdown-item noti-title">
                    <h5><span class="badge badge-danger float-right">745</span>Messages</h5>
                  </div><!-- item--><a href="javascript:void(0);" class="dropdown-item notify-item">
                  <div class="notify-icon"><img src="../../static/picture/avatar-2.jpg" alt="user-img"
                                                class="img-fluid rounded-circle"></div>
                  <p class="notify-details"><b>Charles M. Jones</b><small class="text-muted">Dummy
                    text of the printing and typesetting industry.</small></p>
                </a><!-- item--><a href="javascript:void(0);" class="dropdown-item notify-item">
                  <div class="notify-icon"><img src="../../static/picture/avatar-3.jpg" alt="user-img"
                                                class="img-fluid rounded-circle"></div>
                  <p class="notify-details"><b>Thomas J. Mimms</b><small class="text-muted">You
                    have 87 unread messages</small></p>
                </a><!-- item--><a href="javascript:void(0);" class="dropdown-item notify-item">
                  <div class="notify-icon"><img src="../../static/picture/avatar-4.jpg" alt="user-img"
                                                class="img-fluid rounded-circle"></div>
                  <p class="notify-details"><b>Luis M. Konrad</b><small class="text-muted">It is a
                    long established fact that a reader will</small></p>
                </a><!-- All--><a href="javascript:void(0);" class="dropdown-item notify-item border-top">View
                  All </a>
                </div>
              </li><!-- notification-->
              <li class="list-inline-item dropdown notification-list"><a
                class="nav-link dropdown-toggle arrow-none waves-effect" data-toggle="dropdown"
                href="#" role="button" aria-haspopup="false" aria-expanded="false"><i
                class="dripicons-bell noti-icon"></i><span
                class="badge badge-success noti-icon-badge">2</span></a>
                <div class="dropdown-menu dropdown-menu-right dropdown-arrow dropdown-menu-lg border-0">
                  <!-- item-->
                  <div class="dropdown-item noti-title">
                    <h5>Notification(3)</h5>
                  </div><!-- item--><a href="javascript:void(0);" class="dropdown-item notify-item">
                  <div class="notify-icon bg-success"><i class="mdi mdi-cart-outline"></i></div>
                  <p class="notify-details"><b>Your order is placed</b><small
                    class="text-muted">Dummy text of the printing and typesetting
                    industry.</small></p>
                </a><!-- item--><a href="javascript:void(0);" class="dropdown-item notify-item">
                  <div class="notify-icon bg-warning"><i class="mdi mdi-message"></i></div>
                  <p class="notify-details"><b>New Message received</b><small
                    class="text-muted">You have 87 unread messages</small></p>
                </a><!-- item--><a href="javascript:void(0);" class="dropdown-item notify-item">
                  <div class="notify-icon bg-info"><i class="mdi mdi-glass-cocktail"></i></div>
                  <p class="notify-details"><b>Your class is updated</b><small
                    class="text-muted">It is a long established fact that a reader
                    will</small></p>
                </a><!-- All--><a href="javascript:void(0);" class="dropdown-item notify-item border-top">View
                  All </a>
                </div>
              </li><!-- User-->
              <li class="dropdown notification-list">
                <a class="nav-link dropdown-toggle arrow-none waves-effect nav-user" data-toggle="dropdown"
                   href="#" role="button" aria-haspopup="false" aria-expanded="false">
                  <img src="../../static/picture/avatar-1.jpg" alt="user" class="rounded-circle">
                </a>
                <span>{{ name }}</span>
                <div class="dropdown-menu dropdown-menu-right profile-dropdown  border-0">
                  <!-- item-->
                  <div class="dropdown-item noti-title">
                    <h5>Welcome,{{ name }}</h5>
                  </div>
                  <a class="dropdown-item" href="#">
                    <i class="mdi mdi-account-circle m-r-5 text-muted">
                    </i>用户信息</a>
                  <a class="dropdown-item" href="#">
                    <i class="mdi mdi-lock-open-outline m-r-5 text-muted">
                    </i>切换用户</a>
                  <a class="dropdown-item" href="#">
                    <i class="mdi mdi-settings m-r-5 text-muted">
                    </i>设置
                  </a>
                  <div class="dropdown-divider">
                  </div>
                  <a class="dropdown-item" href="#">
                    <i class="mdi mdi-logout m-r-5 text-muted">
                    </i>退出登录
                  </a>
                </div>
              </li>
              <li class="menu-item">
                <!-- Mobile menu toggle-->
                <a class="navbar-toggle nav-link">
                  <div class="lines">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </a>
                <!-- End mobile menu toggle-->
              </li>
            </ul>
          </div>
          <!-- end menu-extras -->
          <div class="clearfix">
          </div>
        </div>
        <!-- end container -->
      </div>
      <!-- end topbar-main -->
      <!-- MENU Start -->
      <div class="navbar-custom">
        <div class="container-fluid">
          <div id="navigation">
            <!-- Navigation Menu-->
            <ul class="navigation-menu">
              <li class="has-submenu">
                <a href="http://localhost:8080/#/Student">
                  <i class="dripicons-device-desktop">
                  </i>主页
                </a>
              </li>

              <li class="has-submenu">
                <a href="#">
                  <i class="dripicons-jewel">

                  </i>提交材料
                </a>
                <ul class="submenu megamenu">
                  <li>
                    <ul>
                      <li>
                        <a href="#">上传审核材料</a>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <li class="has-submenu">
                <a href="#">
                  <i class="dripicons-blog">

                  </i>发展方向建议
                </a>
                <ul class="submenu">
                  <li class="has-submenu">
                    <a href="#">专业技术能力</a>
                    <ul class="submenu">
                      <li>
                        <a href="suggestion/1/">专业技术推荐</a>
                      </li>
                    </ul>
                  </li>
                  <li class="has-submenu">
                    <a href="#">创新创业能力</a>
                    <ul class="submenu">
                      <li>
                        <a href="suggestion/2/">创新创业推荐</a>
                      </li>
                    </ul>
                  </li>
                  <li class="has-submenu">
                    <a href="#">知识学习能力</a>
                    <ul class="submenu">
                      <li>
                        <a href="suggestion/3/">知识学习推荐</a>
                      </li>
                    </ul>
                  </li>
                  <li class="has-submenu">
                    <a href="#">管理实践能力</a>
                    <ul class="submenu">
                      <li>
                        <a href="suggestion/4/">管理实践推荐</a>
                      </li>
                    </ul>
                  </li>
                  <li class="has-submenu">
                    <a href="#">综合发展能力</a>
                    <ul class="submenu">
                      <li>
                        <a href="suggestion/5/">综合发展推荐</a>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <li class="has-submenu">
                <a href="#">
                  <i class="dripicons-blog">

                  </i>评分准则
                </a>
                <ul class="submenu megamenu">
                  <li>
                    <ul>
                      <li>
                        <router-link to="CMNorm">五大方面评分准则</router-link>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
            </ul>
            <!-- End navigation menu -->
          </div>
          <!-- end #navigation -->
        </div>
        <!-- end container -->
      </div>
      <!-- end navbar-custom -->
    </header>
    <!-- End Navigation Bar-->
    <div class="wrapper">
      <div class="container-fluid">
        <!-- Page-Title -->
        <div class="row">
          <div class="col-sm-12">
            <div class="page-title-box">
              <div class="float-right hide-phone">
                <ul class="list-inline">
                  <li class="list-inline-item mr-3">
                    <input class="knob" data-width="48" data-height="48" data-linecap="round"
                           data-fgcolor="#605daf" :value="rate" data-skin="tron" data-angleoffset="180"
                           data-readonly="true" data-thickness=".1">
                  </li>
                  <li class="list-inline-item">
                    <span class="text-muted">成绩达标率</span>
                    <h6>{{num_pass}}人/{{num_all}}人</h6>
                  </li>
                </ul>
              </div>
              <h4 class="page-title">主页</h4>
              <div class="btn-group mt-2">
                <ol class="breadcrumb hide-phone p-0 m-0">
                  <li class="breadcrumb-item">
                    <a href="#">系统</a>
                  </li>
                  <li class="breadcrumb-item active">主页</li>
                </ol>
              </div>
            </div>
          </div>
        </div>
        <!-- end page title end breadcrumb -->
        <div class="row">
          <div class="col-lg-9">
            <div class="row">
              <div class="col-lg-3">
                <div class="card">
                  <div class="card-body">
                    <div class="icon-contain">
                      <div class="row">
                        <div class="col-2 align-self-center">
                          <i class="fas fa-tasks text-gradient-success">

                          </i>
                        </div>
                        <div class="col-10 text-right">
                          <h5 class="mt-0 mb-1">{{zy}}人</h5>
                          <p class="mb-0 font-12 text-muted">专业技术能力</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-3">
                <div class="card">
                  <div class="card-body justify-content-center">
                    <div class="icon-contain">
                      <div class="row">
                        <div class="col-2 align-self-center">
                          <i class="far fa-gem text-gradient-danger">

                          </i>
                        </div>
                        <div class="col-10 text-right">
                          <h5 class="mt-0 mb-1">{{cx}}人</h5>
                          <p class="mb-0 font-12 text-muted">创新创业能力</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-3">
                <div class="card">
                  <div class="card-body">
                    <div class="icon-contain">
                      <div class="row">
                        <div class="col-2 align-self-center">
                          <i class="fas fa-users text-gradient-warning">

                          </i>
                        </div>
                        <div class="col-10 text-right">
                          <h5 class="mt-0 mb-1">{{zs}}人</h5>
                          <p class="mb-0 font-12 text-muted">知识学习能力</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-3">
                <div class="card ">
                  <div class="card-body">
                    <div class="icon-contain">
                      <div class="row">
                        <div class="col-2 align-self-center">
                          <i class="fas fa-database text-gradient-primary">

                          </i>
                        </div>
                        <div class="col-10 text-right">
                          <h5 class="mt-0 mb-1">{{gl}}人</h5>
                          <p class="mb-0 font-12 text-muted">管理实践能力</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="card">
              <div class="card-body">
                <div class="btn-group btn-group-toggle float-right" data-toggle="buttons">
                  <label class="btn btn-primary btn-sm active">
                    <input type="radio" name="options" id="option1" checked="">用户（左）
                  </label>
                  <label class="btn btn-primary btn-sm">
                    <input type="radio" name="options" id="option2">平均（右）
                  </label>
                </div>
                <h5 class="header-title mb-4 mt-0">成绩雷达图对比
                </h5>
                <div>
                  <img height="100%" width="100%" src="../../static/image/1.png" alt=""/>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-3">
            <div class="card">
              <div class="card-body">
                <div class="dropdown d-inline-block float-right">
                  <a class="nav-link dropdown-toggle arrow-none" id="dLabel4" data-toggle="dropdown" href="#"
                     role="button" aria-haspopup="false" aria-expanded="false">

                  </a>
                </div>
                <!--                        <h5 class="header-title mb-4 mt-0">综合发展能力</h5>-->
                <div>
                  <h6 class="header-title mb-4 mt-0">直达链接</h6><br>
                  <a href="https://www.hunnu.edu.cn/">湖南师范大学官网</a><br><br>
                  <a href="https://jwc.hunnu.edu.cn/">湖南师范大学教务处</a><br>
                  <a href="http://jwglnew.hunnu.edu.cn">湖南师范大学教务系统</a><br><br>
                  <a href="https://stustar.hunnu.edu.cn/">湖南师范大学学生工作处</a><br><br>
                  <a href="https://www.neea.edu.cn/">中国教育考试网</a><br><br>
                  <a href="https://cy.ncss.cn/">全国大学生创业服务网</a><br><br>
                  <a href="https://www.guoxinlanqiao.com/">蓝桥杯大赛官网</a><br><br>
                  <a href="https://gplt.patest.cn/regulation">天梯赛大赛官网</a><br><br>
                  <a href="https://www.csdn.net/">CSDN-专业开发者社区</a><br><br>
                </div>
                <br><br>
                <div>
                  <h6 class="header-title mb-4 mt-0"><font color="black">学业预警情况</font></h6>
                  <span v-if="this.ans === 0"><font color="green">满足毕业最低要求<strong></strong></font></span><br><br>
                  <span v-if="this.ans === 1"><font color="red">不满足毕业最低要求<strong></strong></font></span><br><br>
                  <a href="#"><u>详细展开</u></a><br><br>
                </div>
                <!--                        <ul class="list-unstyled list-inline text-center mb-0 mt-3">-->
                <!--                            <li class="mb-2 list-inline-item text-muted font-13">-->
                <!--                                <i class="mdi mdi-label text-success mr-2">-->

                <!--                                </i>优秀-->
                <!--                            </li>-->
                <!--                            <li class="mb-2 list-inline-item text-muted font-13">-->
                <!--                                <i class="mdi mdi-label text-danger mr-2">-->

                <!--                                </i>不合格-->
                <!--                            </li>-->
                <!--                            <li class="mb-2 list-inline-item text-muted font-13">-->
                <!--                                <i class="mdi mdi-label text-warning mr-2">-->

                <!--                                </i>良好-->
                <!--                            </li>-->
                <!--                        </ul>-->
              </div>
            </div>

          </div>
        </div>
        <div class="row">
          <div class="col-xl-12">
            <div class="card">
              <div class="card-body">
                <h5 class="header-title pb-3 mt-0">学生学习成果</h5>
                <div class="table-responsive">
                  <table class="table table-hover mb-0">
                    <thead>
                    <tr class="align-self-center">
                      <th>学生姓名</th>
                      <th>发展方向</th>
                      <th>最高成绩</th>
                      <th>评价</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                      <td>
                        <img src="../../static/picture/avatar-1.jpg" alt=""
                             class="thumb-sm rounded-circle mr-2">***
                      </td>
                      <td>专业技术能力</td>
                      <td>{{this.m1}}</td>
                      <td>
                        <span class="badge badge-boxed  badge-soft-primary">优秀</span>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <img src="../../static/picture/avatar-2.jpg" alt=""
                             class="thumb-sm rounded-circle mr-2">***
                      </td>
                      <td>创新创业能力</td>
                      <td>{{this.m2}}</td>

                      <td>
                        <span class="badge badge-boxed  badge-soft-primary">优秀</span>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <img src="../../static/picture/avatar-3.jpg" alt=""
                             class="thumb-sm rounded-circle mr-2">***
                      </td>
                      <td>知识学习能力</td>
                      <td>{{this.m3}}</td>

                      <td>
                        <span class="badge badge-boxed  badge-soft-primary">优秀</span>
                      </td>
                    </tr>
                    <tr>

                      <td>
                        <img src="../../static/picture/avatar-4.jpg" alt=""
                             class="thumb-sm rounded-circle mr-2">***
                      </td>
                      <td>管理实践能力</td>
                      <td>{{this.m4}}</td>

                      <td>
                        <span class="badge badge-boxed  badge-soft-primary">优秀</span>
                      </td>
                    </tr>
                    <tr>

                      <td>
                        <img src="../../static/picture/avatar-5.jpg" alt=""
                             class="thumb-sm rounded-circle mr-2">***
                      </td>
                      <td>综合发展能力</td>
                      <td>{{this.m5}}</td>

                      <td>
                        <span class="badge badge-boxed  badge-soft-primary">优秀</span>
                      </td>
                    </tr>

                    </tbody>
                  </table>
                </div>
                <!--end table-responsive-->
              </div>
            </div>
          </div>
        </div>
        <!-- end row -->
      </div>
      <!-- end container -->
    </div>
    <!-- end wrapper -->
    <!-- Footer -->
    <footer class="footer">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">© 2022 大学生发展综合素质测评系统</div>
        </div>
      </div>
    </footer>
    <!-- End Footer -->
  </div>
</template>
<script>
export default {
  name: 'Student',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      'num_all': 0, // 总人数
      'num_pass': 0, // 总达标人数
      'rate': 0, // 达标率
      'zy': 0, // 专业技术能力达标人数
      'cx': 0, // 创新创业能力达标人数
      'zs': 0, // 知识学习能力达标人数
      'gl': 0, // 管理实践能力达标人数
      'zh': 0,  // 综合发展能力达标人数
      "m1": 0, // 专业技术能力最高分
      "m2": 0, // 创新创业能力最高分
      "m3": 0, // 知识学习能力最高分
      "m4": 0, // 管理实践能力最高分
      "m5": 0, // 综合发展能力最高分
      "ans": 1 // 学业预警情况：'满足/不满足毕业最低要求'
    }
  },
  methods: {

  },
  created() {
    this.$axios({
      method: 'post',
      url: '/login/index'
    }).then((res)=>{
      if (res.data.code === 200) {
        this.m1 = res.data.data.m1
        this.m2 = res.data.data.m2
        this.m3 = res.data.data.m3
        this.m4 = res.data.data.m4
        this.m5 = res.data.data.m5
        this.ans = res.data.data.ans
      } else {
        console.log(res.data.msg)
      }
    }).catch((err)=>{
      console.log(err)
    })
    this.$axios({
      method: 'post',
      url: '/api/get_score_std'
    }).then((res)=>{
      this.num_all = res.data.data.num_all
      this.num_pass = res.data.data.num_pass
      this.rate = res.data.data.rate
      this.zy = res.data.data.zy
      this.cx = res.data.data.cx
      this.zs = res.data.data.zs
      this.gl = res.data.data.gl
      this.zh = res.data.data.zh
    }).catch((err)=>{
      console.log(err)
    })
  }
}
</script>
<!-- jQuery -->
