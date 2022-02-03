const { loadModule } = window["vue2-sfc-loader"];

const options = {
  moduleCache: {
    vue: Vue,
  },
  async getFile(url) {
    const res = await fetch(url);

    if (!res.ok) {
      throw Object.assign(new Error(res.statusText + " " + url), { res });
    }

    return {
      getContentData: (asBinary) => (asBinary ? res.arrayBuffer() : res.text()),
    };
  },
  addStyle() {
    /* unused here */
  },
};

loadModule("/static/js/vue/main.vue", options).then((component) =>
  new Vue(component).$mount("#vm")
);


