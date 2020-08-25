<template>
    <v-navigation-drawer v-model="visible" app>
        <v-list dense>
            <v-list-item v-for="item in items" :key="item.title" link class="item-sidebar">
                <v-list-item-icon class="texto">
                    <span class="material-icons">
                      {{item.icon}}
                    </span>
                </v-list-item-icon>

                <v-list-item-content class="texto">
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
import {mapState} from 'vuex';

  export default {
    name: 'Sidebar',
    data () {
      return {
        items: [
          { title: 'Home', icon: 'home' },
          { title: 'Inventory', icon: 'all_inbox' },
        ],
      }
    },
    computed: {
        ...mapState(['visible']),    
        
    }

  }
</script>

<style>


.item-sidebar{
  transition: all 0.4s ease;
}
.item-sidebar .texto{
  color: #757575;
}


.item-sidebar:hover{
  margin-left: 7px;
}
.item-sidebar:hover > .texto{
  color: #c3dd;
}
</style>