<template>
  <div>
    <div class="q-pa-md">
      <span class="text-blue-grey-14">
        Polynom Degree: {{ degree }}
      </span>
      <q-slider v-model="degree" :min="1" :max="15" :step="1" @update:modelValue="emitMlAlgoData()" label
        color="blue-grey-14" />
    </div>

  </div>
</template>

<script>
import { computed, ref } from 'vue'

export default {
  name: 'LinearRegression',
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
    let degree = ref(props.dflf.mlAlgoOptions.Degree)
    if (mlAlgoName.value === 'Linear Regression') {
      degree = ref(mlAlgoOptions.value.Degree)
    }

    function emit () {
      this.$emit('mlAlgoData', {
        mlAlgoName: 'Linear Regression',
        mlAlgoOptions: {
          Degree: this.degree
        }
      })
    }

    return {
      degree,
      emit
    }
  }
}
</script>

<style scoped></style>
