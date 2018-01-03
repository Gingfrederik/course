import Vue from 'vue'
import Router from 'vue-router'

import Login from '../components/Login'
import Logout from '../components/Logout'
import Home from '../components/Home'
import Stage from '../components/Stage'

import Trace from '../components/Trace'
import Fill from '../components/Fill'
import Tmp from '../components/Tmp'
import Register from '../components/Register'
import Got from '../components/Got'
import Search from '../components/Search'
import Close from '../components/Close'
import Timetable from '../components/Timetable'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/tmp',
      component: Tmp 
    },
    {
      path: '/logout',
      component: Logout
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/stage',
      component: Stage 
    },
    {
      path: '/search',
      component: Search
    },
    {
      path: '/fill',
      component: Fill 
    },
    {
      path: '/register',
      component: Register 
    },
    {
      path: '/got',
      component: Got 
    },
    {
      path: '/trace',
      component: Trace 
    },
    {
      path: '/close',
      component: Close 
    },
    {
      path: '/table',
      component: Timetable 
    }

  ]
})
