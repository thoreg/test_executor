var Run = function(data) {
    if( data ) {
        this.id = data.id;
        this.requester = data.requester;
        this.start_time = data.start_time;
        this.end_time = data.end_time;
        this.status = data.status;
        this.environment_id = data.environment_id;
    }
};

testRun.factory('runs', function() {
    var self = this;
    var runs = [];
    var runService = {};

    runService.list = function() {
        return runs;
    };

    runService.reset = function() {
        runs = [];
        runService = {};
    };

    runService.add_multiple_runs = function(data) {
        for(var idx in data) {
            run_data = data[idx];
            runs.push(new Run(run_data));
        }
    };

    return runService;
});