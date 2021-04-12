import { createStore } from 'vuex'

// import example from './module-example'
import toolbar from './toolbar'
import vizcanvas from './vizcanvas'
import leftDrawer from './leftDrawer'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      // example
      toolbar,
      vizcanvas,
      leftDrawer

    },

    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING
  })

  return Store
}
