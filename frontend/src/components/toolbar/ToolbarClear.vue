<template>
  <q-btn
    flat
    color="blue-grey-14"
    :icon="laTrashSolid"
    @click="clearVizCanvas()"
    padding="xs"

  >
  </q-btn>
</template>

<script>
import { laTrashSolid } from '@quasar/extras/line-awesome'

export default {
  name: 'ToolbarClear',
  created () {
    // Svg Icon
    this.laTrashSolid = laTrashSolid
  },
  data () {
    return {

    }
  },
  methods: {
    clearVizCanvas () {
      this.$store.dispatch('toolbar/clearCanvas')
    }
  }
}
</script>

<style scoped>

</style>
