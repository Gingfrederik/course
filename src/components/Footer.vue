<template>
  <footer class="footer">
    <div class="container">
      <div class="row d-flex justify-content-center">
        <div class="col-xs-6 col-sm-6 col-md-6">
          <span class="text-muted">Copyright &copy;{{year}} Gingfrederik All Rights Reserved</span>
          <a target="_blank" href="https://www.facebook.com/cycucourse/"><i class="fa fa-facebook-square fa-2x" aria-hidden="true"></i></a> 
          <a target="_blank" href="https://github.com/Gingfrederik/course"><i class="fa fa-github-square fa-2x" aria-hidden="true"></i></a> 
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  created(){
    var now = new Date();
    this.year = now.getFullYear();
  },
  data: function(){
    return{
      year: ""
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #636c72;
}
a:focus, a:hover {
  color: #bccad0;
}
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  /* Set the fixed height of the footer here */
  height: 60px;
  line-height: 60px; /* Vertically center the text there */
  background-color: #292b2c;
}

.footer > .container {
  padding-right: 15px;
  padding-left: 15px;
}

</style>
