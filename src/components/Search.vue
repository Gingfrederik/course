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
            &nbsp;
            <i class="fa fa-check-circle" aria-hidden="true">&nbsp;跨系</i>
          </span>
        </h5>
      </div>
      <div class="col-md-4 col-sm-10">
        <h2>課程查詢</h2>
      </div>
      <div class="col-md-4 col-sm-10">
        <div class="btn-group" role="group" aria-label="Basic example">
          <button type="button" class="btn btn-primary" @click="refresh">
            <i class="fa fa-refresh" aria-hidden="true"></i>
          </button>
          <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#showModal">
            顯示設定
          </button>
          <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#searchModal">
            搜尋 
          </button>
        </div>
      </div>
    </div>
  </div>


  <div class="modal fade bd-example-modal-sm" id="showModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                                                                                         aria-hidden="true">
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
                    <input v-model="$store.crush" type="checkbox">
                    <div class="slider round"></div>
                  </label>
                </div>
              </div>
              <!--
                <div class="form-group row justify-content-center">
                <label for="inputPassword3" class="col-sm-5 col-form-label">已修顯示</label>
                <div class="col-sm-4">
                <label class="switch">
                <input type="checkbox">
                <div class="slider round"></div>
                </label>
                </div>
                </div>
              -->
            </form>
          </div>
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="refresh" data-dismiss="modal">確定</button>
        </div>

      </div>
    </div>
  </div>


  <div class="modal fade" id="timeModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">上課時間</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <div class="modal-body">
          <div class="container">
            <table class="table table-sm table-bordered center-all">
              <thead class="thead-inverse">
                <tr>
                  <th></th>
                  <th>一</th>
                  <th>二</th>
                  <th>三</th>
                  <th>四</th>
                  <th>五</th>
                  <th>六</th>
                  <th>日</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="time in ordtime" v-bind:class="[time === 'B'?'table-active':'']">
                  <th class="table-info" scope="row">{{time}}</th>
                  <td id="bgcheck">
                    <input type="checkbox" :value="1+time" v-model="$store.gotcou.course_time" autocomplete="off">
                  </td>
                  <td id="bgcheck">
                    <input type="checkbox" :value="2+time" v-model="$store.gotcou.course_time" autocomplete="off">
                  </td>
                  <td id="bgcheck">
                    <input type="checkbox" :value="3+time" v-model="$store.gotcou.course_time" autocomplete="off">
                  </td>
                  <td id="bgcheck">
                    <input type="checkbox" :value="4+time" v-model="$store.gotcou.course_time" autocomplete="off">
                  </td>
                  <td id="bgcheck">
                    <input type="checkbox" :value="5+time" v-model="$store.gotcou.course_time" autocomplete="off">
                  </td>
                  <td id="bgcheck">
                    <input type="checkbox" :value="6+time" v-model="$store.gotcou.course_time" autocomplete="off">
                  </td>
                  <td id="bgcheck">
                    <input type="checkbox" :value="7+time" v-model="$store.gotcou.course_time" autocomplete="off">
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="clearcheck" data-toggle="modal" data-target="#searchModal" data-dismiss="modal">取消</button>
          <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#searchModal" data-dismiss="modal">確定</button>
        </div>

      </div>
    </div>
  </div>


  <div class="modal fade" id="searchModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">搜尋</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <div class="modal-body">
          <div class="container">
            <form>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">代碼</label>
                <div class="col-sm-8">
                  <input type="text" class="form-control" placeholder="大小寫皆可" v-model="$store.gotcou.op_code">
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">名稱</label>
                <div class="col-sm-8">
                  <input type="text" class="form-control" placeholder="" v-model="$store.gotcou.cname">
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">授課老師</label>
                <div class="col-sm-8">
                  <input type="text" class="form-control" placeholder="" v-model="$store.gotcou.teacher">
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">開課系級</label>
                <div class="col-sm-8">
                  <input type="text" class="form-control" placeholder="EX:電機,電機四甲" v-model="$store.gotcou.dept_name">
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">上課時間</label>
                <div class="col-sm-8">
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#timeModal" data-dismiss="modal">
                    選擇時間 
                  </button>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">選修別</label>
                <div class="col-sm-8">
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" name="op_stdy" type="radio" value="必修" v-model="$store.gotcou.op_stdy">必修
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" name="op_stdy" type="radio" value="選修" v-model="$store.gotcou.op_stdy">選修 
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" name="op_stdy" type="radio">Both
                    </label>
                  </div>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">跨系</label>
                <div class="col-sm-8">
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="1" v-model="$store.gotcou.bet_dept" type="checkbox" >
                    </label>
                  </div>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">課程類別</label>
                <div class="col-sm-8">
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="一般" v-model="$store.gotcou.op_type.a" type="checkbox" >一般
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="人哲" v-model="$store.gotcou.op_type.b" type="checkbox" >人哲
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="公民" v-model="$store.gotcou.op_type.c" type="checkbox" >公民
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="宗哲" v-model="$store.gotcou.op_type.d" type="checkbox" >宗哲
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="天" v-model="$store.gotcou.op_type.e" type="checkbox" >天
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="人" v-model="$store.gotcou.op_type.f" type="checkbox" >人
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="物" v-model="$store.gotcou.op_type.g" type="checkbox" >物
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="我" v-model="$store.gotcou.op_type.h" type="checkbox" >我
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="文學" v-model="$store.gotcou.op_type.i" type="checkbox" >文學
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="科技" v-model="$store.gotcou.op_type.j" type="checkbox" >科技
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="科學" v-model="$store.gotcou.op_type.k" type="checkbox" >科學
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="英聽" v-model="$store.gotcou.op_type.l" type="checkbox" >英聽
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="體育" v-model="$store.gotcou.op_type.m" type="checkbox" >體育
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="歷史" v-model="$store.gotcou.op_type.n" type="checkbox" >歷史
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="軍訓" v-model="$store.gotcou.op_type.o" type="checkbox" >軍訓
                    </label>
                  </div>
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="學程" v-model="$store.gotcou.op_type.p" type="checkbox" >學程
                    </label>
                  </div>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-3 col-form-label">選課餘額</label>
                <div class="col-sm-8">
                  <div class="form-check form-check-inline">
                    <label class="form-check-label">
                      <input class="form-check-input" value="act_remain" v-model="$store.gotcou.act_remain" type="checkbox" >大於0
                    </label>
                  </div>
                </div>
              </div>

            </form>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">關閉</button>
          <button type="button" class="btn btn-warning" @click="init_cou" data-dismiss="modal">清除搜尋條件</button>
          <button type="button" class="btn btn-primary" @click="cou" data-dismiss="modal">搜尋</button>
        </div>

      </div>
    </div>
  </div>

  <table id="example" class="table table-striped table-bordered nowrap center-all" cellspacing="0" width="100%">
    <thead>
      <tr>
        <th class="control max-desktop" data-priority="1"></th>
        <th class="max-desktop" data-priority="2">選項</th>
        <th class="min-tablet-p">資訊</th>
        <th class="max-desktop" data-priority="3">名稱(跨)</th>
        <th class="min-tablet-l">時間</th>
        <th class="min-tablet-l">教師</th>
        <th class="min-tablet-p">餘額(總)</th>
        <th class="desktop">去年登記</th>
        <th class="max-desktop" data-priority="4">代碼</th>
        <th class="desktop">學分</th>
        <th class="desktop">類別</th>
        <th class="desktop">開課系級</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="course in $store.courses" :key="course.op_code">
        <td class="control"></td>
        <td :data-id="course.op_code" v-model="course.op_code">
          <div v-if="$store.stagecode==6" class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-outline-primary btn-sm" @click="tra(course.op_code,$event)">追蹤</button>
            <button type="button" class="btn btn-primary btn-sm" @click="reg(course.op_code,$event)">登記</button>
          </div>
          <div v-else-if="$store.stagecode==3" class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-outline-primary btn-sm" @click="tra(course.op_code,$event)">追蹤</button>
            <button type="button" class="btn btn-primary btn-sm" @click="addcou(course.op_code,$event)">加選</button>
          </div>
          <div v-else class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-outline-primary btn-sm" @click="tra(course.op_code,$event)">追蹤</button>
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
        <td>{{course.cname}}<i v-if="course.bet_dept" class="fa fa-check-circle" aria-hidden="true"></i></td>
        <td>{{course.op_time_1}}&nbsp;{{course.op_time_2}}&nbsp;{{course.op_time_3}}</td>
        <td>{{course.teacher}}</td>
        <td>{{course.act_remain}}&nbsp;({{course.op_man}})</td>
        <td>{{course.last_reg_man}}</td>
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
    jQuery(document).ready(function () {
      jQuery('#example').DataTable({
        "iDisplayLength": 100,
        "searching": false,
        responsive: {
          details: {
            display: jQuery.fn.dataTable.Responsive.display.modal({
              header: function (row) {
                var data = row.data();
                return '</br>' + data[3] + '</br>' + data[8] + '</br>' + data[5] + '<style type="text/css">.modal-title {margin:0 auto;}</style>'
              }
            }),
            renderer: function (api, rowIdx, columns) {
              var data = $.map(columns, function (col, i) {
                return col.hidden ?
                '<tr data-dt-row="' + col.rowIndex + '" data-dt-column="' + col.columnIndex + '">' +
                '<td>' + col.title + ':' + '</td> ' +
                '<td>' + col.data + '</td>' +
                '</tr>' :
                '';
              }).join('');
              return data ?
              $('<table/ class="table dtr-details">').append(data) : false;
            }
          }

        },
        columnDefs: [{
          className: 'control',
          orderable: false,
          targets: 0
        },
        {
          orderable: false,
          targets: [1, 2]
        }],
        order: [[9, 'asc']],
        "pagingType": "full",
        "language": {
          "processing": "處理中...",
          "loadingRecords": "載入中...",
          "lengthMenu": "顯示 _MENU_ 項結果",
          "zeroRecords": "沒有符合的結果",
          "info": "顯示第 _START_ 至 _END_ 項結果，共 _TOTAL_ 項",
          "infoEmpty": "顯示第 0 至 0 項結果，共 0 項",
          "infoFiltered": "",
          "infoPostFix": "",
          "search": "搜尋:",
          "paginate": {
            "first": "第一頁",
            "previous": "上一頁",
            "next": "下一頁",
            "last": "最後一頁"
          },
          "aria": {
            "sortAscending": ": 升冪排列",
            "sortDescending": ": 降冪排列"
          }
        }
      })
    })
  },
  methods: {
    refresh: function(){
      if(this.$store.crush==false)
      {
        this.$store.gotcou.coutime = this.$store.coutime
      }
      else
      {
        this.$store.gotcou.coutime = null
      }
      axios.post(this.$store.ip+'/course',
      qs.stringify(this.$store.gotcou),
      { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
      .then(response => {
        this.$router.push('/tmp');
        this.$store.courses = response.data.datas;
      })
    },
    init_cou: function () {
      jQuery(":checkbox").prop('checked', false).parent().removeClass('active');
      jQuery(":radio").prop('checked', false).parent().removeClass('active');
      this.clear();
      if(this.$store.crush==false)
      {
        this.$store.gotcou.coutime = this.$store.coutime
      }
      else
      {
        this.$store.gotcou.coutime = null
      }
      this.$store.gotcou.dept_code = this.$store.student.stmd_cur_dpt;
      axios.post(this.$store.ip+'/course',
      qs.stringify(this.$store.gotcou),
      { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
      .then(response => {
        this.$router.push('/tmp')
        this.$store.courses = response.data.datas;
      })
    },
    cou: function () {
      this.$store.gotcou.dept_code = "";
      if(this.$store.crush==false)
      {
        this.$store.gotcou.coutime = this.$store.coutime
      }
      else
      {
        this.$store.gotcou.coutime = null
      }
      axios.post(this.$store.ip+'/course',
      qs.stringify(this.$store.gotcou),
      { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
      .then(response => {
        this.$router.push('/tmp')
        this.$store.courses = response.data.datas
      })
    },
    reg: function (opcode, event) {
      axios.post(this.$store.ip+'/addregister',
      qs.stringify({ 'opcode': opcode }),
      { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
      .then(response => {
        if (response.data.result == true) {
          jQuery.notify({
            title: "<strong>已登記</strong>: ",
            message: "<br>" + response.data.data.op_code + "</br>" +
            response.data.data.cname
          }, {
            type: 'success',
            placement: {
              from: "bottom",
              align: "right"
            },  
          });
        }
        else {
          jQuery.notify({
            title: "<strong>失敗</strong>: ",
            message: "<br>" + response.data.message + "</br>"
          }, {
            type: 'danger',
            placement: {
              from: "bottom",
              align: "right"
            },  
          });
        }
      }
      )
    },
    tra: function (opcode, event) {
      axios.post(this.$store.ip+'/addtrace',
      qs.stringify({ 'opcode': opcode }),
      { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
      .then(response => {
        if (response.data.result == true) {
          jQuery.notify({
            title: "<strong>已追蹤</strong>:",
            message: "<br>" + response.data.data.op_code + "</br>" +
            response.data.data.cname
          }, {
            type: 'success',
            placement: {
              from: "bottom",
              align: "right"
            },  
          });
        }
      }
      )
    },
    addcou: function (opcode, event) {
      axios.post(this.$store.ip+'/addgot',
      qs.stringify({ 'opcode': opcode }),
      { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
      .then(response => {
        if (response.data.result == true) {
          jQuery.notify({
            title: "<strong>已加選</strong>: ",
            message: "<br>" + response.data.data.op_code + "</br>" +
            response.data.data.cname
          }, {
            type: 'success',
            placement: {
              from: "bottom",
              align: "right"
            },  
          });
        }
        else {
          jQuery.notify({
            title: "<strong>失敗</strong>: ",
            message: "<br>" + response.data.message + "</br>"
          }, {
            type: 'danger',
            placement: {
              from: "bottom",
              align: "right"
            },  
          });
        }
      }
      )
    },
    clearcheck: function(){
      this.$store.gotcou.course_time=[]
    },
    clear: function(){
      this.$store.gotcou = {
        "dept_code": "",
        "cross_type": "",
        "filter_remain": "",
        "cname": "",
        "op_quality": "",
        "mg_dept_code": "",
        "non_stop": "",
        "op_code": "",
        "op_credit": "",
        "op_time_1": "",
        "op_time_2": "",
        "op_time_3": "",
        "teacher": "",
        "transfer_mark": "",
        "filtered": "",
        "act_man": "",
        "design": "",
        "bet_dept": "",
        "reg_man": "",
        "memo1": "",
        "sn_course_type": "",
        "filter_man": "",
        "sex": "",
        "last_reg_man": "",
        "withdraw_bits": "",
        "dept_name": "",
        "upper_man": "",
        "div_code": "",
        "mg_dept_name": "",
        "act_remain": "",
        "op_stdy": "",
        "first_man": "",
        "course_time": [],
        "op_type":
        {
          "a": "",
          "b": "",
          "b": "",
          "d": "",
          "e": "",
          "f": "",
          "g": "",
          "h": "",
          "i": "",
          "j": "",
          "k": "",
          "l": "",
          "m": "",
          "n": "",
          "o": "",
          "p": ""
        },
        "op_man": "",
        "bet_bln": "",
        "coutime":""
      }
    },
  },
  data: function () {
    return {
      id: this.$store.pageid,
      stagecode:this.$store.stagecode,
      yearTerm:this.$store.yearTerm,
      ordtime:['A','1','2','3','4','B','5','6','7','8','C','D','E','F','G'],
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.modal {
  overflow-y:auto;
}

#bgcheck input {
  width: 20px; 
  height: 20px;
}

#table_header {
  padding-bottom: 15px;
}

table.center-all td,
th {
  text-align: center;
  vertical-align: middle;
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
