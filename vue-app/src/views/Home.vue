<template>
  <div>
    <navbar />
    <page-header />
    <section class="tweets-section">
      <h1>30 Most Recent Tweets</h1>
      <div class="tweet-div" :key="item.key" v-for="(item, index) in tweetarray">
        {{index}} {{item[Object.keys(item)[0]].tweetcontents}}
        <Tweet
          class="tweets"
          error-message
          :id="item[Object.keys(item)[0]].tweetid"
          :options="{ align: 'center', theme: 'dark' }"
        >
          <div class="spinner" />
        </Tweet>
      </div>
    </section>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import PageHeader from "@/components/PageHeader.vue";
import { Tweet } from "vue-tweet-embed";
import Footer from "@/components/Footer.vue";

export default {
  name: "home",
  components: {
    Navbar,
    PageHeader,
    Tweet,
    Footer
  },
  data() {
    return {
      tweetarray: []
    };
  },
  mounted() {
    const db = this.$firebase.firestore();
    db.collection("tweetarray")
      .orderBy("createdAt")
      .limit(10)
      .onSnapshot(snap => {
        snap.docChanges().forEach(change => {
          if (change.type === "added") {
            const data = {
              [change.doc.id]: change.doc.data()
            };
            this.tweetarray.unshift(data);
          }
        });
      });
  }
};
</script>

<style lang="scss">
@import "@/assets/styles.scss";
.tweets-section {
  text-align: center;
  padding-bottom: 2rem;
  h1 {
    font-size: 2rem;
    padding-top: 1.5rem;
    padding-bottom: 1rem;
    color: black;
  }
  .tweet-div {
    padding-bottom: 0.4rem;
  }
}
@media screen and (max-width: 769px) {
  .tweets {
    width: 100%;
  }
}
</style>