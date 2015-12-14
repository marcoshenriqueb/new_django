var Vue = require('vue');
var VueRouter = require('vue-router');
var VueResource = require('vue-resource');

Vue.use(VueRouter);
Vue.use(VueResource);

Vue.config.debug = true;
var csrf = document.getElementById('token').getAttribute('value');
Vue.http.headers.common['X-CSRFToken'] = csrf;

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
    var cookieValue = document.cookie.replace(/(?:(?:^|.*;\s*)jwt\s*\=\s*([^;]*).*$)|^.*$/, "$1");
    if (cookieValue != null) {
      this.jwt = cookieValue;
      this.$http.headers.common['Authorization'] = 'JWT ' + cookieValue;
    }
  },

  methods: {
    logout: function(){
      this.jwt = false;
      delete this.$http.headers.common['Authorization'];
      document.cookie = 'jwt=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
  },

  events: {
    'header_home': function (msg) {
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
