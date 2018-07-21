"use strict";
/// <reference path="../../../node_modules/vue/types/vue.d.ts"/>
Vue.component('bloglink', {
    props: ['blogposturl', 'blogposttitle'],
    template: '<h3><i><a style="text-decoration: underline; cursor: pointer;" v-on:click="load_blog_page(blogposturl)">{{blogposttitle}}</a></i></h3>',
    methods: {
        load_blog_page: function (blogpost_url) {
            console.log('component here');
            console.log(blogpost_url);
            this.$parent.load_blog_page(blogpost_url, function (data) {
                if (data.indexOf('WAGTAIL_LOGIN_REQUIRED_FLAG') != -1) {
                    //console.log("yes!!!! it is found");
                    //console.log(window.location.pathname);
                    window.location.href = '/tasks_mngr/conn?next=' + window.location.pathname;
                }
                else {
                    return data;
                }
            });
        }
    }
});
var article = new Vue({
    router: router,
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
        load_blog_page: function (blogpost_url, data_processor) {
            if (data_processor === void 0) { data_processor = function (data) { return data; }; }
            //console.log('parent here');
            //let target_url = blogpost_url + (blogpost_url.indexOf('?') >= 0 ? '&' : '?') + "origin=vuejs";
            this.loading = true;
            this.$http.get(blogpost_url, {
                headers: {
                    "request_agent": "vuejs"
                }
            }).then(function (response) {
                //this.cur_article = response.data;
                console.log("RESPONSE!");
                console.log(response.data);
                this.loaded_content = data_processor(response.data);
                this.loading = false;
            }).catch(function (err) {
                this.loading = false;
                console.log(err);
            });
        },
    }
});
//# sourceMappingURL=blog_index_inline.js.map