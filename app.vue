<script setup>
import { ref } from 'vue'

const msg = ref('5G手机评价分析 - 展示网站')
</script>

<template>
  <h1>{{ msg }}</h1>
  <input v-model="msg">
  <h2>{{ msg }}</h2>
</template>
