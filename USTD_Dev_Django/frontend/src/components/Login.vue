<template>
  <div>
    <meta charset="utf-8">
    <meta name="renderer" content="webkit">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=1280,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no">
    <link href="../../static/css/vendor.style.css" rel="stylesheet">
    <link href="../../static/css/login.style.css" rel="stylesheet">
    <div id="mount">
      <div data-reactroot="">
        <div class="_1RxfFVyy86UE1t7lqCDcGD">
          <div class="_3CkMCIo8-RsWtcLQqsuKBh">
            <div class="_3lr3h2hawOi8pO8fYLQcjI">用户登录</div>
            <form action="login/" method="post">
              <div class="_6vZdUKmPDGrrza0LnuXD9">
                <div>
                  <div class="mobileIcon"></div>
                  <input type="text" v-model="stu_id" name="id" autocomplete="off">
                  <p class="_2nSTvdgBwioyepYsyeaVPN"></p>
                </div>
              </div>
              <div class="_6vZdUKmPDGrrza0LnuXD9">
                <div>
                  <div class="passwordIcon"></div>
                  <input type="password" v-model="pwd" name="pwd" autocomplete="off">
                  <p class="_2nSTvdgBwioyepYsyeaVPN"></p>
                </div>
              </div>
              <div class="_6vZdUKmPDGrrza0LnuXD9">
                <input @click="login" type="button" value="登录" class="_2ZggRBvDTyawWaQQ6ambu4">
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data() {
    return {
      stu_id: '',
      pwd: '',
    }
  },
  methods: {
    login() {
      this.$axios({
        method: 'post',
        url: '/login',
        data: {
          stu_id: this.stu_id,
          pwd: this.pwd
        }
      }).then((res)=>{
        const res_data = res.data;
        if (res_data.code === 200 && res_data.status === 1) {
          this.$router.push({
            path: '/Student',
            params: {

            }
          })
        } else {
          alert(res_data.msg)
        }
      }).catch((err)=>{
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>

</style>
