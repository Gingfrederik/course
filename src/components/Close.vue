<template>
  <main> 
  <div class="container">
    <div class="Aligner">
      <div class="Aligner-item">
        <div class="container">
          <h1>系統關閉中</h1> 
        </div>
      </div>
    </div>
  </div>
  </main>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Close',
  created() {
    axios.get('http://127.0.0.1:5000/stage')
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
