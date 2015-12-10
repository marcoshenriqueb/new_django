
<template>
  <div class="search-container" :class="{'search-container_filled': searchBet}">
    <h1>{{title}}</h1>
    <input type="text"
           class="search-container--search"
           placeholder="Procure por apostas aqui!"
           v-model="searchBet"
           @keyup="ajaxSearch">
  </div>
</template>

<script>
module.exports = {
  data: function(){
    return {
      title: '',
      titles: [
        'A dilma vai sofrer impeachment em 2015?',
        'O vasco será rebaixado nesse domingo?'
      ]
    }
  },

  props: [
    'searchBet',
    'betSearchResults'
  ],

  ready: function(){
    var i = 0;
    this.title = this.titles[0];
    setInterval(function(){
      i++;
      var n = i%2;
      this.title = this.titles[n];
    }.bind(this), 5000);
  },

  methods: {
    ajaxSearch: function(){
      if (this.searchBet.trim().length > 3) {
        this.$http.get('/ajax/table/search/' + this.searchBet)
          .success(function(data){
            this.betSearchResults = data;
          });
      }else {
        this.betSearchResults = {};
      }
    }
  }
}

</script>
