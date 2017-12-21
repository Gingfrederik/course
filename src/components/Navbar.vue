<template>
  <header class="navbar navbar-inverse fixed-top bg-inverse navbar-toggleable-md bd-navbar">
    <nav class="container">
      <div class="d-flex justify-content-between">
        <a class="navbar-brand" herf="/">選課系統</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#bd-main-nav" aria-controls="bd-main-nav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
      <div v-if="this.$store.loginstatus" class="collapse navbar-collapse" id="bd-main-nav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link @click.native="navbar" class="nav-link" to="/search">課程查詢</router-link>
          </li>
          <li class="nav-item active">
            <router-link @click.native="navbar" class="nav-link" to="/trace">追蹤清單</router-link>
          </li>
          <li class="nav-item active">
            <router-link @click.native="navbar" class="nav-link" to="/register">登記清單</router-link>
          </li>
          <li class="nav-item active">
            <router-link @click.native="navbar" class="nav-link" to="/got">修課清單</router-link>
          </li>
          <li class="nav-item active">
            <router-link @click.native="navbar" class="nav-link" to="/table">課程表</router-link>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a @click.native="navbar" class="nav-link active" target="_blank" href="https://www.facebook.com/cycucourse/"><i class="fa fa-facebook-square fa-1x" aria-hidden="true"></i> 粉絲專頁</a></li>
          <li><router-link @click.native="navbar" class="nav-link active" to="/logout"><i class="fa fa-sign-out" aria-hidden="true"></i> 登出</router-link></li>
        </ul>
      </div>
      <div v-else class="collapse navbar-collapse" id="bd-main-nav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link @click.native="navbar" class="nav-link" to="/">首頁</router-link>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a @click.native="navbar" class="nav-link active" target="_blank" href="https://www.facebook.com/cycucourse/"><i class="fa fa-facebook-square fa-1x" aria-hidden="true"></i> 粉絲專頁</a></li>
          <li><router-link @click.native="navbar" class="nav-link active" to="/login"><i class="fa fa-user" aria-hidden="true"></i> 登入</router-link></li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'Navbar',
	methods: {
		navbar: function(){
			jQuery('#bd-main-nav').collapse('toggle');
		},
	},
  data: function(){
    return{
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar{
  text-align:left;
}
.nav-link {
  border-bottom: 1px solid #292b2c;
}
.nav-link:hover {
  border-bottom: 1px solid #ffffff;
}
a:not([href]):not([tabindex]) {
  color: #fff;
}
</style>
