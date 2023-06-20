<template>
  <body id="home-container">
    <LoginMenu></LoginMenu>
  </body>
</template>


<script setup> 

import LoginMenu from '@/components/LoginMenu.vue';

document.title = "SVision"


</script>

<style>

#home-container {
  width: 100%;
  height: 100%;
  background-image: url("../assets/img/background3.png");
  background-size: cover;
  background-position: center;
  position: relative;
  justify-content: center;
  align-items: center;
  display: flex;
}



</style>
