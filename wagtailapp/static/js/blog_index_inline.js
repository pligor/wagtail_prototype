"use strict";
/// <reference path="../../../node_modules/vue/types/vue.d.ts"/>
// import Vue from "vue";
var vv = new Vue({
    el: 'article',
    delimiters: ['${', '}'],
    data: {
        loading: false,
        my_target_div: '#blogpage',
        loaded_content: null,
        placeholder_content: '(here the blogpage will be loaded!)'
    },
    mounted: function () {
        //things you want to happen at the beginning
        this.loaded_content = this.placeholder_content;
    },
    methods: {
        load_blog_page: function (blogpost_url) {
            this.loading = true;
            this.$http.get(blogpost_url).then(function (response) {
                //this.cur_article = response.data;
                console.log("RESPONSE");
                console.log(response.data);
                this.loaded_content = response.data;
                this.loading = false;
            }).catch(function (err) {
                this.loading = false;
                console.log(err);
            });
        },
    }
});
//# sourceMappingURL=blog_index_inline.js.map