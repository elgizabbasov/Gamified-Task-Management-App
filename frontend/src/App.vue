<template>
  <v-app>
    <v-app-bar>
      <div class="d-flex fa-align-center">
        <v-toolbar-title>Task Management App</v-toolbar-title>
      </div>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
