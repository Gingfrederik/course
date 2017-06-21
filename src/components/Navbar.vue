<template>
  <header class="navbar navbar-inverse bg-inverse navbar-toggleable-md bd-navbar">
    <nav class="container">
      <div class="d-flex justify-content-between">
        <a class="navbar-brand" herf="/">新選課系統</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#bd-main-nav" aria-controls="bd-main-nav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse" id="bd-main-nav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a v-on:click="navbar" class="nav-link" href="#">首頁</a>
          </li>
          <li class="nav-item active">
            <a v-on:click="navbar" class="nav-link" href="#/search">課程查詢</a>
          </li>
          <li class="nav-item active">
            <a v-on:click="navbar" class="nav-link" href="#">追蹤清單</a>
          </li>
          <li class="nav-item active">
            <a v-on:click="navbar" class="nav-link" href="#">登記清單</a>
          </li>
          <li class="nav-item active">
            <a v-on:click="navbar" class="nav-link" href="#">修課清單</a>
          </li>
          <li class="nav-item active">
            <a v-on:click="navbar" class="nav-link" href="#">課程表</a>
          </li>
          <li class="nav-item active">
            <a v-on:click="navbar" class="nav-link" href="#">選課紀錄</a>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a v-on:click="navbar" class="nav-link active" href="#/login"><i class="fa fa-user" aria-hidden="true"></i> 登入</a></li>
          <li><a v-on:click="navbar" class="nav-link active" href="#"><i class="fa fa-sign-out" aria-hidden="true"></i> 登出</a></li>
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
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar{
  text-align:left;
}
.nav-link:hover {
  border-bottom: 1px solid #ffffff;
}
a:not([href]):not([tabindex]) {
  color: #fff;
}
</style>
