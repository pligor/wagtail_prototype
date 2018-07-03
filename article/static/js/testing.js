"use strict";
/// <reference path="node_modules/vue/types/vue.d.ts"/>
// import Vue from "vue";
var vv = new Vue({
    el: '#starting',
    delimiters: ['${', '}'],
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
    mounted: function () {
        //things you want to happen at the beginning
        this.getArticles();
    },
    methods: {
        getArticles: function () {
            this.loading = true;
            this.$http.get('/article-api/article').then(function (response) {
                this.articles = response.data;
                this.loading = false;
            }).catch(function (err) {
                this.loading = false;
                console.log(err);
            });
        },
        getArticle: function (id) {
            this.loading = true;
            this.$http.get('/article-api/article/' + id + '/').then(function (response) {
                this.cur_article = response.data;
                this.loading = false;
            }).catch(function (err) {
                this.loading = false;
                console.log(err);
            });
        },
        addArticle: function () {
            this.loading = true;
            this.$http.post('/article-api/article/', this.new_article).then(function (response) {
                this.loading = false;
                this.getArticles();
            }).catch(function (err) {
                this.loading = false;
                console.log(err);
            });
        },
        updateArticle: function () {
            this.loading = true;
            this.$http.put('/article-api/article/' + this.cur_article.article_id + '/', this.cur_article).then(function (response) {
                this.loading = false;
                this.cur_article = response.data;
                this.getArticles();
            }).catch(function (err) {
                this.loading = false;
                console.log(err);
            });
        },
        deleteArticle: function (id) {
            this.loading = true;
            var url_to_delete = '/article-api/article/' + id + '/';
            console.log(url_to_delete);
            this.$http.delete(url_to_delete).then(function (response) {
                this.loading = false;
                this.getArticles();
            }).catch(function (err) {
                this.loading = false;
                console.log(err);
            });
        }
    }
});
//# sourceMappingURL=testing.js.map