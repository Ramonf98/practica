<template>
    <v-navigation-drawer :value="visible" app>
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
            <div class="d-flex justify-center py-3">
              <v-btn color="primary" rounded small dark @click.stop="changeVisible">
                <v-icon>arrow_back</v-icon>
              </v-btn>
            </div>

        </v-list>
    </v-navigation-drawer>
</template>

<script>
import {mapState, mapMutations} from 'vuex';

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

        
    },
    methods: {
      ...mapMutations(['changeVisible']),
    },

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