<template>
  <main class="container"> 
  <br></br>

  <div id="table_header" class="container">
    <div class="row justify-content-between">
      <div class="col-md-4 col-sm-10">
        <h5>
          <span class="badge badge-pill badge-default">
            <i class="fa fa-info-circle" aria-hidden="true">&nbsp;課綱</i>
            &nbsp;
            <i class="fa fa-question-circle" aria-hidden="true">&nbsp;選課大全</i>
          </span>
        </h5>
      </div>
      <div class="col-md-4 col-sm-10">
        <h2>登記清單</h2>
      </div>
      <div class="col-md-4 col-sm-10">
      </div>
    </div>
  </div>


  <table id="example" class="table table-striped table-bordered nowrap center-all" cellspacing="0" width="100%">
    <thead>
      <tr> 
        <th class="control max-desktop" data-priority="1"></th>
        <th class="max-desktop" data-priority="2">選項</th>
        <th class="min-tablet-p">資訊</th>
        <th class="max-desktop" data-priority="3">名稱</th>
        <th class="min-tablet-l">時間</th>
        <th class="min-tablet-l">教師</th>
        <th class="min-tablet-p">餘額</th>
        <th class="desktop">總額</th>
        <th class="max-desktop" data-priority="4">代碼</th>
        <th class="desktop">學分</th>
        <th class="desktop">類別</th>
        <th class="desktop">開課系級</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for = "course in courses.datas">
        <td></td>
        <td>

          <div class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-outline-primary" @click="delreg(course.op_code,$event)" >取消</button>
          </div>
        </td>
        <td>
          <a target = "_blank" :href="'http://cmap.cycu.edu.tw:8080/Syllabus/CoursePreview.html?yearTerm='+yearTerm+'&opCode='+course.op_code">
            <i title="課綱" class="fa fa-info-circle fa-2x" aria-hidden="true"></i>
          </a>
          <a target = "_blank" :href="'https://coursewiki.clouder.today/courses/'+course.op_code">
            <i title="選課大全" class="fa fa-question-circle fa-2x" aria-hidden="true"></i>
          </a>
        </td>
        <td>{{course.cname}}</td>
        <td>{{course.op_time_1}}&nbsp;{{course.op_time_2}}&nbsp;{{course.op_time_3}}</td>
        <td>{{course.teacher}}</td>
        <td>{{course.act_remain}}</td>
        <td>{{course.op_man}}</td>
        <td>{{course.op_code}}</td>
        <td>{{course.op_credit}}</td>
        <td>{{course.op_type}}</td>
        <td>{{course.dept_name}}</td>
      </tr>
    </tbody>
  </table>
  <br></br>
  <br></br>
  </main>
</template>

<script>
import axios from 'axios'
import qs from 'qs'

export default {
  name: 'Search',
  created() {
    if(!(this.$store.loginstatus)){
      this.$router.push("/")
    };
    axios.post(this.$store.ip+'/registerlist',
    qs.stringify({'idcode':this.$store.idcode}),
    {headers:{'Page-Id':this.$store.pageid},withCredentials: true})
    .then(response => {
      this.courses = response.data
    }).then(function(event){
      jQuery(document).ready(function() {
        jQuery('#example').DataTable({
          "iDisplayLength": 50,
          responsive: {
            details: {
              display: jQuery.fn.dataTable.Responsive.display.modal( {
                header: function ( row ) {
                  var data = row.data();
                  return '<br>'+data[5]+'</br>'+data[3]+'<style type="text/css">.modal-title {margin:0 auto;}</style>'
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
            targets:[1,2]
          } ],
          order: [[ 8, 'asc' ]],
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
  methods: {
    delreg: function(opcode,event){
      axios.post(this.$store.ip+'/delregister',
      qs.stringify({'opcode':opcode}),
      {headers:{'Page-Id':this.id},withCredentials: true})
      .then(response=>
      {
        if(response.data.result==true)
        {
          jQuery.notify({
            title: "<strong>已取消登記</strong>: ",
            message: ""
          },{
            type: 'success',
            placement: {
              from: "bottom",
              align: "right"
            },  
          });
          axios.post(this.$store.ip+'/registerlist',
          qs.stringify({'idcode':this.$store.idcode}),
          {headers:{'Page-Id':this.$store.pageid},withCredentials: true})
          .then(response => {
            this.$router.push('/tmp');
            this.courses = response.data;
          }) 
        }
        else
        {
          jQuery.notify({
            title: "<strong>失敗</strong>: ",
            message: "<br>"+response.data.message+"</br>"
          },{
            type: 'danger',
            placement: {
              from: "bottom",
              align: "right"
            },  
          });
        }
      }
      )
    }
  },
  data: function(){
    return {
      id:this.$store.pageid,
      yearTerm:this.$store.yearTerm,
      courses:this.courses
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
