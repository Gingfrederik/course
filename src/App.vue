<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
    <myfooter></myfooter>
  </div>
</template>

<script>
import navbar from './components/Navbar'
import myfooter from './components/Footer'
import axios from 'axios'
import qs from 'qs'

export default {
  name: 'app',
  components: {
    navbar,
    myfooter
  },
  created() {
    this.pulse();
    axios.get(this.$store.ip+'/stage')
    .then(response => {
      this.stage = response.data;
      for(var i=0;i<this.stage.datas.length;i++)
      {
        this.stage.datas[i].bgtime = new Date(this.stage.datas[i].bgtime);
        this.stage.datas[i].edtime = new Date(this.stage.datas[i].edtime);
        var now = new Date();
        if(this.stage.datas[i].bgtime<=now && this.stage.datas[i].edtime>now)
        {
          this.$store.stagecode = this.stage.datas[i].action_bits;
	    console.log(this.$store.stagecode)
        }
      }
    })
  },
  methods:{
    pulse:function(){
      console.log('pulse');
      if(this.$store.loginstatus==true)
      {
        axios.post(this.$store.ip+'/timelist',
        qs.stringify({'idcode':this.$store.idcode}),
        {headers:{'Page-Id':this.$store.pageid},
        withCredentials: true})
        .then(response=>{
          this.times= response.data
          setTimeout(this.pulse,300000);
        })
      }
      else
      {
        setTimeout(this.pulse,100000);
      }
    },
  },
  data: function(){
    return {
      dat: this.$store,
      stage:this.stage,
    }
  }
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/notosanstc.css);

@media (max-width: 575px) { 
  html {
    font-size: 65%;
  }
 }

@media (min-width: 576px) and (max-width: 768px) { 
  html {
    font-size: 80%;
  }
 }

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
main {
    margin-top: 55px;
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
