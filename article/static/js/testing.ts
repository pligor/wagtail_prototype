/// <reference path="node_modules/vue/types/vue.d.ts"/>
// import Vue from "vue";

let vv = new Vue({
    el: '#starting', //the id in the body we need it to run
    delimiters: ['${', '}'], // delimiters are the tags which we apply around the vue js variables to display data in html file
    data: {
        articles: [],
        loading: false,
        cur_article: {},
        message: null,
        new_article: {
            'article_heading': null,
            'article_body': null,
        }
    },
    mounted: function () { //runs before the mounting of the vue.js instance
        //things you want to happen at the beginning
        this.getArticles();
    },
    methods: {
        getArticles: function () {
            this.loading = true;
            this.$http.get('/article-api/article').then(function (response: any) {
                this.articles = response.data;
                this.loading = false;
            }).catch(function (err: any) {
                this.loading = false;
                console.log(err)
            })
        },

        getArticle: function(id: any) {
            this.loading = true;
            this.$http.get('/article-api/article/' + id + '/').then(function (response: any) {
                this.cur_article = response.data
                this.loading = false;
            }).catch(function (err: any) {
                this.loading = false;
                console.log(err)
            })
        },

        addArticle: function() {
            this.loading = true;
            this.$http.post('/article-api/article/', this.newArticle).then(function(response: any) {
                this.loading = false;
                this.getArticles();
            }).catch(function (err: any) {
                this.loading = false;
                console.log(err)
            })
        },

        updateArticle: function() {
            this.loading = true;
            this.$http.put(
                '/article-api/article/' + this.cur_article.article_id + '/', this.cur_article).then(function(response: any) {
                this.loading = false;
                this.cur_article = response.data;
                this.getArticles();
            }).catch(function (err: any) {
                this.loading = false;
                console.log(err)
            })
        },

        deleteArticle: function(id: any) {
            this.loading = true;
            let url_to_delete = '/article-api/article/' + id + '/';
            console.log(url_to_delete)
            this.$http.delete(url_to_delete).then(function(response: any) {
                this.loading = false;
                this.getArticles();
            }).catch(function (err: any) {
                this.loading = false;
                console.log(err)
            })
        }
    }
});
