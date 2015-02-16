var testRun = angular.module('testRun', ['ui.bootstrap']);
testRun.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

testRun.controller('AppController', ['$scope', '$interval', '$modal',
                                     'runFactory', 'runs',
                                     'userFactory', 'users',
                                     function($scope, $interval,  $modal,
                                              runFactory, runs,
                                              userFactory, users) {
    var self = this;
    $scope.list_of_runs = runs.list();
    $scope.list_of_users = users.list();
    $scope.users = users;

    self.init = function() {
        runFactory.objectsAll()
        .success(function(data) {
            runs.add_multiple_runs(data);
        })
        .error(function(data) {
            $scope.message = data.message;
        });

        userFactory.objectsAll()
        .success(function(data) {
            users.add_multiple_users(data);
        })
        .error(function(data) {
            $scope.message = data.message;
        });
    };
    self.init();

    $interval(function() {
        console.log('Interval - called');
        runFactory.objectsAll()
        .success(function(data) {
            runs.reset();
            runs.add_multiple_runs(data);
            $scope.list_of_runs = runs.list();
        })
        .error(function(data) {
            $scope.error_occured = true;
            $scope.message = data.message;
        });
    }, 1000);

    self.submit = function() {
        params = {'requester_id': $scope.selectedUser.id,
                  'environment_id': $scope.environment_id}

        runFactory.create(params)
            .success(function(data) {
                $scope.error_occured = false;
                $scope.message = data.message;
                $('.message').delay(2000).fadeOut('slow');
            })
            .error(function(data) {
                console.log("ERROR - returned");
                console.log(data);
                $scope.error_occured = true;
                $scope.message = data.message;
            });
    };

    self.info = function() {
        var modalInstance = $modal.open({
            templateUrl: 'info.html',
            controller: 'infoModalCtrl',
        });
    };

}]);

angular.module('testRun').controller('infoModalCtrl', function($scope, $modalInstance) {
    $scope.ok = function () {
        $modalInstance.close();
    };
});