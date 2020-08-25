import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    visible: false,
  },
  mutations: {
    changeVisible(state){
      state.visible = !state.visible;
      console.log(state.visible);
    }
  },
  actions: {
  },
  modules: {
  }
})
