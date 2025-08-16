{
    "targets": [
        {
            "target_name": "cytubefilters",
            "sources": [
                "src/filter.cc",
                "src/filterlist.cc",
                "src/jsfilterlist.cc",
                "src/util.cc"
            ],
            "dependencies": [
                "deps/libpcre/libpcre.gyp:libpcre"
            ],
            "include_dirs": [
                "deps/libpcre"
            ],
            "defines": ["PCRE_STATIC"],
            "conditions": [
                [ "OS=='win'", {
                    "include_dirs+": ["node_modules/nan", "../nan"]
                }, {
                    "include_dirs+": ["<!(node -e \"console.log(require('nan'))\")"]
                }]
            ]
        }
    ]
}
