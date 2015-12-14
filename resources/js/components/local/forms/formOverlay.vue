<template>
  <div class="form-overlay_container" @click="exit">
    <div class="form-overlay_content" @click="stopExit">
      <login v-if="formOverlay == 'login'"></login>
      <register v-if="formOverlay == 'register'"></register>
      <div class="form-overlay_content__body" v-if="formOverlay == 'message'">
        <h2 v-if="message">{{message}}</h2>
        <p v-if="subMessage">
          {{subMessage}}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
  module.exports = {
    props: [
      'formOverlay',
      'jwt'
    ],

    data: function(){
      return {
        message: '',
        subMessage: ''
      }
    },

    methods: {
      exit: function(){
        this.formOverlay = false;
      },
      stopExit: function(e){
        e.stopPropagation();
      },
      emailWarning: function(){
        this.formOverlay = 'message'
        this.message = 'Obrigado por se cadastrar!';
        this.subMessage = 'Um email de confirmação foi enviado.';
        setTimeout(function(){
          this.formOverlay = false;
          setTimeout(function(){
            this.message = '';
            this.subMessage = '';
          }.bind(this), 4000)
        }.bind(this), 2000)
      }
    },

    events: {
      'email_sent': 'emailWarning',
      'success': 'exit',
      'register': function(){
        this.formOverlay = 'login';
      },
      'login': function(){
        this.formOverlay = 'register';
      },
      'setJWT': function(data){
        this.jwt = data.token;
        this.$http.headers.common['Authorization'] = 'JWT ' + data.token;
        var now = new Date();
        var d = now.setDate(now.getDate()+14);
        document.cookie = 'jwt=' + data.token + '; expires=' + d + '; path=/'
      }
    },

    components: {
      'login': require('./login.vue'),
      'register': require('./register.vue')
    }
  }

</script>
