declare var VueRouter: any;

//full feldged component
const Foo = Vue.component('foocomp', {
    template: '<div>foo here</div>',
});

//short version of a component
const Bar = {template: '<div>bar here</div>'};

const routes = [
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

const router = new VueRouter({
    routes
});