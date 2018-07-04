let app = new Vue({
    el: '#app', //the id in the body we need it to run

    //this is necessary to avoid mixing up with Django template language
    delimiters: ['${', '}'], // delimiters are the tags which we apply around the vue js variables to display data in html file

    data: {
        message: 'Good to go',
    },
});