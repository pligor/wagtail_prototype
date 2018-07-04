/// <reference path="../../../node_modules/vue/types/vue.d.ts"/>
// import Vue from "vue";
declare var Vue;

Vue.component('bloglink', {
    props: ['blogposturl', 'blogposttitle'],
    template: '<h3><i><a style="text-decoration: underline; cursor: pointer;" v-on:click="load_blog_page(blogposturl)">{{blogposttitle}}</a></i></h3>',
    methods: {
        load_blog_page: function(blogpost_url: string) {
            console.log('component here');
            console.log(blogpost_url);

            this.$parent.load_blog_page(blogpost_url)
        }
    }
});

let article = new Vue({
    el: 'article', //the id in the body we need it to run
    delimiters: ['${', '}'], // delimiters are the tags which we apply around the vue js variables to display data in html file
    data: {
        loading: false,
        my_target_div: '#blogpage',
        loaded_content: null,
        placeholder_content: '(here the blogpage will be loaded!)'
    },
    mounted: function () { //runs before the mounting of the vue.js instance
        //things you want to happen at the beginning
        this.loaded_content = this.placeholder_content
    },
    methods: {
        load_blog_page: function(blogpost_url: string) {
            console.log('parent here');

            this.loading = true;

            this.$http.get(blogpost_url).then(function (response: any) {
                //this.cur_article = response.data;
                console.log("RESPONSE");
                console.log(response.data);

                this.loaded_content = response.data;

                this.loading = false;
            }).catch(function (err: any) {
                this.loading = false;
                console.log(err)
            })
        },
    }
});
