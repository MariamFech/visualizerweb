<template>
  <q-btn-toggle v-model="view"
                size="md"
                v-on:click="splitIt"
                toggle-color="grey-4"
                padding="sm"
                unelevated
                no-caps
                :options="[
          {value: 'one', slot: 'one'},
          {value: 'two', slot: 'two'},
          {value: 'four', slot: 'four'},
        ]"
  >
    <template v-slot:one>
      <q-icon :name="full" color="blue-grey-10"/>
    </template>
    <template v-slot:two>
      <q-icon :name="col" color="blue-grey-10"/>
    </template>
    <template v-slot:four>
      <q-icon :name="grid" color="blue-grey-10"/>
    </template>
  </q-btn-toggle>
</template>

<script>
import { tiLayoutWidthFull, tiLayoutColumn2, tiViewGrid } from '@quasar/extras/themify'
import { ref } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'Split',
  created () {
    // Svg Icon
    this.full = tiLayoutWidthFull
    this.col = tiLayoutColumn2
    this.grid = tiViewGrid
  },
  methods: {
    splitIt () {
      this.split()
    }
  },
  setup () {
    const $state = useStore()
    const view = ref($state.state.leftDrawer.view)
    function split () {
      $state.dispatch('toolbar/clearCanvas')
      if (view.value === 'one') {
        $state.commit('leftDrawer/currentView', 'one')
        window.location.href = '#/'
      }
      if (view.value === 'two') {
        $state.commit('leftDrawer/currentView', 'two')
        window.location.href = '#/t'
      }
      if (view.value === 'four') {
        $state.commit('leftDrawer/currentView', 'four')
        window.location.href = '#/f'
      }
    }

    return {
      view,
      split
    }
  }
}
</script>

<style scoped>

</style>
