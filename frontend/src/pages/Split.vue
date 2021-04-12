<template>
  <q-page class="row">
    <VizCanvas title="One" class="col-6 q-card--bordered" @pointToPaint="emittedPointToPaint" :pointToPaint="pointToPaint"></VizCanvas>
    <VizCanvas title="Two" class="col-6 q-card--bordered" @pointToPaint="emittedPointToPaint" :pointToPaint="pointToPaint"></VizCanvas>
  </q-page>
</template>

<script>
import VizCanvas from 'components/VizCanvas'
import { useStore } from 'vuex'
import { ref } from 'vue'
export default {
  name: 'Split',
  components: { VizCanvas },
  props: ['propsPointToPaint'],
  methods: {
    emittedPointToPaint (data) {
      this.pointToPaint = data
    }
  },
  setup () {
    const pointToPaint = ref({})
    useStore().commit('leftDrawer/currentView', 'four')
    useStore().dispatch('toolbar/clearCanvas')
    return {
      pointToPaint
    }
  }
}
</script>
