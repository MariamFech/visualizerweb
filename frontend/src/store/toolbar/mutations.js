/*
export function someMutation (state) {
}
*/
export const setPointColor = (state, color) => {
  state.pointColor = color
}
export const setPointContour = (state, contour) => {
  state.pointContour = contour
}
export const setPointRadius = (state, radius) => {
  state.pointRadius = radius
}
export const setDispersionValue = (state, dispersion) => {
  state.dispersionValue = dispersion
}
export const setDensityValue = (state, density) => {
  state.densityValue = density
}
export const setClearCanvas = (state) => {
  state.clearCanvas = !state.clearCanvas
}
export const setUndo = (state) => {
  state.undo = !state.undo
}
export const setEraser = (state) => {
  state.erase = !state.erase
}
export const setVoronoi = (state, voronoi) => {
  state.voronoi = !state.voronoi
}
