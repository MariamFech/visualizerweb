<template>
  <q-page class="row">
    <VizCanvas title="One" class="col" @pointToPaint="emittedPointToPaint" :pointToPaint="pointToPaint"></VizCanvas>
  </q-page>
</template>

<script>
import { ref } from 'vue'
import VizCanvas from 'components/VizCanvas'
import { useStore } from 'vuex'
export default {
  name: 'Index',
  components: { VizCanvas },
  props: ['propsPointToPaint'],
  methods: {
    emittedPointToPaint (data) {
      this.pointToPaint = data
    }
  },
  setup () {
    const pointToPaint = ref({})
    useStore().commit('leftDrawer/currentView', 'one')
    useStore().dispatch('toolbar/clearCanvas')
    return {
      pointToPaint
    }
  }
}
</script>
