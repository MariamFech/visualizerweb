<template>
  <div>
    <div class="q-pa-md">
      <span class="text-blue-grey-14">
        Depth: {{ depth }}
      </span>
      <q-slider v-model="depth" :min="1" :max="15" :step="1" @change="emitMlAlgoData()" label color="blue-grey-14" />
    </div>

  </div>
</template>

<script>
import { computed, ref } from 'vue'

export default {
  name: 'RegressionTree',
  props: ['currentAlgoData', 'dflf'],
  methods: {
    emitMlAlgoData () {
      this.emit()
    }
  },
  emits: ['mlAlgoData'],
  setup (props) {
    const mlAlgoName = computed(() => props.currentAlgoData.mlAlgoName)
    const mlAlgoOptions = computed(() => props.currentAlgoData.mlAlgoOptions)
    let depth = ref(props.dflf.mlAlgoOptions.Depth)
    if (mlAlgoName.value === 'Regression Tree') {
      depth = ref(mlAlgoOptions.value.Depth)
    }

    function emit () {
      this.$emit('mlAlgoData', {
        mlAlgoName: 'Regression Tree',
        mlAlgoOptions: {
          Depth: this.depth
        }
      })
    }
    return {
      depth,
      emit
    }
  }
}
</script>

<style scoped></style>
