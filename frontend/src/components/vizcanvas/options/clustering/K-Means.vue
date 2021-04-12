<template>
  <div>
    <div class="q-pa-md">
      <span class="text-blue-grey-14">
        Cluster: {{ cluster }}
      </span>
      <q-slider
        v-model="cluster"
        :min="1"
        :max="20"
        :step="1"
        label
        @change="emitMlAlgoData()"
        color="blue-grey-14"
      />
      <span class="text-blue-grey-14">
        Iterations : {{ iterations }}
      </span>
      <q-slider
        v-model="iterations"
        :min="20"
        :max="300"
        :step="20"
        label
        @change="emitMlAlgoData()"
        color="blue-grey-14"
      />
      <span class="text-blue-grey-14">
        Centroid Seeds : {{ centroidSeeds }}
      </span>
      <q-slider
        v-model="centroidSeeds"
        :min="1"
        :max="30"
        :step="1"
        label
        @change="emitMlAlgoData()"
        color="blue-grey-14"
      />
    </div>

  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'K-Means',
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
    let cluster = ref(props.dflf.mlAlgoOptions.Cluster)
    let iterations = ref(props.dflf.mlAlgoOptions.Iterations)
    let centroidSeeds = ref(props.dflf.mlAlgoOptions['Centroid Seeds'])
    if (mlAlgoName.value === 'K-Means') {
      cluster = ref(mlAlgoOptions.value.Cluster)
      iterations = ref(mlAlgoOptions.value.Iterations)
      centroidSeeds = ref(mlAlgoOptions.value['Centroid Seeds'])
    }

    function emit () {
      this.$emit('mlAlgoData', {
        mlAlgoName: 'K-Means',
        mlAlgoOptions: {
          Cluster: this.cluster,
          Iterations: this.iterations,
          'Centroid Seeds': this.centroidSeeds
        }
      })
    }
    return {
      cluster,
      iterations,
      centroidSeeds,
      emit
    }
  }
}
</script>

<style scoped>

</style>
