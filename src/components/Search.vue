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
      </div>
      <div class="col-md-4 col-sm-10">
        <div class="btn-group" role="group" aria-label="Basic example">
          <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#showModal">
            顯示設定
          </button>
          <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#searchModal">
            進階搜尋 
          </button>
        </div>
      </div>
    </div>
  </div>


  <div class="modal fade bd-example-modal-sm" id="showModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-sm" role="document">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">顯示設定</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <div class="modal-body">
          <div class="container">
            <form>
              <div class="form-group row justify-content-center">
                <label for="inputPassword3" class="col-sm-5 col-form-label">衝堂顯示</label>
                <div class="col-sm-4">
                  <label class="switch">
                    <input type="checkbox">
                    <div class="slider round"></div>
                  </label>
                </div>
              </div>
              <div class="form-group row justify-content-center">
                <label for="inputPassword3" class="col-sm-5 col-form-label">衝堂顯示</label>
                <div class="col-sm-4">
                  <label class="switch">
                    <input type="checkbox">
                    <div class="slider round"></div>
                  </label>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">關閉</button>
          <button type="button" id="searchSubmit" class="btn btn-primary">確定</button>
        </div>

      </div>
    </div>
  </div>


  <div class="modal fade" id="searchModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">進階搜尋</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <div class="modal-body">
          <div class="container">
            <form>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-3 col-form-label">Email</label>
                <div class="col-sm-8">
                  <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
                </div>
              </div>
              <div class="form-group row">
                <label for="inputPassword3" class="col-sm-3 col-form-label">Password</label>
                <div class="col-sm-8">
                  <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">關閉</button>
          <button type="button" class="btn btn-warning">清除搜尋條件</button>
          <button type="button" id="searchSubmit" class="btn btn-primary">搜尋</button>
        </div>

      </div>
    </div>
  </div>


  <table id="example" class="table table-striped table-bordered nowrap center-all" cellspacing="0" width="100%">
    <thead>
      <tr> 
        <th class="control max-desktop" data-priority="1"></th>
        <th class="desktop">選項</th>
        <th class="min-tablet-p" data-priority="4">資訊</th>
        <th class="max-desktop" data-priority="2">課程名稱</th>
        <th class="max-desktop" data-priority="3">時間</th>
        <th class="min-tablet-l">授課教師</th>
        <th class="min-tablet-l">選課餘額</th>
        <th class="desktop">開課人數</th>
        <th class="desktop">課程代碼</th>
        <th class="desktop">學分</th>
        <th class="desktop">課程類別</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for = "course in courses ">
        <td></td>
        <td>

        <div class="btn-group" role="group" aria-label="Basic example">
          <button type="button" id="traceSubmit" class="btn btn-outline-primary">追蹤</button>
          <button type="button" id="selectSubmit" class="btn btn-primary">加選</button>
        </div>
        </td>
        <td>
          <a target = "_blank" :href="'http://cmap.cycu.edu.tw:8080/Syllabus/CoursePreview.html?yearTerm=1052&opCode='+course.OP_CODE">
            <i class="fa fa-info-circle fa-2x" aria-hidden="true"></i>
          </a>
          <a target = "_blank" :href="'https://coursewiki.clouder.today/courses?by_title='+course.CURS_NM_C_S+'&by_instructor='+course.TEACHER_CNAME">
            <i class="fa fa-question-circle fa-2x" aria-hidden="true"></i>
          </a>
        </td>
        <td>{{course.CURS_NM_C_S}}</td>
        <td>{{course.OP_TIME_1}}</td>
        <td>{{course.TEACHER_CNAME}}</td>
        <td>{{course.ACT_REMAIN}}/{{course.OP_MAN}}</td>
        <td>{{course.OP_MAN}}</td>
        <td>{{course.OP_CODE}}</td>
        <td>{{course.OP_CREDIT}}</td>
        <td>{{course.OP_TYPE}}</td>
      </tr>
    </tbody>
  </table>
  <br></br>
  <br></br>
  </main>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Search',
  created() {
    axios.get('https://idontknow.com.tw/course_list')
    .then(response => {
      // JSON responses are automatically parsed.
      this.courses = response.data
    }).then(function(event){
      jQuery(document).ready(function() {
        jQuery('#example').DataTable({
          responsive: {
            details: {
              display: jQuery.fn.dataTable.Responsive.display.modal( {
                header: function ( row ) {
                  var data = row.data();
return '<br>'+data[5]+'</br>'+data[3]+'<style type="text/css">.modal-title {margin:0 auto;}</style>'
                }
              } ),
              renderer: jQuery.fn.dataTable.Responsive.renderer.tableAll( {
                tableClass: 'table'
              } )            
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
          order: [[ 3, 'asc' ]],
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
      courses:this.courses
    }
  },
  methods: {
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
