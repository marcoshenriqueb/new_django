<style lang="stylus">
  .django
    letter-spacing 2rem
    margin-top -1rem
    color #99CCFF
    font-size 8rem
    text-transform uppercase
</style>

<template>
  <h1 class="django">{{msg}}</h1>
</template>

<script>
  module.exports = {
    data: function () {
      return {
        msg: 'django'
      }
    }
  }
</script>
