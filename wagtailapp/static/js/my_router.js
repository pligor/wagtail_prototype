"use strict";
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
            template: '<div>(empty at route)</div>'
        }
    },
    {
        path: '/foo',
        component: Foo
    },
    {
        path: '/bar',
        component: Bar
    },
];
var router = new VueRouter({
    routes: routes
});
//# sourceMappingURL=my_router.js.map