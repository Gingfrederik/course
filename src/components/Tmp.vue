<template>
  <main> 
  <div class="container">
    <div class="Aligner">
      <div class="Aligner-item">
        <div class="container">
        </div>
      </div>
    </div>
  </div>
  </main>
</template>

<script>
export default {
  name: 'Tmp',
  created() {
    this.$router.go(-1)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.Aligner {
  display: flex;
  align-items: center;
  min-height: 24em;
  justify-content: center;
}

.Aligner-item {
  flex: 2;
}

.Aligner-item--top {
  align-self: flex-start;
}

.Aligner-item--bottom {
  align-self: flex-end;
}

.Aligner-item--fixed {
  flex: none;
  max-width: 50%;
}
</style>
