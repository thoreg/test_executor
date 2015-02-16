var User = function(data) {
    if( data ) {
        this.id = data.id;
        this.full_name = data.first_name + ' ' + data.last_name;
    }
};

testRun.factory('users', function() {
    var self = this;
    var users = [];
    var userService = {};

    userService.list = function() {
        return users;
    };

    userService.add_multiple_users = function(data) {
        for(var idx in data) {
            user_data = data[idx];
            users.push(new User(user_data));
        }
    };

    userService.get_full_name_by_id = function(id) {
        user = $.grep(users, function(e){ return e.id == id; });
        if( user ) {
            return user[0].full_name;
        };
    };

    return userService;
});