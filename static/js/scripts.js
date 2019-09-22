new Vue({
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('/1wire-devices')
      .then(response => (this.info = response))
  }
})