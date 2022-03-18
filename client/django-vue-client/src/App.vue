<template>
  <Tweets />
</template>

<script>
import Tweets from './components/Tweets.vue'

export default {
  name: 'App',
  components: {
    Tweets
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
