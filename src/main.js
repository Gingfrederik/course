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
      stagecode:'',
      student:null,
      idcode:'',
      loginstatus: false,
      cookie:'',
      pageid: '',
      courses:null,
      ip:'idontknow.com.tw:8443',
    }
  },
  render: h => h(App),
  router: router
})
