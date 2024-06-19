<template>
  <div id="app">
    <HomePageTop class="simple"></HomePageTop>
<br><br><br>
    <router-view ></router-view>
    <PageBelow class="simple" ></PageBelow>
  </div>
</template>

<script>
import PageBelow from "@/components/mainBoby/PageBelow.vue";
import HomePageTop from "@/components/mainBoby/HomePageTop.vue";
export default {
  components:{
    PageBelow,
    HomePageTop,
  },
  data(){
    return{
    }
  },
  methods:{
  },
}
</script>

<style>
#app {
  position: relative;
}

.simple {
  width: 100%; /* Assuming you want these components to occupy full width */
}

/* Make HomePageTop fixed at the top */
.simple:first-child {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 999; /* Ensure it's above other content */
}

/* Add some padding to the router-view to prevent content from overlapping */
.router-view {
  padding-top: 60px; /* Adjust as needed based on the height of HomePageTop */
}

</style>
