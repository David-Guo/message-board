module.exports = {
    entry : {
        index : "./index.js"
    },
    devtool: 'source-map',
    output : {
        path : "./lib",
        filename : "bundle.js"
    },
    module : {
        loaders :[
            {test:/\.js$/, loader:'jsx-loader'}
        ]

    }
}