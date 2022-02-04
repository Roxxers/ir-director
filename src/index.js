import Vue from 'vue';
import Toast from 'buefy';
import Main from './vue/main.vue';

Vue.use(Toast)

new Vue(Main).$mount("#vm")

