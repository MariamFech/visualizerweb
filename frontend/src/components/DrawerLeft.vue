<template>
  <div class="q-pa-md flex flex-center " >
    <div class="q-pa-sm full-width text-center">
      <span class="text-h6 text-weight-bold text-blue-grey ">VisualizerWeb</span>
      <span class="text-caption text-blue-grey "> 0.0.1</span>
      <q-separator />
    </div>
    <div class="q-pb-md full-width text-center">

        <q-btn
          flat
          class="q-ma-sm full-width text-blue-grey"
          color="blue-gray"
          label="Save"
          :icon="iconSave"
          @click="fileExport"
        />
        <q-btn
          flat
          class="q-ma-sm full-width text-blue-grey"
          color="blue-gray"
          label="Load"
          :icon="iconLoad"
          @click="prompt = true"
        />

      <q-separator />
    </div>
    <div class="q-pa-md p-ma-xs full-width text-center ">
      <div class="p-pa-md">
        <span class="text-subtitle2 text-blue-grey"> View:</span>
      </div>
      <Split class="q-pa-md"></Split>
      <q-separator />
    </div>
    <q-card
      flat
      bordered
      class="my-card">
      <q-card-section>
        <p>
          VisualizerWeb was developed as part of a bachelor thesis at the HTW-Berlin.
        </p>
        <p>
          Created by Stefan Draeger based on "Visualizer in Machine Learning".
        </p>
        <p>
          Get the code on <a href="https://github.com/stdrg/visualizerweb">Github</a>.
        </p>
      </q-card-section>
    </q-card>
  </div>
  <q-dialog v-model="prompt" persistent>
    <q-card style="min-width: 350px">
      <q-card-section class="q-pa-md">
        <q-file
          v-model="importedFile"
          label="Import"
          label-color="blue-gray"
          color="grey-blue"
          clearable
          flat
        />
      </q-card-section>
      <q-card-actions align="right" class="text-primary">
        <q-btn flat color="negative" label="Cancel" v-close-popup />
        <q-btn flat color="positive" label="Import" @click="fileImport" v-close-popup />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import Split from './drawer/Split'
import { useStore } from 'vuex'
import { ref } from 'vue'
import { exportFile } from 'quasar'
import { laSaveSolid, laFileUploadSolid } from '@quasar/extras/line-awesome'
export default {
  name: 'DrawerLeft',
  components: { Split },
  created () {
    this.iconSave = laSaveSolid
    this.iconLoad = laFileUploadSolid
  },
  setup () {
    const $store = useStore()
    const vizcanvasState = $store.state.vizcanvas
    const leftDrawerState = $store.state.leftDrawer
    const importedFile = ref(null)

    function fileExport () {
      const exportData = {
        view: leftDrawerState.view,
        points: vizcanvasState.points
      }
      exportFile('VisualizerWeb_export.json', JSON.stringify(exportData))
    }
    function fileImport () {
      const x = importedFile.value.text()

      x.then(text => $store.commit('vizcanvas/setPoints', JSON.parse(text).points))
      $store.dispatch('toolbar/undo')
    }

    return {
      fileExport,
      fileImport,
      importedFile,
      prompt: ref(false)
    }
  }
}
</script>

<style scoped>

</style>
