const getJsonResponse = {
  data() {
    return {
      resultsOfResponse: this.makeHttpRequest()
    };
  },
  methods: {
    makeHttpRequest() {
      axios
        .get('http://127.0.0.1:8000/api/posts')
        .then(response => (this.resultsOfResponse = response))
        .catch(error => console.log(error));
    }
  },
};

Vue.createApp(getJsonResponse).mount('#getPosts');
