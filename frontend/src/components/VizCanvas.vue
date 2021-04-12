<template>
  <div>
    <q-layout container view="hHh lpR fFf">
      <q-page-container>
        <q-page :id="title" class="flex flex-center">
          <Options @responseData="responseData" @buttonsState="buttonsState" :updateButtonsState="clickedButtons"></Options>
          <svg :id="svgId" class="bg-grey-3" :style="style"></svg>
        </q-page>
      </q-page-container>
      <q-resize-observer @resize="onResize"/>
    </q-layout>
  </div>
</template>

<script>
import { ref, onMounted, watchEffect } from 'vue'
import { useStore } from 'vuex'
import Options from 'components/vizcanvas/Options'
import * as d3 from 'd3'
import { getColors } from 'components/vizcanvas/helper/color'

export default {
  name: 'VizCanvas',
  components: {
    Options
  },
  props: ['title', 'pointToPaint'],
  emits: ['pointToPaint'],
  methods: {
    responseData (data) {
      this.response = data
    },
    buttonsState (data) {
      this.clickedButtons = data
    }
  },
  setup (props, context) {
    const $store = useStore()
    const colors = ref()

    const style = ref({
      width: '100px',
      height: '100px'
    })
    const svgId = 'vizcanvas' + props.title
    const report = ref({})
    // emitted data from the Options Component
    const response = ref(null)
    const clickedButtons = ref(null)
    /**
     * to use d3js we need the VueJs onMounted Lifecycle hook
     * @see https://v3.vuejs.org/api/composition-api.html#lifecycle-hooks
     */
    onMounted(() => {
      // get elements
      const canvas = document.getElementById(props.title)
      const vizCanvas = document.getElementById(svgId)
      const svg = d3.select(vizCanvas)
      // watchEffect for resize observer
      watchEffect(() => {
        style.value = {
          width: report.value.width,
          height: canvas.style.minHeight
        }
      })

      // vars
      let drag = false

      // get data from vuex store
      const toolbarState = $store.state.toolbar
      const vizcanvasState = $store.state.vizcanvas

      // layers for different types of presentation
      const voronoi = svg.append('g')
        .attr('class', 'voronoi')
        .attr('opacity', 0.6)

      const point = svg.append('g')
        .attr('class', 'points')

      // event listener for painting on the Point layer
      vizCanvas.addEventListener('mousedown', ev => { getData(ev) }, { passive: true })
      vizCanvas.addEventListener('mouseup', ev => getData(ev), { passive: true })
      vizCanvas.addEventListener('touchstart', ev => getData(ev), { passive: true })
      vizCanvas.addEventListener('touchend', ev => getData(ev), { passive: true })
      vizCanvas.addEventListener('mouseleave', () => { drag = false }, { passive: true })

      // Watch Vuex memory and props to react on changes.
      $store.watch((state) => { return toolbarState.clearCanvas }, (newValue) => {
        clearCanvas(newValue)
      })
      $store.watch((state) => { return vizcanvasState.points }, () => {
        if (toolbarState.undo) { redraw() }
      })
      $store.watch((state) => { return props.pointToPaint }, (newValue) => {
        draw(newValue)
      })

      let firstPoint = false
      let mcs = [] // mouse coord store
      const tmpPoints = []
      const tmpHistory = []

      /**
       * get mouse position and and save it
       * @param event
       */
      function getData (event) {
        const density = toolbarState.densityValue
        if (event.type === 'mousedown' || event.type === 'touchstart') {
          mcs = d3.pointers(event)
          drag = true
          firstPoint = true
          storeData(event)
        }
        if (event.type === 'mouseup' || event.type === 'touchend') {
          drag = false
          $store.commit('vizcanvas/addPoints', tmpPoints)
          tmpPoints.length = 0
          storeHistory()
        }
        svg.on('mousemove touchmove', (event) => {
          event.preventDefault()
          const ed =
            Math.sqrt(Math.pow((mcs[0][0] - d3.pointers(event)[0][0]), 2) + Math.pow((mcs[0][1] - d3.pointers(event)[0][1]), 2))
          if (drag && ed >= density) {
            storeData(event)
            mcs = d3.pointers(event)
          }
        })
      }

      /**
       * Determine the mouse position and calculate where to draw a point
       * @param event MouseEvent
       * @returns {number[]} Tuple of x, y coordinates eg.: [1,2]
       */
      function getCoords (event) {
        const mouseCoords = d3.pointers(event)
        const dispersionValue = toolbarState.dispersionValue
        let x, y
        if (firstPoint) {
          x = Math.round(mouseCoords[0][0])
          y = Math.round(mouseCoords[0][1])
          firstPoint = false
        } else {
          x = Math.round(mouseCoords[0][0]) + Math.floor((Math.random() * dispersionValue) + 1) - (dispersionValue / 2)
          y = Math.round(mouseCoords[0][1]) + Math.floor((Math.random() * dispersionValue) + 1) - (dispersionValue / 2)
        }
        return [x, y]
      }

      /**
       * stores the determined coordinate in the vuex store
       * @param event
       */
      function storeData (event) {
        const point = {}
        const id = 'p' + vizcanvasState.points.length
        const coords = getCoords(event)
        point.id = id
        point.x = coords[0]
        point.y = coords[1]
        point.fill = 'none'
        point.radius = toolbarState.pointRadius
        point.strokeWidth = toolbarState.pointContour
        point.strokeColor = toolbarState.pointColor
        point.label = 'none'
        tmpHistory.push(id)
        tmpPoints.push(point)
        emitPointToPaint(point)
      }

      /**
       * saves data to the history vuex store
       */
      function storeHistory () {
        $store.commit('vizcanvas/addHistory', tmpHistory)
        tmpHistory.length = 0
      }

      /**
       * emmits the point to be painted to the next higher component
       * @param point Point Data
       */
      function emitPointToPaint (point) {
        context.emit('pointToPaint', point)
      }

      /**
       * draws a point on the point layer <br/>
       * How it works: <br/>
       * To ensure that each Vizcanvas component draws the same point, the parent component must be responsible for distributing the coordinate. Therefore, the coordinate is always emitted first, then received as a prop, and then drawn.
       *
       * @param pointToPaint
       */
      function draw (pointToPaint) {
        point
          .attr('fill-opacity', 0.8)
          .attr('stroke-opacity', 0.9)
          .append('circle')
          .attr('id', pointToPaint.id)
          .attr('cx', pointToPaint.x)
          .attr('cy', pointToPaint.y)
          .attr('fill', pointToPaint.fill)
          .attr('r', pointToPaint.radius)
          .attr('stroke-width', pointToPaint.strokeWidth)
          .attr('stroke', pointToPaint.strokeColor)
          .attr('label', 'none')
      }

      /**
       * Redraw the drawing area
       */
      function redraw () {
        removeAllPoints()
        const data = vizcanvasState.points
        point
          .attr('fill-opacity', 0.8)
          .attr('stroke-opacity', 0.9)
          .selectAll('circle')
          .data(data)
          .join('circle')
          .attr('id', d => d.id)
          .attr('cx', d => d.x)
          .attr('cy', d => d.y)
          .attr('fill', d => d.fill)
          .attr('r', d => d.radius)
          .attr('stroke-width', d => d.strokeWidth)
          .attr('stroke', d => d.strokeColor)
          .attr('label', 'none')
      }

      /**
       * clear all layers
       * @param bool
       */
      function clearCanvas (bool) {
        if (bool) {
          clickedButtons.value = ref({
            voronoi: false,
            predict: false
          })
          removeVoronoi()
          removeAllPoints()
          $store.commit('vizcanvas/clearHistory')
          $store.commit('vizcanvas/clearPoints')
        }
      }

      /**
       * clear point layer
       */
      function removeAllPoints () {
        point.selectAll('circle').remove()
      }

      // watch emitted data
      watchEffect(() => processResponse(response.value))
      watchEffect(() => processClickedButtons(clickedButtons.value))

      let showVoronoi = false
      let predictionData

      /**
       * process the response from the server
       * @param response
       */
      function processResponse (response) {
        if (response !== null) {
          predictionData = undefined
          if (response.prediction !== undefined) {
            predictionData = processPredictionData(response.prediction)
          }
          colorizePoints(response)
          if (showVoronoi && response.value !== null && predictionData !== undefined) {
            renderVoronoi(predictionData)
          }
        }
      }

      /**
       * Prepare prediction data
       * @param pd prediction data
       * @returns {[]} Json with {x,y,label}
       */
      function processPredictionData (pd) {
        const data = pd.data
        const labels = pd.predictionlabels
        const newData = []
        for (let i = 0; i < labels.length; i++) {
          newData.push({
            x: data[i].x,
            y: data[i].y,
            label: labels[i]
          })
        }
        return newData
      }

      /**
       * process clicked buttons
       * @param bool
       */
      function processClickedButtons (bool) {
        if (bool !== null && response.value !== null) {
          showVoronoi = bool.voronoi
          presentation(bool)
        }
      }

      /**
       * Decides which data should be used for the rendering of the Voronio diagram
       * Side Effect: the diagram updates after each response from server.
       * @param bool
       */
      function presentation (bool) {
        if (bool.voronoi) {
          if (predictionData === undefined) {
            renderVoronoi(getCircleValues())
          } else {
            renderVoronoi(predictionData)
          }
        } else { removeVoronoi() }
      }

      /**
       * get values of all points on the point plane
       * @returns {[]} Json with x, y, label
       */
      function getCircleValues () {
        const vals = []
        point.selectAll('circle').nodes().forEach((value, index) => {
          vals.push({
            x: Number(value.attributes.cx.value),
            y: Number(value.attributes.cy.value),
            label: Number(response.value.labels[index])
          })
        })
        return vals
      }

      /**
       * get colors based on the unique number of labels
       * background: https://personal.sron.nl/~pault/
       * @param labels Array of labels
       * @returns {[]} Array of colors
       */
      function getColorsFromLabels (labels) {
        const uniques = labels.filter((item, i, ar) => ar.indexOf(item) === i)
        return getColors(uniques.length)
      }

      /**
       * color the painted dots according to the labels
       * @param data Data from Server
       */
      function colorizePoints (data) {
        const colors = getColorsFromLabels(data.labels)
        let i = 0
        point.selectAll('circle')
          .join(
            enter => enter.append('circle'),
            update => update
              .attr('label', function () {
                return data.labels[i]
              })
              .attr('fill', function () {
                const color = colors[data.labels[i]]
                i++
                return color
              })
          )
      }

      /**
       * render voronoi diagramm
       * @param data Data from Server
       */
      function renderVoronoi (data) {
        const xy = []
        const labels = []
        const width = parseInt(getComputedStyle(vizCanvas).width)
        const height = parseInt(getComputedStyle(vizCanvas).height)
        data.forEach(el => {
          xy.push([el.x, el.y])
          labels.push(el.label)
        })
        const delaunay = d3.Delaunay.from(xy).voronoi([0, 0, width, height])
        const colors = getColorsFromLabels(labels)
        removeVoronoi()
        data.forEach((el, i) => {
          voronoi.append('path')
            .attr('d', delaunay.renderCell(i))
            .attr('fill', colors[el.label])
            .attr('stroke', colors[el.label])
        })
      }

      function removeVoronoi () {
        voronoi.selectAll('path').remove()
      }
    })

    return {
      svgId,
      style,
      report,
      colors,
      response,
      clickedButtons,
      onResize (size) {
        report.value = size
      }
    }
  }

}

</script>
