<template>
    <div class="product-grid">
        <div v-for="product in products" :key="product.id" class="product-container">
            <h2 class="product-name">{{ product.name }}</h2>
            <p class="product-price">Cena: {{ product.price }} zł</p>
            <div class="form-field">
                <label for="quantity" class="quantity-label">Ilość:</label>
                <input type="number" :id="'quantity-' + product.id" min="1" v-model="product.quantity" class="quantity-input">
            </div>
            <button @click="addToCart(product)" class="add-to-cart-button">Dodaj do Koszyka</button>
        </div>
    </div>
</template>
  
<script>
export default {
    name: 'ProductList',
    data() {
        return {
            products: []
        };
    },
    created() {
        this.fetchProducts();
    },
    methods: {
        fetchProducts() {
            this.$axios.get('/products/')
                .then(response => {
                    // Przekształcanie odpowiedzi, aby zawierała tylko produkty z klucza 'results'
                    this.products = response.data.results.map(product => ({ ...product, quantity: 1 }));
                })
                .catch(error => {
                    console.error('Błąd przy pobieraniu produktów:', error);
                    if (error.response) {
                        // Odpowiedź serwera była poza zakresem kodu statusu 2xx
                        console.log(error.response.data);
                        console.log(error.response.status);
                        console.log(error.response.headers);
                    } else if (error.request) {
                        // Żądanie zostało wysłane, ale nie otrzymano odpowiedzi
                        console.log(error.request);
                    } else {
                        // Coś innego spowodowało błąd żądania
                        console.log('Error', error.message);
                    }
                });
        }
    }
};
</script>
  
<style>
/* Style dla ProductList */

.product-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.product-container {
    background-color: #f3e0dc; /* Jasny, ciepły kolor tła */
    padding: 20px;
    margin: 10px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}

.product-name {
    font-size: 24px;
    font-weight: bold;
    color: #5a2a27; /* Ciasteczkowy brąz */
}

.product-price {
    font-size: 18px;
    color: #d98695; /* Delikatny róż */
    padding: 5px;
}

.form-field {
    margin-top: 10px;
}

.quantity-label {
    font-size: 16px;
    color: #5a2a27; /* Ciasteczkowy brąz */
    margin-right: 5px;
}

.quantity-input {
    font-size: 16px;
    width: 20%;
    color: #5a2a27; /* Ciasteczkowy brąz */
    background-color: #ffeaf5; /* Jasny róż */
    border: 2px solid #5a2a27; /* Ciasteczkowy brąz */
    border-radius: 5px;
    padding: 5px 10px;
}

.add-to-cart-button {
    font-size: 18px;
    background-color: #d98695; /* Delikatny róż */
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 10px;
}

.add-to-cart-button:hover {
    background-color: #f3a7b0; /* Ciemniejszy róż */
}
</style>

