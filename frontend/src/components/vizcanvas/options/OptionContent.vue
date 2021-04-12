<template>
  <div class="q-pa-none" style="width: 500px">

    <q-tabs
      v-model="tabs.mainTab"
      class="text-blue-grey-3 text-weight-bold"
      active-color="blue-grey"
      indicator-color="primary"
      align="justify"

    >
      <q-tab name="clustering" label="Clustering"/>
      <q-tab name="classification" label="Classification"/>
    </q-tabs>

    <q-separator/>

    <q-tab-panels v-model="tabs.mainTab" animated >
      <q-tab-panel name="clustering" class="q-pa-none">

        <q-splitter
          v-model="splitterModel"
          style="height: 250px"
        >
          <template v-slot:before>
            <q-tabs
              v-model="tabs.clusteringTab"
              vertical
              no-caps
              class="text-blue-grey-4"
              active-color="blue-grey"
            >
              <q-tab name="kmeans" label="K-Means"/>
              <q-tab name="hierarchical" label="Hierarchical"/>
            </q-tabs>
          </template>

          <template v-slot:after>
            <q-tab-panels
              v-model="tabs.clusteringTab"
              animated
              transition-prev="slide-down"
              transition-next="slide-up"
            >
              <q-tab-panel name="kmeans">
                <KMeans @mlAlgoData="mlAlgoData"
                        :currentAlgoData="currentAlgoData"
                        :dflf="dflf.kMeans()"
                ></KMeans>
              </q-tab-panel>

              <q-tab-panel name="hierarchical">
                <Hierarchical  @mlAlgoData="mlAlgoData"
                               :currentAlgoData="currentAlgoData"
                               :dflf="dflf.hierarchical()"
                ></Hierarchical>
              </q-tab-panel>
            </q-tab-panels>
          </template>
        </q-splitter>
      </q-tab-panel>

      <q-tab-panel name="classification" class="q-pa-none">

        <q-splitter
          v-model="splitterModel"
          style="height: 250px"
        >

          <template v-slot:before>
            <q-tabs
              v-model="tabs.classificationTab"
              vertical
              no-caps
              class="text-blue-grey-4"
              active-color="blue-grey"
            >
              <q-tab name="svm" label="SVM"/>
              <q-tab name="nearest" label="Nearest Neighbor"/>
              <q-tab name="decision" label="Decision Tree"/>
            </q-tabs>
          </template>

          <template v-slot:after>
            <q-tab-panels
              v-model="tabs.classificationTab"
              animated
              transition-prev="slide-down"
              transition-next="slide-up"
            >
              <q-tab-panel name="svm">
                <Svm
                  @mlAlgoData="mlAlgoData"
                  :currentAlgoData="currentAlgoData"
                  :dflf="dflf.suvm()"
                ></Svm>
              </q-tab-panel>

              <q-tab-panel name="nearest">
                <NearestNeighbors
                  @mlAlgoData="mlAlgoData"
                  :currentAlgoData="currentAlgoData"
                  :dflf="dflf.nearestNeighbors()"
                ></NearestNeighbors>
              </q-tab-panel>
              <q-tab-panel name="decision">
                <DecisionTree
                  @mlAlgoData="mlAlgoData"
                  :currentAlgoData="currentAlgoData"
                  :dflf="dflf.decisionTree()"
                ></DecisionTree>
              </q-tab-panel>
            </q-tab-panels>
          </template>
        </q-splitter>
      </q-tab-panel>
    </q-tab-panels>
    <q-separator/>
    <div class="q-pa-sm float-right">
      <q-btn color="negative"
             outline label="Cancel"
             style="width: 100px; margin-left: 10px"
             v-close-popup />
      <q-btn color="positive"
             outline label="Ok"
             style="width: 100px; margin-left: 10px"
             v-close-popup
             @click="emitData()"/>
    </div>
  </div>

</template>

<script>
import KMeans from './clustering/K-Means'
import Hierarchical from './clustering/Hierarchical'
import NearestNeighbors from './classification/NearestNeighbors'
import Svm from './classification/Svm'
import DecisionTree from './classification/DecisionTree'
import * as dflf from './default/MlAlgoDefaults'
import { ref } from 'vue'

export default {
  name: 'OptionContent',
  components: {
    KMeans,
    Hierarchical,
    NearestNeighbors,
    Svm,
    DecisionTree
  },
  props: ['currentTabs', 'currentAlgoData'],
  methods: {
    mlAlgoData (data) {
      this.mla = data
    },
    emitData () {
      let mad = this.mla

      if (!this.mla) {
        if (this.tabs.mainTab === 'clustering') {
          if (this.tabs.clusteringTab === 'kmeans') {
            mad = this.dflf.kMeans()
          } else if (this.tabs.clusteringTab === 'hierarchical') {
            mad = this.dflf.hierarchical()
          }
        } else if (this.tabs.mainTab === 'classification') {
          if (this.tabs.classificationTab === 'svm') {
            mad = this.dflf.suvm()
          } else if (this.tabs.classificationTab === 'nearest') {
            mad = this.dflf.nearestNeighbors()
          } else if (this.tabs.classificationTab === 'decision') {
            mad = this.dflf.decisionTree()
          }
        }
      }
      this.$emit('mlAlgoData', mad)

      this.$emit('lastTab', {
        mainTab: this.tabs.mainTab,
        clusteringTab: this.tabs.clusteringTab,
        classificationTab: this.tabs.classificationTab
      })
    }
  },
  emits: ['mlAlgoData', 'lastTab'],
  setup (props) {
    const mla = ref(null)
    const tabs = ref({
      mainTab: props.currentTabs.mainTab,
      clusteringTab: props.currentTabs.clusteringTab,
      classificationTab: props.currentTabs.classificationTab
    })

    return {
      tabs,
      dflf,
      mla,
      splitterModel: ref(35)

    }
  }
}

</script>

<style scoped>

</style>
