<template>
  <div class="form-overlay_container" @click="exit">
    <div class="form-overlay_content" @click="stopExit">
      <login v-if="formOverlay == 'login'"></login>
      <register v-if="formOverlay == 'register'"></register>
    </div>
  </div>
</template>

<script>
  module.exports = {
    props: [
      'formOverlay',
      'jwt'
    ],

    methods: {
      exit: function(){
        this.formOverlay = false;
      },
      stopExit: function(e){
        e.stopPropagation();
      }
    },

    events: {
      'success': 'exit',
      'register': function(){
        this.formOverlay = 'login';
      },
      'login': function(){
        this.formOverlay = 'register';
      },
      'setJWT': function(data){
        this.jwt = data;
        this.$http.headers.common['Authorization'] = 'Bearer ' + data;
      }
    },

    components: {
      'login': require('./login.vue'),
      'register': require('./register.vue')
    }
  }

</script>
