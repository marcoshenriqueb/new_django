<template>
  <div class="form-overlay_content__header">
    <hr>
    <h2>Login</h2>
    <hr>
  </div>
  <div class="form-overlay_content__body">
    <label for="email">Email:</label>
    <input type="text" name="email" v-model="email">

    <label for="password">Senha:</label>
    <input type="password" name="password" v-model="password">

    <button @click="validateAndLogin" name="button">Entrar</button>

    <span class="error" v-for="e in error">{{e}}</span>

    <hr>

    <span>Não tem uma conta ainda? <a @click="goLogin">Cadastre-se!</a></span>
  </div>
</template>

<script>
  module.exports = {

    data: function(){
      return{
        email: '',
        password: '',
        error: {}
      }
    },

    methods: {
      validateAndLogin: function(){
        var data = {
          email: this.email,
          password: this.password
        };
        this.$http.post('/auth/login', data)
          .success(function(data){
            this.email = '';
            this.password = '';
            this.$dispatch('success');
            this.$dispatch('setJWT', data);
          })
          .error(function(data, status){
            if (status == 401) {
              this.error = data;
            }
          });
      },
      goLogin: function(){
        this.$dispatch('login');
      }
    }
  }
</script>
