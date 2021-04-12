<template>
  <div>
    <div class="q-pa-md">
      <span class="text-blue-grey-14">
        Kernel:
      </span>
      <div class="text-center">
        <q-option-group
          v-model="kernel"
          :options="options"
          inline
          @update:modelValue="emitMlAlgoData()"
          color="blue-grey-14"
        />
      </div>
      <span class="text-blue-grey-14">
        <br>
        C: {{ paramC }}
      </span>
      <q-slider
        v-model="paramC"
        :min="1"
        :max="50"
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
  name: 'Svm',
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
    let paramC = ref(props.dflf.mlAlgoOptions.C)
    let kernel = ref(props.dflf.mlAlgoOptions.Kernel)

    if (mlAlgoName.value === 'SVM') {
      paramC = ref(mlAlgoOptions.value.C)
      kernel = ref(mlAlgoOptions.value.Kernel)
    }

    function emit () {
      this.$emit('mlAlgoData', {
        mlAlgoName: 'SVM',
        mlAlgoOptions: {
          C: this.paramC,
          Kernel: this.kernel
        }
      })
    }

    return {
      kernel,
      paramC,
      emit,
      options: [
        {
          label: 'rbf',
          value: 'rbf'
        },
        {
          label: 'linear',
          value: 'linear'
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
