<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input type="text" v-model="username" placeholder="Username" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Register</button>
      </form>
    </div>

    <div v-if="showSnackbar" class="show-snackbar">{{ errorMessage }}</div>
  </template>
  
  <script>
  export default {
    name: 'UserRegister',
    data() {
      return {
        username: '',
        password: '',
        errorMessage: '',
        showSnackbar: false,
        snackbarTimeout: null,
      }
    },
    methods: {
      async register() {
        try {
          const response = await this.$axios.post('/register', {
            username: this.username,
            password: this.password
          });
          console.log(response.data);
          if (response.status === 201) {
            this.$router.push('/UserLogin');
          }
        } catch (error) {
          console.error(error);
          if (error.response && error.response.data) {
            // Zapisz komunikat o błędzie z serwera
            this.errorMessage = error.response.data.error || 'Wystąpił błąd podczas rejestracji.';
          } else {
            // Zapisz ogólny komunikat o błędzie, jeśli odpowiedź serwera nie jest dostępna
            this.errorMessage = 'Wystąpił błąd podczas rejestracji.';
          }
          this.displaySnackbar(); // Wywołaj snackbar z komunikatem o błędzie
        }
      },
      displaySnackbar() {
        this.showSnackbar = true;
        clearTimeout(this.snackbarTimeout); // Czyść poprzedni timeout, jeśli istnieje
        this.snackbarTimeout = setTimeout(() => {
          this.showSnackbar = false;
        }, 3000); // Ustaw czas wyświetlania snackbar na 3 sekundy
      }
    }
  };
  </script>
  

  <style scoped>
div {
  background-color: #f3e0dc; /* jasny, ciepły kolor tła */
  border-radius: 10px;
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: 50px auto;
  padding: 20px;
  text-align: center;
}

h2 {
  color: #5a2a27; /* ciemniejszy kolor tekstu */
  font-family: 'Cookie', cursive; /* stylowy font, jeśli dostępny */
}

input[type="text"], input[type="password"] {
  border: 2px solid #5a2a27;
  border-radius: 5px;
  margin-bottom: 10px;
  padding: 5px;
  width: 90%;
}

button {
  background-color: #5a2a27; /* kolor przycisku */
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  padding: 10px 20px;
  text-transform: uppercase;
}

button:hover {
  background-color: #7a3b34; /* kolor przycisku po najechaniu */
}
</style>
  