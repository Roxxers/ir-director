
// Vue instance, makes sure to change delimiter to not conflict with jinja
const vm = new Vue({ 
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        greeting: 'Hello, Vue!'
    },
    methods: {
        changeView: function (car_number, camera_group) {
            // Build formData object.
            let formData = new FormData();
            formData.append('driver_number', car_number);
            formData.append('camera_group', camera_group);
            fetch("api/changeview",
                {
                    body: formData,
                    method: "post"
                });
        }
    }
})


function get_drivers() {
    fetch("http://127.0.0.1:5000/api/session/drivers")
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        console.log(data);
    });
}

