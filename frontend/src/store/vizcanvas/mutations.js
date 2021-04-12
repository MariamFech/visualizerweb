/*
export function someMutation (state) {
}
*/

export function setPoints (state, points) {
  state.points = points
}

export function addPoints (state, points) {
  state.points = state.points.concat(points)
}

export function clearPoints (state) {
  state.points.length = 0
}

export function deletePoint (state, index) {
  delete state.points[index]
}

export function addHistory (state, pointIds) {
  const pids = [].concat(pointIds)
  const hist = {}
  hist.id = state.history.length
  hist.action = 'add'
  hist.pointids = pids
  state.history.push(hist)
}

export function removeHistory (state) {
  state.history.pop()
}

export function clearHistory (state, points) {
  state.history.length = 0
}
