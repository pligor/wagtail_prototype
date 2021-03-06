"use strict";
/// <reference path="../../../node_modules/vue/types/vue.d.ts"/>
Vue.component('static-item', {
    template: '<span>Company <b>is</b> the best</span>'
});
Vue.component('parametric', {
    props: ['param1', 'param2'],
    template: '<li>{{param1}}: {{param2}}</li>'
});
var app = new Vue({
    el: '#app',
    //this is necessary to avoid mixing up with Django template language
    delimiters: ['${', '}'],
    data: {
        message: 'Good to go',
        mytitle: 'Nothing here really',
        seen: true,
        todos: [
            'first todo',
            'second todo',
            'third thing',
            'fourth todo',
            'ktl.'
        ],
    },
    methods: {
        add_curses: function (count) {
            this.message = this.message + (" @^$%^%$$%^&@$".repeat(count));
        },
        get_numbered_todos: function () {
            return this.todos.map(function (value, ind, arr) {
                return {
                    key: ind,
                    val: value
                };
            });
            /*let num_todos: object[] = [];
            let count = 0;
            for(let todo in this.todos) {
                count += 1;
                num_todos.push({
                    key: count,
                    val: this.todos[]
                })
            }

            return num_todos*/
        }
    }
});
//# sourceMappingURL=tutorial.js.map