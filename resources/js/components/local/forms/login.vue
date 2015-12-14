<template>
  <div class="form-overlay_content__header">
    <hr>
    <h2>Login</h2>
    <hr>
  </div>
  <div class="form-overlay_content__body">
    <label for="username">Usuário:</label>
    <input type="text" name="username" v-model="username">

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
        username: '',
        password: '',
        error: {}
      }
    },

    methods: {
      validateAndLogin: function(){
        var data = {
          username: this.username,
          password: this.password
        };
        this.$http.post('/api-token-auth/', data)
          .success(function(data){
            this.email = '';
            this.password = '';
            this.$dispatch('success');
            this.$dispatch('setJWT', data);
          })
          .error(function(data, status){
            if (status == 400) {
              this.error = ['Credenciais inválidas'];
            }
          });
      },
      goLogin: function(){
        this.$dispatch('login');
      }
    }
  }
</script>
