<template>
  <main>
    <div class="Aligner">
      <div class="Aligner-item">
        <div class="container">
<br></br>
       <div class="alert alert-danger" role="alert">
          <strong>
            <span style="white-space: pre-line">請注意
              本網站為第三方服務
              不會紀錄任何使用者資訊
              但您仍必須了解將帳號密碼交給第三方服務的風險
              本網站將不會承擔任何密碼遺失或是選課問題之責任
            </span>
          </strong>
        </div>
          <form class="form-signin">
            <h1 class="form-signin-heading">登入</h1>
            <label for="inputID" class="sr-only">學號</label>
            <input type="number" v-model="inid" class="form-control" placeholder="學號" required autofocus>
            <label for="inputPassword" class="sr-only">密碼</label>
            <input type="password" v-model="inpass" class="form-control" placeholder="密碼" required>
            <button class="btn btn-lg btn-primary btn-block" @keyup.enter="hash" @click="hash" type="submit">Login</button>
          </form>
<br></br>
<br></br>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
  import axios from 'axios'
  import CryptoJS from 'crypto-js'
  import qs from 'qs'

  axios.defaults.withCredentials = true;

  export default {
    name: 'Login',
    created(){
        axios.get('https://'+this.$store.ip+'/login_init', { withCredentials: true })
          .then(response => {
            this.loginstatus = response.data.result;
            if (this.loginstatus) {
              this.$store.pageid = response.headers['securerandom']
            }
            else {
              this.$router.push('/close')
            }
          })
    },
    methods: {
      hash: function (event) {
                    jQuery.notify({
                      message: "<strong>請稍等</strong>",
                    }, {
                        type: 'info',
			placement: {
                  from: "top",
                  align: "center"
                },  
		    delay:1000,
                      });
              var md5pass = CryptoJS.MD5(this.inpass).toString();
              var hashpass = CryptoJS.algo.HMAC.create(CryptoJS.algo.SHA256, md5pass);
              this.$store.idcode = this.inid;
              hashpass.update(this.inid);
              hashpass.update(this.$store.pageid);
              this.hashout = encodeURIComponent(hashpass.finalize());
	      this.inpass = null;
              axios.post('https://'+this.$store.ip+'/login',
                qs.stringify({
                  'idcode': this.$store.idcode,
                  'hash': this.hashout
                }),
                { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
                .then(response => {
                  if (response.data.result === true) {
                    jQuery.notify({
                      title: "<strong>成功</strong>: ",
                      message: response.data.message
                    }, {
                        type: 'success',
			placement: {
                  from: "top",
                  align: "center"
                },  
                      });
                    this.$store.loginstatus = true
                    axios.get('https://'+this.$store.ip+'/content',
                      { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
                      .then(response => {
                        this.$store.student = response.data
                      })
                      .then(() => {
                        axios.post('https://'+this.$store.ip+'/course',
                          qs.stringify({ 'dept_code': this.$store.student.stmd_cur_dpt }),
                          { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
                          .then(response => {
                            this.$store.courses = response.data.datas;
			    this.$store.gotcou = this.gotcou;
			    this.$store.gotcou.dept_code= this.$store.student.stmd_cur_dpt
                          })
                      .then(() => {
                        axios.post('https://'+this.$store.ip+'/coutime',
                          qs.stringify({ 'idcode': this.$store.idcode}),
                          { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
                          .then(response => {
                            this.$store.coutime = response.data;
                          })
                          .then(() => {
                            this.$router.push('/search')
                          })
                      }
                      )
                      }
                      )
                  }
                  else {
                    jQuery.notify({
                      title: "<strong>失敗</strong>: ",
                      message: response.data.message
                    }, {
                        type: 'danger',
			placement: {
			from: "bottom",
			align: "right"
			},  
                      });
        axios.get('https://'+this.$store.ip+'/login_init', { withCredentials: true })
          .then(response => {
            this.loginstatus = response.data.result;
            if (this.loginstatus) {
              this.$store.pageid = response.headers['securerandom']
            }
            else {
              this.$router.push('/close')
            }
          })
		  }
		})
	    }
    },
    data: function () {
      return {
        inid: '',
        inpass: '',
        hashout: '',
        loginstatus: null,
        gotcou :{
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
	    },
         "op_man": "",
          "bet_bln": "",
	    "coutime":""
      }
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
  
  .form-signin {
    max-width: 30rem;
    padding: 15px;
    margin: 0 auto;
  }
  
  .form-signin .form-signin-heading,
  .form-signin {
    margin-bottom: 10px;
  }
  
  .form-signin {
    font-weight: normal;
  }
  
  .form-signin .form-control {
    position: relative;
    height: auto;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    padding: 10px;
    font-size: 16px;
  }
  
  .form-signin .form-control:focus {
    z-index: 2;
  }
  
  .form-signin input[type="text"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
</style>
