<template>
  <main>
    <div class="Aligner">
      <div class="Aligner-item">
        <div class="container">
          <form class="form-signin">
            <h1 class="form-signin-heading">登入</h1>
            <label for="inputID" class="sr-only">學號</label>
            <input type="number" v-model="inid" class="form-control" placeholder="學號" required autofocus>
            <label for="inputPassword" class="sr-only">密碼</label>
            <input type="password" v-model="inpass" class="form-control" placeholder="密碼" required>
            <button class="btn btn-lg btn-primary btn-block" @click="hash" type="submit">Login</button>
          </form>
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
    methods: {
      hash: function (event) {
        axios.get('https://'+this.$store.ip+'/login_init', { withCredentials: true })
          .then(response => {
            this.loginstatus = response.data.result;
            if (this.loginstatus) {
              this.$store.pageid = response.headers['securerandom']
            }
          })
          .then(() => {
            if (this.loginstatus) {
              var md5pass = CryptoJS.MD5(this.inpass).toString();
              var hashpass = CryptoJS.algo.HMAC.create(CryptoJS.algo.SHA256, md5pass);
              this.$store.idcode = this.inid;
              hashpass.update(this.inid);
              hashpass.update(this.$store.pageid);
              this.hashout = encodeURIComponent(hashpass.finalize());
              this.inpass = null;
            }
          })
          .then(() => {
            if (this.loginstatus) {
              axios.post('https://'+this.$store.ip+'/login',
                qs.stringify({
                  'idcode': this.$store.idcode,
                  'hash': this.hashout
                }),
                { headers: { 'Page-Id': this.$store.pageid }, withCredentials: true })
                .then(response => {
                  if (response.data.result === true) {
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
                            this.$store.courses = response.data.datas
                          })
                          .then(() => {
                            this.$router.push('/search')
                          })
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
                  }
                })
            }
            else {
              this.$router.push('/close')
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
