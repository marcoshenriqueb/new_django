var Vue = require('vue');
var VueRouter = require('vue-router');
var VueResource = require('vue-resource');
Vue.use(VueRouter);
Vue.use(VueResource);

var app = Vue.extend ({

  data: function(){
    return {
      title: 'django'
    };
  }

});

var router = new VueRouter({
  history: true,
	saveScrollPosition: true
});

router.map({});

router.start(app, '#app');
