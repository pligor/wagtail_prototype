"use strict";
/// <reference path="../../../node_modules/vue/types/vue.d.ts"/>
Vue.component('bloglink', {
    props: ['blogposturl', 'blogposttitle'],
    // template: '<h3><i><a v-bind:href="blogposturl" v-on:click.prevent="load_blog_page(blogposturl)">{{blogposttitle}}</a></i></h3>',
    template: '<h3><i><router-link v-bind:to="blogposturl">{{blogposttitle}}</router-link></i></h3>',
    methods: {
        load_blog_page: function (blogpost_url) {
            console.log('bloglink component here');
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
var blog_page_comp = Vue.component('blogpagecomp', {
    template: '<div v-html="loaded_content"></div>',
    data: function () {
        return {
            loaded_content: '(blogpage NOT found)',
        };
    },
    mounted: function () {
        console.log("here is the route that you requested: " + this.$route.params.wagtailpageroute);
        var blogpost_url = '/wagtailapp/' + this.$route.params.wagtailpageroute;
        this.load_blog_page(blogpost_url);
    },
    methods: {
        load_blog_page: function (blogpost_url) {
            var _this = this;
            console.log('blogpagecomp component here');
            console.log(blogpost_url);
            this.$parent.load_blog_page(blogpost_url, function (data) {
                if (data.indexOf('WAGTAIL_LOGIN_REQUIRED_FLAG') != -1) {
                    //console.log("yes!!!! it is found");
                    //console.log(window.location.pathname);
                    window.location.href = '/tasks_mngr/conn?next=' + window.location.pathname;
                }
                else {
                    _this.loaded_content = data;
                    return data;
                }
            });
        }
    }
});
//full feldged component
var Foo = Vue.component('foocomp', {
    template: '<div>foo here</div>',
});
//short version of a component
var Bar = { template: '<div>bar here</div>' };
var routes = [
    {
        path: '/',
        component: {
            template: '<div>(here the blogpage will be loaded! most likely most of the times)</div>'
        },
    },
    {
        path: '/foo',
        component: Foo
    },
    {
        path: '/bar',
        component: Bar
    },
    {
        path: '/wagtailapp/:wagtailpageroute',
        component: blog_page_comp,
    },
];
var router = new VueRouter({
    routes: routes
});
var article = new Vue({
    router: router,
    el: 'article',
    delimiters: ['${', '}'],
    data: {
        loading: false,
        my_target_div: '#blogpage',
    },
    mounted: function () {
        //things you want to happen at the beginning
        //this.loaded_content = this.placeholder_content
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
                var final_data = data_processor(response.data);
                //this.loaded_content = final_data;
                this.loading = false;
            }).catch(function (err) {
                this.loading = false;
                console.log(err);
            });
        },
    }
});
//# sourceMappingURL=blog_index_inline.js.map