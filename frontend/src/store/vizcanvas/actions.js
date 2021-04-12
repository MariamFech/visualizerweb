/*
export function someAction (context) {
}
*/

export function removeAllPoints (context) {
  context.commit('setRemoveAllPoints')
}

export function undo (context) {
  // finde letzten history eintrag
  // lösche points
  // löschen letzten history eintrag
  if (context.state.history.length !== 0) {
    const lastHistoryEntry = context.state.history.find(h => h.id === context.state.history.length - 1)
    const ids = Object.values(lastHistoryEntry.pointids)
    const points = Object.values(context.state.points)
    const p = []
    ids.forEach(id => {
      const x = context.state.points.indexOf(
        context.state.points.find(p => p.id === id)
      )
      p.push(x)
    })
    if (context.state.history.length === 1) {
      points.length = 0
    } else {
      p.forEach(e => {
        points.splice(e, e)
      })
    }
    context.commit('setPoints', points)
    context.commit('removeHistory')
  }
}

export function erase (context) {
  context.commit('setEraser')
}
