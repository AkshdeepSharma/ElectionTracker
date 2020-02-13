<template>
  <footer class="section is-small">
    <div class="container">
      <p
        id="tnc"
      >This webapp has no affiliation to the Canadian Government or any political parties, news outlets, or otherwise. If you have any questions, concerns or suggestions, please contact me through one of the mediums below.</p>
    </div>
    <div class="row buttons are-medium is-centered">
      <a href="https://github.com/AkshdeepSharma" target="_blank" class="button" id="sm-icons">
        <i class="fab fa-github" />
      </a>
      <a
        href="https://linkedin.com/in/akshdeep-sharma"
        target="_blank"
        class="button"
        id="sm-icons"
      >
        <i class="fab fa-linkedin-in" />
      </a>
      <a href="mailto:akshdeep.sharma1@gmail.com" class="button" id="sm-icons">
        <i class="far fa-envelope" />
      </a>
      <a href="https://medium.com/@akshdeep.sharma1" target="_blank" class="button" id="sm-icons">
        <i class="fab fa-medium-m" />
      </a>
    </div>
  </footer>
</template> 

<style lang="scss">
@import "@/assets/styles.scss";
footer {
  background-color: $primary;
  color: white;
}
#sm-icons {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
  border-radius: 100%;
  height: 48px;
  width: 48px;
  border: 2px solid white 0.9;
  color: white;
  background-color: $primary;
}
#sm-icons:hover {
  color: $primary;
  opacity: 1;
  background-color: white;
  border: 2px solid white 1;
}
#tnc {
  text-align: center;
  padding-top: 0.5rem;
  padding-bottom: 1.5rem;
}
@media screen and (max-width: 769px) {
  footer {
    margin-top: 20px;
    height: 20rem;
  }
}
</style>