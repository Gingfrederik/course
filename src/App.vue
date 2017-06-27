<template>
  <div id="app">
    <Navbar></Navbar>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Footer from './components/Footer'

export default {
  name: 'app',
  components: {
    Navbar,
    Footer
  },
  data: function(){
    return {
      user_course:['EE336G','EE255G','EE360G','EE380E','GR189A',
      'EE144A','GE286B','GE439B','EE367G','EE415G']
    }
  }
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/notosanstc.css);

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  min-height: 100vh;
  position: relative;
  margin: 0;
}

* {
  font-family: 'Noto Sans TC', sans-serif;
}
</style>
