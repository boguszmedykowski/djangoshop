<template>
  <nav class="candy-navbar">
    <div class="navbar-content">
      <div class="navbar-brand">
        Candy-Shop
      </div>
      <div>
      </div>
    
      <div class="navbar-menu">
        <router-link to="/addProduct" class="navbar-item">Dodaj produkt</router-link>
        <router-link to="/ProductList" class="navbar-item">Lista produktów</router-link>
        <router-link to="/CandyCart" class="navbar-item">Koszyk</router-link>
        <router-link to="/UserLogin" class="navbar-item">Login</router-link>
        <router-link to="/UserRegister" class="navbar-item">Register</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'CandyNavBar',
};
</script>

<style>

.candy-navbar {
  background-color: #f3a7b0; /* jasnoróżowy kolor tła */
  padding: 10px; /* Wewnętrzny padding dla nawigacji */
  border-radius: 10px 10px 0 0;
}

.navbar-content {
  display: flex;
  justify-content: space-between; /* Wyśrodkowanie na osi X z odstępem między elementami */
  align-items: center; /* Wyśrodkowanie na osi Y */
}

.navbar-brand {
  font-size: 36px; /* Wielkość czcionki */
  font-weight: bold; /* Pogrubienie czcionki */
  color: #fff; /* Jasny kolor tekstu */
  font-family: 'Cookie', cursive; /* Stylowa czcionka */
}

.navbar-menu {
  display: flex;
  gap: 20px; /* Odstęp między elementami menu */
}

.navbar-item {
  font-size: 18px; /* Wielkość czcionki */
  color: #5a2a27; /* Ciasteczkowy brąz */
  text-decoration: none; /* Usunięcie podkreślenia linków */
  border: 2px solid #f3a7b0; /* Jasnoróżowa ramka */
  padding: 5px 10px; /* Wewnętrzny padding przycisku */
  border-radius: 10px; /* Zaokrąglenie rogów przycisku */
  transition: background-color 0.3s, color 0.3s; /* Animacja zmiany koloru tła i tekstu */
  background-color: #ffeaf5; /* Jasnoróżowe tło */
}

.navbar-item:hover {
  background-color: #f3a7b0; /* Różowe tło po najechaniu myszką */
  color: #fff; /* Jasny kolor tekstu po najechaniu myszką */
}

.navbar-item:active {
  background-color: #d98695; /* Ciemniejszy róż po wciśnięciu przycisku */
  color: #fff; /* Jasny kolor tekstu po wciśnięciu przycisku */
}

</style>

