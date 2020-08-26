<template>
    <div>
        <v-app-bar app color="primary" dark dense>
            <v-app-bar-nav-icon @click.stop="changeVisible"></v-app-bar-nav-icon>
            <v-spacer></v-spacer> <!-- Añade una separa entre medio de los componentes -->
            <v-btn icon><v-icon>mdi-email</v-icon></v-btn>
            <router-link to="/login"><v-btn text>Login</v-btn></router-link> 
        </v-app-bar>
        <Sidebar></Sidebar>
        
    </div>

    
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import {mapMutations} from 'vuex';


export default {
    name: 'Header',
    components: {
        Sidebar,
    },
    methods: {
        ...mapMutations(['changeVisible'])
    },

}
</script>