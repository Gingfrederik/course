<template>
  <main> 
  <div class="container">
    <div class="Aligner">
      <div class="Aligner-item">
        <div class="container">
          <h1>登出囉</h1> 
        </div>
      </div>
    </div>
  </div>
  </main>
</template>


<script>
import axios from 'axios'
axios.defaults.withCredentials = true;

export default {
  name: 'Logout',
  created() {
      axios.get('http://127.0.0.1:5000/logout',
      {headers:{'Page-Id':this.id},withCredentials: true})
      .then(response=>{
        this.$store.pageid='';
        this.$store.idcode='';
        this.$store.loginstatus=false;
    })
  },
  methods: {
  },
  data: function(){
    return {
      id:this.$store.pageid
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
