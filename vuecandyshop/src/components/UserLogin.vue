<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>
  
<script>
export default {
  name: 'UserLogin',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async login() {
      try {
        const response = await this.$axios.post('/login', {
          username: this.username,
          password: this.password
        });

        if (response.status === 200) {
          // Zapisz token w lokalnym składowym magazynie (localStorage) lub ciasteczku (cookie)
          const accessToken = response.data.access_token;
          localStorage.setItem('access_token', accessToken);

          // Dodaj token do nagłówka 'Authorization' w każdym żądaniu Axios
          this.$axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;

          // Przejdź na inną stronę lub wykonaj inne akcje
          this.$router.push('/ProductList');
        }
      } catch (error) {
        console.error(error);
        // Obsłuż błąd logowania
      }
    }
  }
}
</script>



<style scoped>
h2 {
  color: #5a2a27;
  font-family: 'Cookie', cursive;
  text-align: center;
}

div {
  background-color: #f3e0dc;
  border-radius: 10px;
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: 50px auto;
  padding: 20px;
  text-align: center;
}

input {
  border: 2px solid #5a2a27;
  border-radius: 5px;
  margin-bottom: 10px;
  padding: 5px;
  width: 90%;
}

button {
  background-color: #5a2a27;
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  padding: 10px 20px;
  text-transform: uppercase;
}

button:hover {
  background-color: #7a3b34;
}
</style>

  