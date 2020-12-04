window.addEventListener('load',function () {
    let endpoint = '/api/dashboard_data/'
    var defaultdata = []
    var userdata = []
    var videodata = []
    var labels = []
    $.ajax({
        method: 'GET',
        url: endpoint,
        success: function (data) {
            labels = data.labels
            defaultdata = data.default
            userdata = data.userdata
            videodata = data.videodata
            console.log(data)
            setchart()
            setusertable()
            setvideotable()
        },
        error: function (error_data) {
            console.log("error_data")
            console.log(error_data)
        }
    })

    function setchart(){
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Users count',
                data: defaultdata,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            maintainAspectRatio: false,
            animation:{duration: 10000}
        }
    });
}
    function setusertable(){
        $('#usertable').DataTable( {
            data: userdata,
            columns: [

                { data: 'First name' },
                { data: 'Last name' },
                { data: 'Email' },
                { data: 'Active' },
                { data: 'Superuser' },
                { data: 'Staff' },
                { data: 'Joined date' }
            ]
        });
    }
    function setvideotable(){
        $('#embedvideos').DataTable( {
            data: videodata,
            columns: [

                { data: 'timeStamp' },
                { data: 'url' },
            ]
        });
    }

})

