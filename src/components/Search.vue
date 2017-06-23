<template>
  <main class="container"> 
  <br></br>
  <table id="example" class="table table-striped table-bordered nowrap" cellspacing="0" width="100%">
    <thead>
      <tr>
        <th>課程名稱</th>
        <th></th>
        <th>時間</th>
        <th>授課教師</th>
        <th>選課餘額</th>
        <th>開課人數</th>
        <th>課程代碼</th>
        <th>學分</th>
        <th>課程類別</th>
      </tr>
    </thead>
    <tbody>
	<tr v-for = "course in courses ">
    <td>{{course.CURS_NM_C_S}}</td>
    <td>
		<a target = "_blank" :href="'http://cmap.cycu.edu.tw:8080/Syllabus/CoursePreview.html?yearTerm=1052&opCode='+course.OP_CODE">
		    <i class="fa fa-info-circle fa-lg" aria-hidden="true"></i>
		</a>
		<a target = "_blank" :href="'https://coursewiki.clouder.today/courses?by_title='+course.CURS_NM_C_S+'&by_instructor='+course.TEACHER_CNAME">
		    <i class="fa fa-question-circle fa-lg" aria-hidden="true"></i>
		</a>
	    </td>
            <td>{{course.OP_TIME_1}}</td>
            <td>{{course.TEACHER_CNAME}}</td>
            <td>{{course.ACT_REMAIN}}</td>
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
                  return data[2]+' '+data[0];
                }
              } ),
              renderer: jQuery.fn.dataTable.Responsive.renderer.tableAll( {
                tableClass: 'table'
              } )
            }
          }   
        }) 
      })
    })
  },
    data:function (course) {
      return {
        courses:this.courses
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
</style>
