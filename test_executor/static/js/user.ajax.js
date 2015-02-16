testRun.factory('userFactory', ['$http', function($http) {

    var urlBase = '/api/test_executor/users/';
    var dataFactory = {};

    dataFactory.objectsAll = function () {
        return $http.get(urlBase);
    };

    return dataFactory;
}]);