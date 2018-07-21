"use strict";
var Foo = { template: '<div>foo</div>' };
var Bar = { template: '<div>bar</div>' };
var routes = [
    { path: '/foo', component: Foo },
    { path: '/bar', component: Bar }
];
var router = new VueRouter({
    routes: routes
});
//# sourceMappingURL=my_router.js.map