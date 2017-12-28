<template>
  <main> 
  <br></br>
  <div class="container">

    <div id="table_header" class="container">
      <div class="row justify-content-between">
        <div class="col-md-4 col-sm-10">
        </div>
        <div class="col-md-4 col-sm-10">
          <h2>課程表</h2>
        </div>
        <div class="col-md-4 col-sm-10">
          <h5>
            <span class="badge badge-info">
              目前學分:{{$store.student.credit_total}}/{{$store.student.max_limit}}
            </span>
          </h5>
        </div>
      </div>
    </div>
    <br></br>
    <table class="table table-sm table-bordered center-all">
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
          <th class="table-info" scope="row"><font style="color:gray">{{ times[time].time }}</font></th>
          <th class="table-info" scope="row">{{ times[time].flag }}</th>
          <td>{{ times[time].datas.mon.course }}<br><font style="color:gray">{{ times[time].datas.mon.room }}</font></td>
          <td>{{ times[time].datas.tue.course }}<br><font style="color:gray">{{ times[time].datas.tue.room }}</font></td>
          <td>{{ times[time].datas.wed.course }}<br><font style="color:gray">{{ times[time].datas.wed.room }}</font></td>
          <td>{{ times[time].datas.thu.course }}<br><font style="color:gray">{{ times[time].datas.thu.room }}</font></td>
          <td>{{ times[time].datas.fri.course }}<br><font style="color:gray">{{ times[time].datas.fri.room }}</font></td>
          <td>{{ times[time].datas.sat.course }}<br><font style="color:gray">{{ times[time].datas.sat.room }}</font></td>
          <td>{{ times[time].datas.sun.course }}<br><font style="color:gray">{{ times[time].datas.sun.room }}</font></td>
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
    if(!(this.$store.loginstatus)){
      this.$router.push("/")
    };
    axios.post(this.$store.ip+'/timelist',
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
