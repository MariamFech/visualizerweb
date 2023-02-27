<template>
  <q-page-sticky position="top-left" :offset="[5, 5]">
    <q-btn text-color="blue-grey-15" class="q-card--bordered" style="background-color: rgba(236, 239, 241, 0.9) "
      size="md" unelevated square no-caps padding="xs sm" @click="prompt = true">
      <strong>{{ mlAlgoName }}:&nbsp;</strong>
      {{ mlAlgoOptions }}
    </q-btn>
  </q-page-sticky>
  <q-page-sticky position="top-right" :offset="[5, 5]">
    <div class="column items-center">
      <q-btn class="col" :loading="loading" @click="requestData" style="margin-bottom: 5px" v-model="run"
        :icon="laPlaySolid" square unelevated :disable="disableBtn" label-position="left" color="green" direction="right"
        padding="xs" />

      <q-btn
        :style="`${clickedButtons.voronoi ? 'background-color: rgba(244, 144, 55, 0.7) !important' : 'background-color: rgba(238, 219, 203, 0.7) !important'}`"
        v-model="voronoi" label="&nbsp;V&nbsp;" unelevated :outline="!clickedButtons.voronoi" :disable="disableVBtn"
        :color="`${disableVBtn ? 'primary' : 'yellow-10'}`" direction="right" padding="xs sm" @click="voronoiBtn" />
    </div>
    <q-dialog v-model="prompt">
      <q-card>
        <OptionContent @mlAlgoData="mlAlgoData" @lastTab="lastTab" :currentTabs="currentTabs"
          :currentAlgoData="currentAlgoData"></OptionContent>
      </q-card>
    </q-dialog>
  </q-page-sticky>
</template>

<script>
import { ref, watchEffect } from 'vue'
import { useStore } from 'vuex'
import OptionContent from './options/OptionContent'
import { laPlaySolid } from '@quasar/extras/line-awesome'
import axios from 'axios'

export default {
  name: 'OptionDropdownBtn',
  components: {
    OptionContent
  },
  created () {
    this.laPlaySolid = laPlaySolid
  },
  methods: {
    mlAlgoData (data) {
      this.mlAlgoName = data.mlAlgoName
      let str = ''
      Object.entries(data.mlAlgoOptions).forEach(el => {
        const key = el[0]
        const value = el[1]
        str = str.concat(key + ': ' + value + ' ')
      })
      this.mlAlgoOptions = str
      this.currentAlgoData = data
    },

    lastTab (data) {
      this.currentTabs = data
    },
    requestData () {
      this.request()
    },
    voronoiBtn () {
      this.clickedButtons.voronoi = !this.clickedButtons.voronoi
      this.$emit('buttonsState', this.clickedButtons)
    }
  },
  emits: ['responseData', 'buttonsState'],
  props: ['updateButtonsState'],
  setup (props) {
    const clickedButtons = ref({
      voronoi: false
    })
    const $store = useStore()
    const loading = ref(false)
    const currentTabs = {
      mainTab: 'clustering',
      clusteringTab: 'kmeans',
      classificationTab: 'svm',
      regressionTab: 'linear'
    }
    const progress = ref(false)
    const currentAlgoData = ref({})
    const disableBtn = ref(false)
    const disableVBtn = ref(false)
    const classification = ['Decision Tree', 'Nearest Neighbors', 'SVM']
    const regression = ['Regression Tree', 'Linear Regression']

    watchEffect(() => {
      if (Object.entries(currentAlgoData.value).length > 0) {
        const c = currentAlgoData.value.mlAlgoOptions.Cluster
        const algoName = currentAlgoData.value.mlAlgoName
        if (c !== undefined) {
          disableBtn.value = $store.state.vizcanvas.points.length < c
          disableVBtn.value = disableBtn.value
        } else if (checkMlAlgoName(algoName)) {
          disableBtn.value = !checkClasses()
          disableVBtn.value = disableBtn.value
        } else if (regressionAlg(algoName)) {
          disableVBtn.value = true
          if ($store.state.vizcanvas.points.length < 2) {
            disableBtn.value = true
          } else {
            disableBtn.value = false
          }
        }
      }
      if ($store.state.toolbar.clearCanvas) {
        clickedButtons.value.voronoi = false
      }
    })

    function regressionAlg (name) {
      let result = false
      regression.forEach(el => {
        if (el === name) {
          result = true
        }
      })
      return result
    }

    function checkMlAlgoName (name) {
      let yes = false
      classification.forEach(el => {
        if (el === name) {
          yes = true
        }
      })
      return yes
    }

    function checkClasses () {
      const points = $store.state.vizcanvas.points
      const colorArr = []
      points.forEach(el => {
        colorArr.push(el.strokeColor)
      })
      return colorArr.filter((v, i, a) => a.indexOf(v) === i).length >= 2
    }

    function request () {
      const postData = getPostData()
      const servUrl = process.env.BACKENDURL + '/compute'
      axios.post(servUrl, postData)
        .then(response => {
          if (response.data.error) {
            console.error(response.data.error)
          } else {
            this.$emit('responseData',
              mergePredictionDataInResponse(response.data, postData.predictionData))
          }
          loading.value = false
        })
        .catch(error => {
          console.error(error)
          loading.value = false
        })
    }

    function mergePredictionDataInResponse (response, predictionData) {
      let prediction

      if (response.prediction !== undefined) {
        prediction = {
          data: predictionData,
          predictionlabels: response.prediction
        }
      }
      return {
        specific: response.specific,
        labels: response.labels,
        prediction
      }
    }

    function getPostData () {
      loading.value = true
      const requestPoints = []
      $store.state.vizcanvas.points.forEach(el => {
        const id = el.id
        const x = el.x
        const y = el.y
        const strokeColor = el.strokeColor
        requestPoints.push({ id, x, y, strokeColor })
      })
      return {
        mlAlgoName: currentAlgoData.value.mlAlgoName,
        mlAlgoOptions: currentAlgoData.value.mlAlgoOptions,
        points: requestPoints,
        predictionData: getPredictionData()
      }
    }
    function getPredictionData () {
      const spacing = 10
      const width = document.getElementById('One').offsetWidth
      const height = document.getElementById('One').offsetHeight
      const coords = []
      for (let y = spacing; y < height - spacing; y += spacing) {
        for (let x = spacing; x < width - spacing; x += spacing) {
          coords.push({ x, y })
        }
      }
      return coords
    }

    return {
      mla: ref({}),
      mlAlgoName: ref('choose'),
      mlAlgoOptions: ref(''),
      run: ref(true),
      voronoi: ref(true),
      predict: ref(true),
      currentTabs,
      currentAlgoData,
      loading,
      progress,
      request,
      clickedButtons,
      prompt: ref(false),
      disableBtn,
      disableVBtn

    }
  }
}
</script>

<style scoped></style>
