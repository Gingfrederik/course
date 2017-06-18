<template>
  <main> 
  <div class="Aligner">
    <div class="Aligner-item">
      <div class="container">
        <form class="form-signin">
          <h1 class="form-signin-heading">登入</h1>
          <label for="inputID" class="sr-only">學號</label>
          <input type="text" id="inputID" class="form-control" placeholder="學號" required autofocus>
          <label for="inputPassword" class="sr-only">密碼</label>
          <input type="password" id="inputPassword" class="form-control" placeholder="密碼" required>
          <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
        </form>
      </div>
    </div>
  </div>
  </main>
</template>

<script>
export default {
  name: 'Login'
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
