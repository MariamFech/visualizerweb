<template>
  <q-btn
    flat
    padding="xs"
    color="blue-grey-10"
    :icon="laUndoSolid"
    @click="undo()"
  >
  </q-btn>
</template>

<script>
import { laUndoSolid } from '@quasar/extras/line-awesome'

export default {
  name: 'ToolbarUndo',
  created () {
    // Svg Icon
    this.laUndoSolid = laUndoSolid
  },
  data () {
    return {

    }
  },
  methods: {
    undo () {
      this.$store.dispatch('toolbar/undo')
    }
  }
}
</script>

<style scoped>

</style>
