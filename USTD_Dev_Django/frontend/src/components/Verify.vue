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
    <header id="topnav">
      <div class="topbar-main">
        <div class="container-fluid">
          <!-- Logo container-->
          <div class="logo">
            <a href="#" class="logo">
              <i class="mdi mdi-bowling text-success mr-1"></i>
              <span class="hide-phone">大学生发展综合素质测评系统</span>
            </a>
          </div>
          <!-- End Logo container-->
          <div class="menu-extras topbar-custom">
            <ul class="list-inline float-right mb-0">
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
                </a><!-- All--><a href="javascript:void(0);"
                                  class="dropdown-item notify-item border-top">View All </a>
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
                  <a class="dropdown-item" href="http://127.0.0.1:8000/">
                    <i class="mdi mdi-logout m-r-5 text-muted">
                    </i>退出登录
                  </a>
                </div>
              </li>
              <li class="menu-item list-inline-item">
                <!-- Mobile menu toggle--><a class="navbar-toggle nav-link">
                <div class="lines"><span></span><span></span><span></span></div>
              </a><!-- End mobile menu toggle-->
              </li>
            </ul>
          </div><!-- end menu-extras -->
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
                  <i class="dripicons-jewel">
                  </i>主页
                </a>
              </li>

              <li class="has-submenu">
                <a href="#">
                  <i class="dripicons-device-desktop">

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
                  <li class="list-inline-item mr-3">
                    <input class="knob" data-width="48" data-height="48" data-linecap="round"
                           data-fgcolor="#605daf" value="" data-skin="tron" data-angleoffset="180"
                           data-readonly="true" data-thickness=".1">
                  </li>
                  <li class="list-inline-item">
                    <span class="text-muted">成绩达标率</span>
                    <h6>人/人</h6>
                  </li>
                </ul>
              </div>
              <h4 class="page-title">材料</h4>

            </div>
          </div>
        </div>
        <!-- end page title end breadcrumb -->
        <div class="row">
          <div class="col-12">
            <div class="card">
              <div class="card-body">
                <h4 class="mt-0 header-title">材料提交</h4>
                <br>
                <table class="table mb-0">
                  <thead>
                  <tr>
                    <th>学号</th>
                    <th>证明材料描述</th>
                    <th>所属类别</th>
                    <th>证明材料图片</th>
                    <th>审核状态</th>
                    <th>操作</th>
                  </tr>
                  </thead>
                  <tbody>
                  {% for item in shenhe_list %}
                  <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td><img height="100px" width="100px" src=""></td>
                    {% if item.zhuangtai == "T" %}
                    <td><font color="green">通过</font></td>
                    {% endif %}
                    {% if item.zhuangtai == "F" %}
                    <td><font color="red">未通过</font></td>
                    {% endif %}
                    {% if item.zhuangtai == "D" %}
                    <td><font color="#CEBE29">待审核</font></td>
                    {% endif %}
                    <td>
                      <a href="/#?id=">删除</a>
                    </td>
                  </tr>
                  {% endfor %}
                  </tbody>
                </table>
                <form enctype="multipart/form-data" action="#" method="post">
                  {% csrf_token %}
                  <p>学号：<input type="text" name="id" value="" disabled="disabled"></p>
                  <p>描述：<input type="text" name="miaoshu"></p>
                  <p>
                    类别：
                    <select name="leibie">
                      <option>创新创业</option>
                      <option>专业技术</option>
                      <option>管理实践</option>
                      <option>综合发展</option>
                    </select>
                  </p>
                  <p>图片：<input type="file" name="image"></p>
                  <input type="submit" value="upload">
                </form>
              </div>
            </div>
          </div>
          <!-- end col -->
        </div>
        <!-- end row -->

        <!-- end row -->
      </div>
      <!-- end container -->
    </div><!-- end wrapper --><!-- Footer -->
    <footer class="footer">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">© 2022 大学生发展综合素质测评系统
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Verify'
}
</script>

<style scoped>

</style>
