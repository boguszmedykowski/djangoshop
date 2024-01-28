<template>
  <div class="candy-cart">
    <h1 class="cart-title">Koszyk</h1>
    <div v-if="cartItems.length">
      <div v-for="item in cartItems" :key="item.id" class="cart-item-container">
        <p class="cart-item-text">{{ item.name }} - {{ item.quantity }} x {{ item.price }} zł</p>
      </div>
    </div>
    <p v-else class="cart-empty">Koszyk jest pusty</p>
  </div>
</template>

<script>

export default {
name: 'CandyCart',
data() {
  return {
    cartItems: []
  };
},
created() {
  this.fetchCartItems();
},
methods: {
  fetchCartItems() {
    this.$axios.get('/cart')
      .then(response => {
        this.cartItems = response.data;
      })
      .catch(error => {
        console.error('Błąd przy pobieraniu zawartości koszyka:', error);
      });
  }
}
};
</script>

<style>
/* Style dla komponentu koszyka */

.candy-cart {
  padding: 20px;
  text-align: center; /* Wyśrodkowanie zawartości na środku */
  width: 50%;
  display: flex; /* Włączamy flexbox */
  flex-direction: column; /* Ustawiamy kierunek flexbox na kolumnowy */
  justify-content: center; /* Wyśrodkowanie na osi Y */
  align-items: center; /* Wyśrodkowanie na osi X */
  margin: 0 auto; /* Wyśrodkowanie w poziomie */
}

.cart-title {
font-size: 24px;
color: #ff1493;
margin-bottom: 20px;
}

.cart-item-container {
background-color: #fff;
border: 2px solid #ff1493;
border-radius: 5px;
margin: 10px 0;
padding: 10px;
display: flex;
justify-content: space-between;
}

.cart-item-text {
font-size: 16px;
color: #ff1493;
}

.cart-empty {
font-size: 18px;
color: #ff1493;
margin-top: 20px;
}
</style>
