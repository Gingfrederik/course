// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueStash from 'vue-stash'

Vue.use(VueStash)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  data: {
    store: {
      yearTerm:"1062",
      crush:true,
      coutime:null,
      gotcou:null,
      stagecode:null,
      student:null,
      idcode:null,
      loginstatus: false,
      cookie:null,
      pageid: null,
      courses:null,
      ip:'https://course.geederik.tw:8443',
      //ip:'http://127.0.0.1:5000',
    }
  },
  render: h => h(App),
  router: router
})
