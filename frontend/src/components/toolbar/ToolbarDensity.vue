<template>
    <q-btn-dropdown color="blue-grey-14"
                    :label=" `${'Density: ' + (x = densityValue <= 9 ? '&nbsp ' + densityValue :  densityValue) }`"
                    padding="xs sm"
                    style="width: 9em"
                    unelevated
                    outline
    >
        <q-item clickable v-close-popup >
          <q-item-section>
            <q-slider class="col-grow"
                      v-model="densityValue"
                      @change="setDensityValue"
                      :min="1"
                      :max="20"
                      :step="1"
                      snap
                      color="blue-grey-14"
            />
          </q-item-section>
        </q-item>
    </q-btn-dropdown>
</template>

<script>

export default {
  created () {

  },
  data () {
    return {
      densityValue: 4
    }
  },
  methods: {
    setDensityValue () {
      this.$store.commit('toolbar/setDensityValue', (this.densityValue * 5))
    }
  }
}
</script>

<style scoped>

</style>
