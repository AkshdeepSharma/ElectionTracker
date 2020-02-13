<template>
  <nav class="navbar is-spaced" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <img id="navbar-img" src="@/assets/logo.png">
      </router-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: "navbar"
};
</script>

<style lang="scss">
@import "@/assets/styles.scss";
@media screen and (max-width: 769px) {
  .navbar-brand {
    margin-left: -50px;
  }
  .navbar-end {
    margin-right: -50px;
  }
}
</style>