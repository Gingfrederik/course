<template>
  <main class="container"> 
  <br></br>
  <div id="table_header" class="container">
    <div class="row justify-content-between">
      <div class="col-md-4 col-sm-10">
      </div>
      <div class="col-md-4 col-sm-10">
        <h2>選課時段</h2>
      </div>
      <div class="col-md-4 col-sm-10">
      </div>
    </div>
  </div>
  <table id="example" class="table table-striped table-bordered nowrap center-all" cellspacing="0" width="100%">
    <thead>
      <tr> 
        <th class="control max-desktop" data-priority="1"></th>
        <th class="max-desktop" data-priority="2">階段</th>
        <th class="min-tablet-p">開始</th>
        <th class="min-tablet-p">結束</th>
        <th class="desktop">備註</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="stage in stages.datas">
        <td></td>
        <td>{{stagetype[stage.sn_stage_type]}}</td>
        <td>{{stage.bgtime}}</td>
        <td>{{stage.edtime}}</td>
        <td>{{stage.remark}}</td>
      </tr>
    </tbody>
  </table>
  <br></br>
  </main>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Stage',
  created() {
    axios.get(this.$store.ip+'/stage')
    .then(response => {
      this.stages = response.data
    }).then(function(event){
      jQuery(document).ready(function() {
        jQuery('#example').DataTable({
        "iDisplayLength": 100,
        "searching": false,
          responsive: {
            details: {
              display: jQuery.fn.dataTable.Responsive.display.modal( {
                header: function ( row ) {
                  var data = row.data();
                  return '<br>'+data[1]+'</br>'+'<style type="text/css">.modal-title {margin:0 auto;}</style>'
                }
              } ),
              renderer: function ( api, rowIdx, columns ) {
                var data = $.map( columns, function ( col, i ) {
                  return col.hidden ?
                  '<tr data-dt-row="'+col.rowIndex+'" data-dt-column="'+col.columnIndex+'">'+
                  '<td>'+col.title+':'+'</td> '+
                  '<td>'+col.data+'</td>'+
                  '</tr>' :
                  '';
                } ).join('');
                return data ?
                $('<table/ class="table dtr-details">').append( data ) :
                false;
              }          
            }

          },   
          columnDefs: [ {
            className: 'control',
            orderable: false,
            targets:0
          },
          {
            orderable: false,
            targets:[1,2,3,4]
          }],
          "pagingType": "full",
          "language": {
            "processing":   "處理中...",
            "loadingRecords": "載入中...",
            "lengthMenu":   "顯示 _MENU_ 項結果",
            "zeroRecords":  "沒有符合的結果",
            "info":         "顯示第 _START_ 至 _END_ 項結果，共 _TOTAL_ 項",
            "infoEmpty":    "顯示第 0 至 0 項結果，共 0 項",
            "infoFiltered": "",
            "infoPostFix":  "",
            "search":       "搜尋:",
            "paginate": {
              "first":    "第一頁",
              "previous": "上一頁",
              "next":     "下一頁",
              "last":     "最後一頁"
            },
            "aria": {
              "sortAscending":  ": 升冪排列",
              "sortDescending": ": 降冪排列"
            }
          }
        }) 
      })
    })
  },
  data: function(){
    return {
      stagetype:{
        "11":"第一次篩選登記",
        "12":"第二次篩選登記",
        "21":"第一次加退選",
        "22":"第二次加退選",
        "23":"第三次加退選"
      },
    stages:null
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#table_header {
  padding-bottom:15px;
}
table.center-all td,th{
  text-align :center;
  vertical-align:middle;
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
</style>
