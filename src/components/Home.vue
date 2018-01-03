<template>
  <main> 
  <div class="container">
    <br><br>
    <div class="alert alert-info" role="alert">
      目前階段:
      <strong v-if="stage!=null">
        {{stagetype[stage.datas[0].sn_stage_type]}}
        <br>
        {{stage.datas[0].bgtime}}&nbsp;~&nbsp;{{stage.datas[0].edtime}}
        </br>
        <span style="white-space: pre-line">{{stage.datas[0].remark}}</span>
      </strong>
    </div>
    <div v-if="stage!=null">
      <div v-if="stage.datas[1]!=null" class="alert alert-warning" role="alert">
        下個階段:
        <strong>
          {{stagetype[stage.datas[1].sn_stage_type]}}
          <br>
          {{stage.datas[1].bgtime}}&nbsp;~&nbsp;{{stage.datas[1].edtime}}
          </br>
          <span style="white-space: pre-line">{{stage.datas[1].remark}}</span>
        </strong>
      </div>
    </div>

    <div class="Aligner">
      <div class="Aligner-item">
        <div class="container">
          <h1>選課系統</h1> 
        </div>
        <div class="container">
          <router-link to="/login" tag="button" type="button" class="btn btn-success btn-lg">
            <i class="fa fa-user" aria-hidden="true"></i> 登入
          </router-link>
        </div>
        <br><br>
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
    axios.get(this.$store.ip+'/stage')
    .then(response => {
      // JSON responses are automatically parsed.
      this.stage = response.data
  })},
  data: function(){
    return {
      stagetype:{
        "11":"第一次篩選登記",
        "12":"第二次篩選登記",
        "21":"第一次加退選",
        "22":"第二次加退選",
        "23":"第三次加退選"
      },
      stage:null
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
