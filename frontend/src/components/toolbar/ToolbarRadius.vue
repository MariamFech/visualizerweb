<template>
  <q-btn-toggle id="toolbarradius"
                v-model="pointRadius"
                v-on:click="setPointRadius"
                color="primary"
                toggle-color="grey-4"
                padding="xs"
                unelevated
                no-caps
                :options="[
                  {value: '3', slot: 'one'},
                  {value: '5', slot: 'two'},
                  {value: '7', slot: 'three'},
                  {value: '9', slot: 'four'}
                ]"
  >
    <template v-slot:one>
      <q-icon color="blue-grey-14">
        <svg xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="4"/>
        </svg>

      </q-icon>
    </template>
    <template v-slot:two>
      <q-icon color="blue-grey-14">
        <svg xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="6"/>
        </svg>
      </q-icon>

    </template>
    <template v-slot:three>
      <q-icon color="blue-grey-14" size="sm">
        <svg xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="8"/>
        </svg>
      </q-icon>

    </template>
    <template v-slot:four>
      <q-icon color="blue-grey-14">
        <svg xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10"/>
        </svg>
      </q-icon>
    </template>
  </q-btn-toggle>

</template>

<script>

export default {
  created () {
    // Svg Icon
  },
  data () {
    return {
      pointRadius: '5'
    }
  },
  methods: {
    setPointRadius () {
      this.$store.commit('toolbar/setPointRadius', this.pointRadius)
    }
  }
}
</script>

<style scoped>

</style>
