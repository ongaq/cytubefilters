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
            "include_dirs": ["node_modules/nan", "deps/libpcre"],
            "defines": ["PCRE_STATIC"]
        }
    ]
}
