<template>
  <div>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">
    <meta content="Admin Dashboard" name="description">
    <meta content="Mannatthemes" name="author">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- X-editable css -->
    <link type="text/css" href="../../static/css/bootstrap-editable.css" rel="stylesheet">
    <link href="../../static/css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <link href="../../static/css/icons.css" rel="stylesheet" type="text/css">
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css">
    <!-- Navigation Bar-->
    <header id="topnav">
      <div class="topbar-main">
        <div class="container-fluid">
          <!-- Logo container-->
          <div class="logo">
            <a href="" class="logo">
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
                <span></span>
                <div class="dropdown-menu dropdown-menu-right profile-dropdown  border-0">
                  <!-- item-->
                  <div class="dropdown-item noti-title">
                    <h5>Welcome,</h5>
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
                  <a class="dropdown-item" href="http://127.0.0.1:8000/">
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
                <a href="http://127.0.0.1:8000/login/index.html">
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
            <li class="has-submenu">
              <a href="#">
                <i class="dripicons-blog">
                </i>评分准则
              </a>
              <ul class="submenu megamenu">
                <li>
                  <ul>
                    <li>
                      <a href="#">五大方面评分准则</a>
                    </li>
                  </ul>
                </li>
              </ul>
            </li>
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
                  <li class="list-inline-item mr-3"><input class="knob" data-width="48"
                                                           data-height="48" data-linecap="round"
                                                           data-fgcolor="#605daf" value=""
                                                           data-skin="tron" data-angleoffset="180"
                                                           data-readonly="true"
                                                           data-thickness=".1"></li>
                  <li class="list-inline-item"><span class="text-muted">达标率</span>
                    <h6>人/人</h6>
                  </li>
                </ul>
              </div>
              <h4 class="page-title">学业预警功能</h4>
              <div class="btn-group mt-2">
                <ol class="breadcrumb hide-phone p-0 m-0">
                  <li class="breadcrumb-item"><a href="#">学业预警功能是来提醒学生要满足学校的毕业要求</a></li>
                </ol>
              </div>
            </div>
          </div>
        </div><!-- end page title end breadcrumb -->
        <div class="row">
          <div class="col-12">
            <div class="card">
              <div class="card-body">
                <h4 class="mt-0 header-title">学业预警</h4>
                <p class="text-muted mb-4 font-13">以下要求只要其中一项没有达到就会预警</p>
                <table class="table table-striped">
                  <thead>
                  <tr>
                    <th style="width: 50%;">项目</th>
                    <th>成绩/及格分数</th>
                    <th>是否合格</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr>
                    <td>最低学分要求</td>
                    <td><a href="#" id="inline-xuefen" data-pk="1">
                      {% if minimum >= 24 %}
                      <font color="green"></font>/24</a>
                      {% endif %}
                      {% if minimum < 24 %}
                      <font color="red"></font>/24
                      {% endif %}
                    </td>
                    {% if minimum >= 24 %}
                    <td><font color="green">是</font></td>
                    {% endif %}
                    {% if minimum < 24 %}
                    <td><font color="red">否</font></td>
                    {% endif %}
                  </tr>
                  <tr>
                    <td>必修课成绩</td>
                    <td><a href="#" id="inline-bixiu" data-pk="1">
                      {% if compulsory >= 20 %}
                      <font color="green"></font>/20</a>
                      {% endif %}
                      {% if compulsory < 20 %}
                      <font color="red"></font>/20
                      {% endif %}
                    </td>
                    {% if compulsory >= 20 %}
                    <td><font color="green">是</font></td>
                    {% endif %}
                    {% if compulsory < 20 %}
                    <td><font color="red">否</font></td>
                    {% endif %}
                  </tr>
                  <tr>
                    <td>选修课成绩</td>
                    <td><a href="#" id="inline-xuanxiu" data-pk="1" data-value="">
                      {% if elective >= 4 %}
                      <font color="green"></font>/4</a>
                      {% endif %}
                      {% if elective < 4 %}
                      <font color="red"></font>/4
                      {% endif %}
                    </td>
                    {% if elective >= 4 %}
                    <td><font color="green">是</font></td>
                    {% endif %}
                    {% if elective < 4 %}
                    <td><font color="red">否</font></td>
                    {% endif %}
                  </tr>
                  <tr>
                    <td>体测成绩</td>
                    <td><a href="#" id="inline-tiyu" data-type="select" data-pk="1"
                           data-value="0" data-source="/status"
                           data-title="Select status">
                      {% if physical >= 60 %}
                      <font color="green"></font>/60</a>
                      {% endif %}
                      {% if physical < 60 %}
                      <font color="red"></font>/60
                      {% endif %}
                    </td>
                    {% if physical >= 60 %}
                    <td><font color="green">是</font></td>
                    {% endif %}
                    {% if physical < 60 %}
                    <td><font color="red">否</font></td>
                    {% endif %}
                  </tr>
                  <tr>
                    <td>四级成绩</td>
                    <td><a href="#" id="inline-siji" data-type="combodate"
                           data-pk="1" data-title="">
                      {% if cet4 >= 425 %}
                      <font color="green"></font>/425</a>
                      {% endif %}
                      {% if cet4 < 425 %}
                      <font color="red"></font>/425
                      {% endif %}
                    </td>
                    {% if cet4 >= 425 %}
                    <td><font color="green">是</font></td>
                    {% endif %}
                    {% if cet4 < 425 %}
                    <td><font color="red">否</font></td>
                    {% endif %}
                  </tr>
                  <tr>
                    <td>普通话成绩</td>
                    <td><a href="#" id="inline-putonghua" data-type="textarea" data-pk="1"
                           data-title="Enter comments">
                      {% if mandarin >= 80 %}
                      <font color="green"></font>/80</a>
                      {% endif %}
                      {% if mandarin < 80 %}
                      <font color="red"></font>/80
                      {% endif %}
                    </td>
                    {% if mandarin >= 80 %}
                    <td><font color="green">是</font></td>
                    {% endif %}
                    {% if mandarin < 80 %}
                    <td><font color="red">否</font></td>
                    {% endif %}
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div><!-- end col -->
        </div><!-- end row -->
      </div><!-- end container -->
    </div><!-- end wrapper -->
    <!-- Footer -->
    <footer class="footer">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">© 2022 大学生发展综合素质测评系统</div>
        </div>
      </div>
    </footer><!-- End Footer -->
  </div>
</template>

<script>
export default {
  name: 'AcademicWarning'
}
</script>

<style scoped>

</style>
