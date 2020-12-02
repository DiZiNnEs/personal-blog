import getDomainName from "./constants.js";


const getJsonResponse = {
  data() {
    return {
      posts: this.getPosts(),
      domainName: getDomainName(),
    };
  },
  methods: {
    getPosts() {
      axios
        .get(`${getDomainName()}/api/posts`)
        .then(response => (this.posts = response.data))
        .catch(error => console.log(error));
    },
    getDomainNameToUrl (slug) {
      return `${getDomainName()}/post/${slug}`;
    },
  },
};

Vue.createApp(getJsonResponse).mount('#getPosts');
