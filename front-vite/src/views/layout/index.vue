<script setup>
import Layout from "@/views/layout/components/Layout.vue";
import Footer from "@/views/layout/components/Footer.vue";
import BackToTop from "@/views/layout/components/BackToTop.vue";
import Header from "@/views/layout/components/Header.vue";
import Main from "./components/Main.vue";
</script>

<template>
  <Layout>
    <Header />
    <Main />
    <BackToTop />
    <Footer />
  </Layout>
</template>
