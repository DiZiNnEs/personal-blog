class httpClient {

  getHttpRequest(path) {
    let posts = 123;
    axios
      .get(path)
      .then(response => posts = response.data)
      .catch(error => console.log(error));
    return posts;
  }

  getHttpRequest2(path) {
    let posts = 123;
    axios.get(path)
      .then(function (response) {
        // handle success
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });
  }
}


const http = new httpClient();
console.log(http.getHttpRequest('/api/posts/'))
http.getHttpRequest2('/api/posts/')


// Make a request for a user with a given ID
// axios.get('/api/posts/')
//   .then(function (response) {
//     // handle success
//     console.log(response);
//   })
//   .catch(function (error) {
//     // handle error
//     console.log(error);
//   })
//   .then(function () {
//     // always executed
//   });
