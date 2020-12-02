import getDomainName from "./constants.js";


const Post = {
  data() {
    return {
      post: this.getPost(1),
    }
  },
  methods: {
    getPost(slug) {
      axios
        .get(`${getDomainName()}/api/post/${slug}`)
        .then(response => (this.posts = response.data))
        .catch(error => console.log(error));
    },
  }
};

Vue.createApp(Post).mount('#post');
