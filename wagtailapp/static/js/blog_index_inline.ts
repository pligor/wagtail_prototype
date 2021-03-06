/// <reference path="../../../node_modules/vue/types/vue.d.ts"/>
// import Vue from "vue";
declare var Vue: any;
declare var $: any;

Vue.component('bloglink', {
    props: ['blogposturl', 'blogposttitle'],
    // template: '<h3><i><a v-bind:href="blogposturl" v-on:click.prevent="load_blog_page(blogposturl)">{{blogposttitle}}</a></i></h3>',
    template: '<h3><i><router-link v-bind:to="blogposturl">{{blogposttitle}}</router-link></i></h3>',
    methods: {
        load_blog_page: function (blogpost_url: string) {
            console.log('bloglink component here');
            console.log(blogpost_url);

            this.$parent.load_blog_page(blogpost_url, (data: string) => {
                if (data.indexOf('WAGTAIL_LOGIN_REQUIRED_FLAG') != -1) {
                    //console.log("yes!!!! it is found");
                    //console.log(window.location.pathname);
                    window.location.href = '/tasks_mngr/conn?next=' + window.location.pathname;
                } else {
                    return data
                }
            })
        }
    }
});


let blog_page_comp = Vue.component('blogpagecomp', {
    //v-html="loaded_content"
    template: '<div v-html="loaded_content"></div>',
    data: function () {
        return {
            //loaded_content: '(blogpage NOT found)',
            loaded_content: $('#blog_main_view').html(),
        }
    },
    mounted: function () {
        console.log("here is the route that you requested: " + this.$route.params.wagtailpageroute);
        if (this.$route.params.wagtailpageroute) {
            let blogpost_url = '/wagtailapp/' + this.$route.params.wagtailpageroute;
            this.load_blog_page(blogpost_url);
        } else {
            console.log("at default route")
        }
        //console.log(this.$slots.default[0]);
        //this.loaded_content = 'aaaaa';
        //this.$el.attr('malakas', 'eisai');
        //console.log(this.$el);
    },
    beforeRouteUpdate: function (to: any, from: any, next: any) {
        console.log("reacting to route changes");
        //console.log(to);
        //console.log(from);
        this.load_blog_page(to.path);
        // react to route changes...
        // don't forget to call next()
        next()
    },
    methods: {
        load_blog_page: function (blogpost_url: string) {
            console.log('blogpagecomp component here');
            console.log(blogpost_url);

            this.$parent.load_blog_page(blogpost_url, (data: string) => {
                if (data.indexOf('WAGTAIL_LOGIN_REQUIRED_FLAG') != -1) {
                    //console.log("yes!!!! it is found");
                    //console.log(window.location.pathname);
                    window.location.href = '/tasks_mngr/conn?next=' + window.location.pathname;
                } else {
                    this.loaded_content = data;
                    return data
                }
            })
        },
    }
});

//full feldged component
const Foo = Vue.component('foocomp', {
    template: '<div>foo here</div>',
});

//short version of a component
const Bar = {template: '<div>bar here</div>'};


const routes = [
    /*{
        path: '/wagtailapp/',
        components: {
            default: {
                template: '<div>!!!This is not what you want to see here, use a real root</div>'
            }
        },
    },*/
    {
        path: '/wagtailapp/cms*',
        component: Foo
    },
    {
        path: '/wagtailapp/documents*',
        component: Foo
    },
    {
        path: '/wagtailapp/some_blogs*',
        component: Foo
    },
    {
        path: '/wagtailapp/bar*',
        component: Bar
    },
    {
        path: '/wagtailapp/:wagtailpageroute*',
        components: {
            default: blog_page_comp,
            //namedone: blog_page_comp,
        },
    },
];

const router = new VueRouter({
    routes,
    mode: 'history',
});

let article = new Vue({
    router,
    el: 'article', //the id in the body we need it to run
    delimiters: ['${', '}'], // delimiters are the tags which we apply around the vue js variables to display data in html file
    data: {
        loading: false,
        my_target_div: '#blogpage',

        //loaded_content: null,
        //placeholder_content: '(here the blogpage will be loaded!)'
    },
    mounted: function () { //runs before the mounting of the vue.js instance
        //things you want to happen at the beginning
        //this.loaded_content = this.placeholder_content
    },
    methods: {
        load_blog_page: function (blogpost_url: string, data_processor: (data: string) => string = (data) => data) {
            //console.log('parent here');
            //let target_url = blogpost_url + (blogpost_url.indexOf('?') >= 0 ? '&' : '?') + "origin=vuejs";
            this.loading = true;

            this.$http.get(blogpost_url, {
                headers: {
                    "request_agent": "vuejs"
                }
            }).then(function (response: any) {
                //this.cur_article = response.data;
                console.log("RESPONSE!");
                console.log(response.data);

                let final_data = data_processor(response.data);
                //this.loaded_content = final_data;

                this.loading = false;
            }).catch(function (err: any) {
                this.loading = false;
                console.log(err)
            })
        },
    }
});
