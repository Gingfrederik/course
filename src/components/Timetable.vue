<template>
  <main> 
  <br></br>
  <div class="container">
    <table class="table table-responsive center-all">
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
        <tr v-for="time in times" v-bind:class="[time.flag === 'B'?'table-active':'']">
          <th class="table-info" scope="row">{{ time.time }}</th>
          <th class="table-info">{{ time.flag }}</th>
          <td>{{ time.mon }}</td>
          <td>{{ time.tues }}</td>
          <td>{{ time.wed }}</td>
          <td>{{ time.thur }}</td>
          <td>{{ time.fri }}</td>
          <td>{{ time.sat }}</td>
          <td>{{ time.sun }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <br></br>
  <br></br>
  </main>
</template>

<script>
export default {
  name: 'Home',
  data: function(){
    return {
      times:  [
      {
        "flag": "A",
        "time": "07:10 ~ 08:00",
        "mon": "",
        "tues": "",
        "wed": "田徑(男.女) 一",
        "thur": "",
        "fri": "田徑(男.女) 一",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "1",
        "time": "08:10 ~ 09:00",
        "mon": "",
        "tues": "類比電路實驗\n電學大樓      306",
        "wed": "電子學(一)\n真知教學大樓  409",
        "thur": "",
        "fri": "",
        "sat": "",
        "sun": ""
      },
      {

        "flag": "2",
        "time": "09:10 ~ 10:00",
        "mon": "",
        "tues": "類比電路實驗\n電學大樓      306",
        "wed": "",
        "thur": "通訊實驗\n電學大樓      306",
        "fri": "",
        "sat": "",
        "sun": ""
      },
      {

        "flag": "3",
        "time": "10:10 ~ 11:00",
        "mon": "電子學(一)\n真知教學大樓  512",
        "tues": "類比電路實驗\n電學大樓      306",
        "wed": "",
        "thur": "通訊實驗\n電學大樓      306",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "4",
        "time": "11:10 ~ 12:00",
        "mon": "電子學(一)\n真知教學大樓  512",
        "tues": "",
        "wed": "",
        "thur": "通訊實驗\n電學大樓      306",
        "fri": "",
        "sat": "",
        "sun": ""
      },
      {

        "flag": "B",
        "time": "12:10 ~ 13:00",
        "mon": "",
        "tues": "",
        "wed": "",
        "thur": "",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "5",
        "time": "13:10 ~ 14:00",
        "mon": "普通物理實驗(一)",
        "tues": "通信調變理論\n真知教學大樓  510",
        "wed": "電子學(三)\n真知教學大樓  517",
        "thur": "電子學(三)\n真知教學大樓  409",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "6",
        "time": "14:10 ~ 15:00",
        "mon": "普通物理實驗(一)",
        "tues": "",
        "wed": "",
        "thur": "電子學(三)\n真知教學大樓  409",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "7",
        "time": "15:10 ~ 16:00",
        "mon": "普通物理實驗(一)",
        "tues": "日本國情與文化\n真知教學大樓  618",
        "wed": "通信調變理論\n真知教學大樓  510",
        "thur": "中西哲學家的生命觀\n真知教學大樓  816",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "8",
        "time": "16:10 ~ 17:00",
        "mon": "",
        "tues": "日本國情與文化\n真知教學大樓  618",
        "wed": "通信調變理論\n真知教學大樓  510",
        "thur": "中西哲學家的生命觀\n真知教學大樓  816",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "C",
        "time": "17:05 ~ 17:55",
        "mon": "",
        "tues": "",
        "wed": "",
        "thur": "",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "D",
        "time": "18:00 ~ 18:50",
        "mon": "",
        "tues": "",
        "wed": "",
        "thur": "",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "E",
        "time": "18:55 ~ 19:45",
        "mon": "",
        "tues": "",
        "wed": "",
        "thur": "",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {
        "flag": "F",
        "time": "19:50 ~ 20:40",
        "mon": "",
        "tues": "",
        "wed": "",
        "thur": "",
        "fri": "",
        "sat": "",
        "sun": ""

      },
      {

        "flag": "G",
        "time": "20:45 ~ 21:35",
        "mon": "",
        "tues": "",
        "wed": "",
        "thur": "",
        "fri": "專題研究(一)",
        "sat": "",
        "sun": ""
      }
    ]}
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
