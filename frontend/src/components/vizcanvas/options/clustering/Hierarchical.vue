<template>
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
        Linkage:
      </span>
      <q-option-group
        v-model="linkage"
        :options="linkageOptions"
        inline
        @update:modelValue="emitMlAlgoData()"
        color="blue-grey-14"
      />

    </div>
</template>

<script>
import { computed, ref } from 'vue'

export default {
  name: 'Hierarchical',
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
    let linkage = ref(props.dflf.mlAlgoOptions.Linkage)
    if (mlAlgoName.value === 'Hierarchical') {
      cluster = ref(mlAlgoOptions.value.Cluster)
      linkage = ref(mlAlgoOptions.value.Linkage)
    }

    function emit () {
      this.$emit('mlAlgoData', {
        mlAlgoName: 'Hierarchical',
        mlAlgoOptions: {
          Cluster: this.cluster,
          Linkage: this.linkage
        }
      })
    }
    return {
      linkage,
      cluster,
      emit,
      linkageOptions: [
        {
          label: 'Ward',
          value: 'ward'
        },
        {
          label: 'Complete',
          value: 'complete'
        },
        {
          label: 'Average',
          value: 'average'
        },
        {
          label: 'Single',
          value: 'single'
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
