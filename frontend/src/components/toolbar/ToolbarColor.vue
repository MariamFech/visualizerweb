<template>

    <q-btn-toggle id="toolbarcolor"
                  v-model="pointColor"
                  v-on:click="setPointColor"
                  color="primary"
                  toggle-color="grey-4"
                  padding="xs"
                  unelevated
                  no-caps
                  :options="[
          {value: 'black', slot: 'black'},
          {value: '#4EB265', slot: 'green'},
          {value: '#DC050C', slot: 'red'},
          {value: '#FABE00', slot: 'yellow'},
          {value: '#1965B0', slot: 'blue'}
        ]"
    >
      <template v-slot:black>
        <q-icon :name="evaDroplet" color="black" stroke="grey" stroke-width=".5"/>
      </template>
      <template v-slot:green>
        <q-icon :name="evaDroplet" color="green" stroke="grey" stroke-width=".5"/>
      </template>
      <template v-slot:red>
        <q-icon :name="evaDroplet" color="red" stroke="grey" stroke-width=".5"/>
      </template>
      <template v-slot:yellow>
        <q-icon :name="evaDroplet" color="yellow-14" stroke="grey" stroke-width=".5"/>
      </template>
      <template v-slot:blue>
        <q-icon :name="evaDroplet" color="blue" stroke="grey" stroke-width=".5"/>
      </template>
    </q-btn-toggle>

</template>
<script>
import { laPaintBrushSolid } from '@quasar/extras/line-awesome'
import { evaDroplet } from '@quasar/extras/eva-icons'
import { ref } from 'vue'

export default {
  created () {
    // Svg Icon
    this.evaDroplet = evaDroplet
    this.laPaintBrushSolid = laPaintBrushSolid
  },
  methods: {
    setPointColor () {
      this.$store.commit('toolbar/setPointColor', this.pointColor)
    }
  },
  setup () {
    return {
      pointColor: ref('black')

    }
  }
}
</script>

<style scoped>

</style>
