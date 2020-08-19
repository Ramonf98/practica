<template>
    <v-navigation-drawer v-model="visible" absolute temporary>
        <v-list dense>
            <v-list-item v-for="item in items" :key="item.title" link>
                <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
import {mapState,mapMutations} from 'vuex';

  export default {
    name: 'Sidebar',
    data () {
      return {
        items: [
          { title: 'Home', icon: 'home' },
          { title: 'Inventory', icon: 'all_inbox' },
        ]
      }
    },
    computed: {
        ...mapState(['visible']),    
        
    },
    methods: {
        ...mapMutations(['changeVisible'])
    },

  }
</script>