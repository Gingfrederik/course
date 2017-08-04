<template>
  <main> 
  <br></br>
  <div class="container">
    <table class="table table-responsive table-bordered center-all">
      <thead class="thead-inverse">
        <tr>
          <th colspan="2">時間&nbsp;/&nbsp;星期</th>
          <th>星期一</th>
          <th>星期二</th>
          <th>星期三</th>
          <th>星期四</th>
          <th>星期五</th>
          <th>星期六</th>
          <th>星期日</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="time in ordtime" v-bind:class="[times[time].flag === 'B'?'table-active':'']">
          <th class="table-info" scope="row">{{ times[time].time }}</th>
          <th class="table-info">{{ times[time].flag }}</th>
          <td>{{ times[time].datas.mon }}</td>
          <td>{{ times[time].datas.tue }}</td>
          <td>{{ times[time].datas.wed }}</td>
          <td>{{ times[time].datas.thu }}</td>
          <td>{{ times[time].datas.fri }}</td>
          <td>{{ times[time].datas.sat }}</td>
          <td>{{ times[time].datas.sun }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <br></br>
  <br></br>
  </main>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
axios.defaults.withCredentials = true;

export default {
  name: 'Home',
  created() {
    axios.post('http://127.0.0.1:5000/timelist',
    qs.stringify({'idcode':this.$store.idcode}),
    {headers:{'Page-Id':this.$store.pageid},
    withCredentials: true})
    .then(response=>{
      this.times= response.data
    })
  },
  data: function(){
    return{
      ordtime:['A','1','2','3','4','B','5','6','7','8','C','D','E','F','G'],
      times:null
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
table.center-all td,th{
  text-align :center;
  vertical-align:middle;
}
.fixed {
  position:absolute;
}
table{
  table-layout:fixed;
}
td {
  min-width:100px;
  max-width:200px;
}
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
