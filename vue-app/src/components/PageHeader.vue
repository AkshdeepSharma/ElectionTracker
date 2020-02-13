<template>
  <section class="hero is-fullheight-with-navbar">
    <div class="hero-body">
      <div id="ph" class="container">
        <h1>Canadian Federal Election Tweet Hub</h1>
        <h2>A place where you can see Tweets from all running candidates and their parties.</h2>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "page-header"
};
</script>

<style lang="scss">
@import "@/assets/styles.scss";
.hero {
  background-color: $primary;
}
#ph {
  text-align: center;
  color: white;
  margin-top: -10rem;
  h1 {
    padding-top: 0rem;
    font-size: 3.5rem;
  }
  h2 {
    font-size: 1.5rem;
  }
}
@media screen and (max-width: 769px) {
  #ph {
    h1 {
      font-size: 3rem;
      line-height: 120%;
      margin-bottom: 3rem;
    }
    h2 {
      font-size: 1.2rem;
    }
  }
}
</style>