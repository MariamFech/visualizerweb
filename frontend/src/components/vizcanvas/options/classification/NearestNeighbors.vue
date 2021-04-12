<template>
  <div>
    <div class="q-pa-md">
      <span class="text-blue-grey-14">
        Neighbors: {{ neighbors }}
      </span>
      <q-slider
        v-model="neighbors"
        :min="1"
        :max="20"
        :step="1"
        @update:modelValue="emitMlAlgoData()"
        label
        color="blue-grey-14"
      />
    </div>

  </div>
</template>

<script>
import { computed, ref } from 'vue'

export default {
  name: 'NearestNeighbors',
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
    let neighbors = ref(props.dflf.mlAlgoOptions.Neighbors)
    if (mlAlgoName.value === 'Nearest Neighbors') {
      neighbors = ref(mlAlgoOptions.value.Neighbors)
    }

    function emit () {
      this.$emit('mlAlgoData', {
        mlAlgoName: 'Nearest Neighbors',
        mlAlgoOptions: {
          Neighbors: this.neighbors
        }
      })
    }

    return {
      neighbors,
      emit
    }
  }
}
</script>

<style scoped>

</style>
