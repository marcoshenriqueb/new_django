<template>
  <div class="form-overlay_content__header">
    <hr>
    <h2>Cadastro</h2>
    <hr>
  </div>
  <div class="form-overlay_content__body">
    <label for="username">Nome de usuário:</label>
    <input type="text" name="username" v-model="username">

    <label for="email">Email:</label>
    <input type="email" name="email" v-model="email">

    <label for="password">Senha:</label>
    <input type="password" name="password" v-model="password">

    <label for="password">Confirme a senha:</label>
    <input type="password" name="password_confirmation" v-model="password_confirmation">

    <button @click="validateAndRegister" name="button">Cadastrar</button>

    <span class="error" v-for="e in error">{{e[0]}}</span>

    <hr>

    <span>Já é cadastrado? <a @click="goRegister">Entre aqui!</a></span>
  </div>
</template>

<script>
  module.exports = {

    data: function(){
      return {
        username: '',
        email: '',
        password: '',
        password_confirmation: '',
        error: {}
      }
    },

    methods: {
      validateAndRegister: function(){
        var data = {
          username: this.username,
          email: this.email,
          password: this.password,
        };
        this.$http.post('/api/users/', data)
          .success(function(data){
            this.name = '';
            this.email = '';
            this.password = '';
            this.password_confirmation = '';
            this.$dispatch('email_sent');
          })
          .error(function(data, status){
            if (status == 400) {
              this.error = data;
            }
          });
      },
      goRegister: function(){
        this.$dispatch('register');
      }
    }
  }
</script>
