<template>
    <v-navigation-drawer :value="visible" app stateless width="200">
        <v-list dense>


          <router-link :to="item.link" class="no-underline" v-for="item in items" :key="item.title">
            <v-list-item  link class="item-sidebar">
                <v-list-item-icon class="texto">
                    <span class="material-icons">
                      {{item.icon}}
                    </span>
                </v-list-item-icon>

                <v-list-item-content class="texto">
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            </router-link>
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
          { title: 'Home', icon: 'home', link:"/" },
          { title: 'Inventory', icon: 'all_inbox', link:"" },
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

.no-underline{
  text-decoration: none;
}
.item-sidebar{
  transition: all 0.2s linear;
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