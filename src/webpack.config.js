'use strict'

const { VueLoaderPlugin } = require('vue-loader')
const path = require('path');

module.exports = {
  entry: ['./index.js', './sass/main.scss'],
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, "../static/js/"),
  },
  mode: "production",
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.s[ac]ss$/i,
        exclude: /node_modules/,
        use: [
            {
                loader: "file-loader",
                options: { outputPath: "../css/", name: "main.min.css"}
            }, 
            "sass-loader"
        ],
      },
    ]
  },
  plugins: [
    new VueLoaderPlugin()
  ]
};