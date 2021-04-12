<template>
  <div class="row justify-start">
    <q-separator vertical inset spaced="sm"/>
    <div class="col-auto">
      <ToolbarUndo></ToolbarUndo>
    </div>
    <q-separator vertical inset spaced="sm"/>
    <div class="col-auto">
      <ToolbarColor></ToolbarColor>
    </div>
    <q-separator vertical inset spaced="sm"/>
    <div class="col-auto">
      <ToolbarRadius></ToolbarRadius>
    </div>
    <q-separator vertical inset spaced="sm"/>
    <div class="col-auto">
      <ToolbarContour></ToolbarContour>
    </div>
    <q-separator vertical inset spaced="sm"/>
    <div class="col-auto">
      <ToolbarDispersion></ToolbarDispersion>
    </div>
    <q-separator vertical inset spaced="sm"/>
    <div class="col-auto">
      <ToolbarDensity></ToolbarDensity>
    </div>
    <q-separator vertical inset spaced="sm"/>
    <div class="col-auto">
      <ToolbarClear></ToolbarClear>
    </div>
  </div>
</template>

<script>
import ToolbarColor from 'components/toolbar/ToolbarColor'
import ToolbarContour from 'components/toolbar/ToolbarContour'
import ToolbarRadius from 'components/toolbar/ToolbarRadius'
import ToolbarDispersion from 'components/toolbar/ToolbarDispersion'
import ToolbarDensity from 'components/toolbar/ToolbarDensity'
import ToolbarClear from 'components/toolbar/ToolbarClear'
import ToolbarUndo from 'components/toolbar/ToolbarUndo'

export default {
  name: 'Toolbar',
  components: {
    ToolbarColor,
    ToolbarContour,
    ToolbarRadius,
    ToolbarDispersion,
    ToolbarDensity,
    ToolbarClear,
    ToolbarUndo
  }

}
</script>

<style scoped>

</style>
