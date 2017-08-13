<template>
  <main> 
  <div class="container">
    <br><br>
    <div class="alert alert-info" role="alert">
      目前階段
<strong>
      <br>{{stage.datas[0].bgtime}}&nbsp;~&nbsp;{{stage.datas[0].edtime}}</br>
<span style="white-space: pre-line">{{stage.datas[0].remark}}</span></strong>
    </div>

    <div class="Aligner">
      <div class="Aligner-item">
        <div class="container">
          <h1>選課系統</h1> 
        </div>
      </div>
    </div>
  </div>
  </main>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  created() {
    axios.get('https://'+this.$store.ip+'/stage')
    .then(response => {
      // JSON responses are automatically parsed.
      this.stage = response.data
  })},
  data: function(){
    return {
      stage:this.stage
    }
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
