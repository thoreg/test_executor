testRun.factory('runFactory', ['$http', function($http) {

    var urlBase = '/api/test_executor/runs/';
    var dataFactory = {};

    dataFactory.objectsAll = function () {
        return $http.get(urlBase);
    };

    dataFactory.create = function (params) {
        return $http({
            withCredentials: true,
            method: 'post',
            url: urlBase,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            data: $.param(params)
        });
    };

    return dataFactory;
}]);