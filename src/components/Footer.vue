<template>
  <footer class="footer">
    <div class="container">
      <span class="text-muted">Copyright &copy; Gingfrederik</span>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
