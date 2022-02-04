import Vue from 'vue';
import Toast from 'buefy';
import Main from './vue/main.vue';

Vue.use(Toast)

const vm = new Vue(Main).$mount("#vm")


