<template>
  <q-layout view="lHh lpR lFf">

    <q-header class="bg-primary text-white " bordered >
      <q-toolbar>
        <q-btn dense flat icon="menu" color="blue-grey-14" padding="xs" @click="toggleLeftDrawer" />

        <q-toolbar-title>
         <Toolbar></Toolbar>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen"
              side="left"
              overlay
              behavior="mobile"
              no-swipe-open
              no-swipe-close
              no-swipe-backdrop>
      <q-card class="flex flex-center" flat>
      <DrawerLeft></DrawerLeft>
      </q-card>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import { ref } from 'vue'
import Toolbar from 'components/Toolbar'
import DrawerLeft from 'components/DrawerLeft'

export default {
  components: { Toolbar, DrawerLeft },
  setup () {
    const leftDrawerOpen = ref(false)

    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
}
</script>
