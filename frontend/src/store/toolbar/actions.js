/*
export function someAction (context) {
}
*/
export function clearCanvas (context) {
  context.commit('setClearCanvas')
  if (context.state.clearCanvas) {
    makeFalse(context, 'clearCanvas')
  }
}

export function undo (context) {
  context.commit('setUndo')
  if (context.state.undo) {
    context.dispatch('vizcanvas/undo', null, { root: true })
    makeFalse(context, 'undo')
  }
}

export function erase (context) {
  context.commit('setEraser')
}

async function makeFalse (context, str) {
  setTimeout(function () {
    if (str === 'undo') {
      undo(context)
    }
    if (str === 'clearCanvas') {
      clearCanvas(context)
    }
  }, 50)
}
