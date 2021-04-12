<template>

  <q-btn-toggle id="toolbarcontour"
                v-model="pointContour"
                v-on:click="setPointContour"
                color="primary"
                toggle-color="grey-4"
                padding="xs"
                unelevated
                :options="[
                  {value: '1', slot: 'one'},
                  {value: '2', slot: 'two'},
                  {value: '3', slot: 'three'},
                  {value: '4', slot: 'four'}
                ]"
  >
    <template v-slot:one>
      <q-icon>
        <svg xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="8" fill="none" stroke-width="1" stroke="#455A64"/>
        </svg>
      </q-icon>
    </template>
    <template v-slot:two>
      <q-icon>
        <svg xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="8" fill="none" stroke-width="2" stroke="#455A64"/>
        </svg>
      </q-icon>
    </template>
    <template v-slot:three>
      <q-icon size="sm">
        <svg xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="8" fill="none" stroke-width="3" stroke="#455A64"/>
        </svg>
      </q-icon>
    </template>
    <template v-slot:four>
      <q-icon>
        <svg xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="8" fill="none" stroke-width="4" stroke="#455A64"/>
        </svg>
      </q-icon>
    </template>
  </q-btn-toggle>
</template>

<script>

import { ref } from 'vue'

export default {
  methods: {
    setPointContour () {
      this.$store.commit('toolbar/setPointContour', this.pointContour)
    }
  },
  setup () {
    return {
      pointContour: ref('2')
    }
  }
}
</script>

<style scoped>

</style>
