var Vue = require('vue');
var VueRouter = require('vue-router');
var VueResource = require('vue-resource');
Vue.use(VueRouter);
Vue.use(VueResource);

var app = Vue.extend ({});

var router = new VueRouter({
  history: true,
	saveScrollPosition: true
});

router.map({
  '/': {
    component: require('./components/routed/home.vue')
  }
});

router.start(app, '#app');
