import getDomainName from "./constants.js";


const getJsonResponse = {
  data() {
    return {
      resultsOfResponse: this.makeHttpRequest(),
      domainName: getDomainName(),
    };
  },
  methods: {
    makeHttpRequest() {
      axios
        .get(`${getDomainName()}/api/posts`)
        .then(response => (this.resultsOfResponse = response.data))
        .catch(error => console.log(error));
    },
    getDomainNameToUrl (slug) {
      return `${getDomainName()}/post/${slug}`;
    }
  },
};

Vue.createApp(getJsonResponse).mount('#getPosts');
