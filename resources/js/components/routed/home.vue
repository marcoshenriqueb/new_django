<template>
  <div class="cover" v-if="!searchBet" transition="fade-out">
    <picture>
      <img src="/static/sitefront/images/manchester-sm.jpg" srcset="/static/sitefront/images/manchester-sm.jpg 800w, /static/sitefront/images/manchester-md.jpg 1200w">
    </picture>
  </div>

  <bet-search :bet-search-results.sync="betSearchResults" :search-bet.sync="searchBet"></bet-search>

  <div class="bet-search-results" v-if="searchBet">
    <div class="bet-search-results__item" v-for="r in betSearchResults">
      <div class="bet-search-results__item_header">
        <h3>{{r.name}}</h3>
      </div>
      <span>{{r.description}}</span>
      <div class="bet-search-results__item_footer">
        <span>Prazo: {{r.deadline}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  module.exports = {
    data: function(){
      return {
        betSearchResults: {}
      }
    },

    props: [
      'searchBet'
    ],

    ready: function(){
      this.$dispatch('header_home', 'header_home')
    },

    components: {
      'bet-search': require('./../local/bet-search.vue')
    }
  }
</script>
