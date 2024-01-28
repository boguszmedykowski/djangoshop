<template>
    
  <div id="app">
    <CandyNavBar />
    <div class="background">
      <router-view /> <!-- Tutaj będą renderowane komponenty na podstawie routingu -->

    </div>
    </div>

</template>

<script>
import CandyNavBar from './components/CandyNavBar.vue';
import '@/assets/css/style.css'


export default {
  name: 'App',
  components: {
    CandyNavBar
  }
}
</script>

<style>
.background {
  background-color: #ffbfbe; /* Kolor tła w stylu cukierkowym */
  padding: 10px; /* Wewnętrzny padding dla nawigacji */
  border-radius: 0 0 20px 20px;
}

</style>
