<template>
  <div class="form-container">
    <h2 class="form-title">Dodaj Produkt</h2>
    <form @submit.prevent="submitForm" class="add-product-form">
      <div class="form-field">
        <label for="name" class="form-label">Nazwa</label>
        <input type="text" id="name" v-model="product.name" class="form-input">
      </div>
      <div class="form-field">
        <label for="price" class="form-label">Cena</label>
        <input type="number" id="price" v-model="product.price" class="form-input">
      </div>
      <button type="submit" class="form-button">Dodaj Produkt</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      product: {
        name: '',
        price: 0
      }
    };
  },
  methods: {
    submitForm() {
      this.$axios.post('/add_product', this.product)
        .then(response => {
          alert('Produkt został dodany!');
          console.log(response.data);
        })
        .catch(error => {
          alert('Wystąpił błąd przy dodawaniu produktu.');
          console.error(error);
        });
    }
  }
};
</script>

<style>
/* Style dla formularza */

.form-container {
  display: flex;
  flex-direction: column;
  align-items: center; /* Wyśrodkowanie na osi X */
  justify-content: center; /* Wyśrodkowanie na osi Y */
  height: 50vh; /* Ustawienie wysokości na całą widoczność okna przeglądarki */
  background-color: #f3e0dc; /* Jasny, ciepły kolor tła */
  text-align: right;
}

.form-title {
  font-size: 24px;
  color: #5a2a27; /* Ciasteczkowy brąz */
  margin-bottom: 20px;
}

.add-product-form {
  background-color: #ffeaf5; /* Jasny róż */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}

.form-field {
  margin-bottom: 10px;
}

.form-label {
  font-size: 18px;
  color: #5a2a27; /* Ciasteczkowy brąz */
  margin-right: 5px;
}

.form-input {
  font-size: 16px;
  color: #5a2a27; /* Ciasteczkowy brąz */
  background-color: #fff;
  border: 2px solid #d98695; /* Delikatny róż */
  border-radius: 5px;
  padding: 5px 10px;
}

.form-button {
  font-size: 18px;
  background-color: #d98695; /* Delikatny róż */
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  transition: background-color 0.3s;
}

.form-button:hover {
  background-color: #f3a7b0; /* Ciemniejszy róż */
}
</style>
