import Vue from 'vue'
import Router from 'vue-router'

import Login from '../components/Login'
import Home from '../components/Home'
import Search from '../components/Search'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/search',
      component: Search
    }
  ]
})
