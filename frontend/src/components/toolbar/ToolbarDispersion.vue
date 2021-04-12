<template>
  <q-btn-dropdown color="blue-grey-14"
                  :label=" `${'Dispersion: ' + (x = dispersionValue <= 99 ? '&nbsp ' + dispersionValue :  dispersionValue) }`"
                  padding="xs sm"
                  style="width: 11em"
                  unelevated
                  outline
  >
    <q-item clickable v-close-popup>
      <q-item-section>
        <q-slider class="col-grow"
                  v-model="dispersionValue"
                  @change="setDispersionValue"
                  :min="0"
                  :max="160"
                  :step="20"
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
      dispersionValue: 20
    }
  },
  methods: {
    setDispersionValue () {
      this.$store.commit('toolbar/setDispersionValue', this.dispersionValue)
    }
  }
}
</script>

<style scoped>

</style>
