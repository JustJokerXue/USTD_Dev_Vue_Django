import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld.vue'
import Student from '../components/Student.vue'
import CMNorm from '../components/CMNorm.vue'
import Login from '../components/Login.vue'
import AcademicWarning from '../components/AcademicWarning.vue'
import Error from '../components/Error.vue'
import Error2 from '../components/Error2.vue'
import Infor from '../components/Infor.vue'
import PwdChange from '../components/PwdChange.vue'
import Suggestion from '../components/Suggestion.vue'
import Verify from '../components/Verify.vue'
import VueRouter from "vue-router";

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/AcademicWarning',
      name: 'AcademicWarning',
      component: AcademicWarning
    },
    {
      path: '/CMNorm',
      name: 'CMNorm',
      component: CMNorm
    },
    {
      path: '/Error',
      name: 'Error',
      component: Error
    },
    {
      path: '/Error2',
      name: 'Error2',
      component: Error2
    },
    {
      path: '/Infor',
      name: 'Infor',
      component: Infor
    },
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/PwdChange',
      name: 'PwdChange',
      component: PwdChange
    },
    {
      path: '/Student',
      name: 'Student',
      component: Student
    },
    {
      path: '/Suggestion',
      name: 'Suggestion',
      component: Suggestion
    },
    {
      path: '/Verify',
      name: 'Verify',
      component: Verify
    }
  ]
})
