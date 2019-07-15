<template>
  <div class="about">
    <h1>hola {{value}}</h1>
  </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
  name: 'about',
  computed: {
    ...mapState(['value']),
    este_valor() {
      return this.value
    }
  }
}
</script>