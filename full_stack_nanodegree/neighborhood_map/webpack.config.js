var path = require('path')

module.exports = {
  entry: { app: "./src/js/app.js" },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js'
  },
  module: {
    loaders: [
        {
          test: /\.css$/,
          loader: ["style-loader", "css-loader"]
        },
        {
          test: /\.js$/,
          loader: "babel-loader",
          query: {
            presets: ["es2015"]
          }
        }
    ]
  },
  resolve: {
    extensions: [ '*', '.js', '.css' ],
    modules: [
      path.resolve('./src'),
      path.resolve('./src/static'),
      path.resolve('./node_modules')
    ]
  },
  devServer: {
    contentBase: [
      path.join(__dirname, "src")
    ]
  }
};
