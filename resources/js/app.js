var Vue = require('vue');
var VueRouter = require('vue-router');
var VueResource = require('vue-resource');

Vue.use(VueRouter);
Vue.use(VueResource);

Vue.config.debug = true;
// Vue.http.headers.common['X-CSRF-TOKEN'] = document.getElementById('token').getAttribute('value');

var app = Vue.extend ({

  data: function(){
    return{
      header_home: '',
      searchBet: '',
      formOverlay: false,
      jwt: false
    }
  },

  computed: {
    headerState: function(){
      if (this.searchBet) {
        return false;
      }else if (this.$route.fullPath == '/') {
        return true;
      }else {
        return false;
      }
    }
  },

  ready: function(){
    // var jwt = document.getElementById('jwt');
    // if (jwt != null) {
    //   this.jwt = jwt.getAttribute('value');
    //   this.$http.headers.common['Authorization'] = 'Bearer ' + jwt.getAttribute('value');
    // }
  },

  methods: {
    logout: function(){
      this.$http.get('/auth/logout')
        .success(function(data){
          this.jwt = false;
          delete this.$http.headers.common['Authorization'];
        })
        .error(function(data, status){
          alert(status);
        });
    }
  },

  events: {
    'header_home': function (msg) {
      // `this` in event callbacks are automatically bound
      // to the instance that registered it
      this.header_home = msg;
    }
  },

  components: {
    'form-overlay': require('./components/local/forms/formOverlay.vue')
  }
  
});

var router = new VueRouter({
  history: true,
	saveScrollPosition: true
});

router.map({
    '/' :{
      component: require('./components/routed/home.vue')
    },
    '/faq': {
      component: require('./components/routed/faq.vue')
    },
    '/mercados': {
      component: require('./components/routed/markets.vue')
    }
});

router.start(app, '#app');
