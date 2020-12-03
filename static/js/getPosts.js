import getDomainName from "./constants.js";


const getJsonResponse = {
  data() {
    return {
      posts: this.getPosts(),
    };
  },
  methods: {
    getPosts() {
      axios
        .get(`/api/posts`)
        .then(response => (this.posts = response.data))
        .catch(error => console.log(error));
    },
    getDomainNameToUrl (slug) {
      return `${getDomainName()}/post/${slug}`;
    },
  },
};

Vue.createApp(getJsonResponse).mount('#getPosts');
