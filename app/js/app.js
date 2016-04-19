'use strict';

var App = angular.module('App', ['ngRoute']);

App.factory('myHttpInterceptor', function ($rootScope, $q) {
    return {
        'requestError': function (config) {
            $rootScope.status = 'HTTP REQUEST ERROR ' + config;
            return config || $q.when(config);
        },
        'responseError': function (rejection) {
            $rootScope.status = 'HTTP RESPONSE ERROR ' + rejection.status + '\n' +
                rejection.data;
            return $q.reject(rejection);
        },
    };
});

App.factory('guestService', function ($rootScope, $http, $q, $log) {
    $rootScope.status = 'Retrieving data...';
    var deferred = $q.defer();
    $http.get('rest/query')
        .success(function (data, status, headers, config) {
            $rootScope.guests = data;
            deferred.resolve();
            $rootScope.status = '';
        });
    return deferred.promise;
});

App.config(function ($routeProvider) {
    $routeProvider.when('/', {
        controller: 'MainCtrl',
        templateUrl: '/partials/main.html',
        resolve: {'guestService': 'guestService'},
    });
    $routeProvider.when('/invite', {
        controller: 'InsertCtrl',
        templateUrl: '/partials/insert.html',
    });

    $routeProvider.when('/update/:id', {
        controller: 'UpdateCtrl',
        templateUrl: '/partials/update.html',
        resolve: {'guestService': 'guestService'},
    });
    $routeProvider.otherwise({
        redirectTo: '/'
    });
});

App.config(function ($httpProvider) {
    $httpProvider.interceptors.push('myHttpInterceptor');
});

App.controller('MainCtrl', function ($scope, $rootScope, $log, $http, $routeParams, $location, $route) {

    $scope.invite = function () {
        $location.path('/invite');
    };

    $scope.update = function (guest) {
        $location.path('/update/' + guest.id);
    };

    $scope.delete = function (guest) {
        $rootScope.status = 'Deleting guest ' + guest.id + '...';
        $http.post('/rest/delete', {'id': guest.id})
            .success(function (data, status, headers, config) {
                for (var i = 0; i < $rootScope.guests.length; i++) {
                    if ($rootScope.guests[i].id == guest.id) {
                        $rootScope.guests.splice(i, 1);
                        break;
                    }
                }
                $rootScope.status = '';
            });
    };

});

App.controller('InsertCtrl', function ($scope, $rootScope, $log, $http, $routeParams, $location, $route) {

    $scope.submitInsert = function () {
        var guest = {
            dato: {
                dato1: $scope.dato1,
                dato2: $scope.dato2,
                dato3: $scope.dato3,
                dato4: $scope.dato4,
                dato5: $scope.dato5,
                dato6: $scope.dato6,
                dato7: $scope.dato7,
                dato8: $scope.dato8,
                dato9: $scope.dato9,
                dato10: $scope.dato10,
                dato11: $scope.dato11,
                dato12: $scope.dato12,
                dato13: $scope.dato13,
                dato14: $scope.dato14,
                dato15: $scope.dato15,
                dato16: $scope.dato16,
            },

            hab: {
                hab1: $scope.hab1,
                hab2: $scope.hab2,
                hab3: $scope.hab3,
                hab4: $scope.hab4,
                hab5: $scope.hab5,
                hab6: $scope.hab6,
                hab7: $scope.hab7,
                hab8: $scope.hab8,
                hab9: $scope.hab9,
                hab10: $scope.hab10,
                hab11: $scope.hab11,
                hab12: $scope.hab12,
                hab13: $scope.hab13,
                hab14: $scope.hab14,
                hab15: $scope.hab15,
                hab16: $scope.hab16,
                hab17: $scope.hab17,
                hab18: $scope.hab18,
                hab19: $scope.hab19,
                hab20: $scope.hab20,
                hab21: $scope.hab21,
                hab22: $scope.hab22,
                hab23: $scope.hab23,
                hab24: $scope.hab24,
                hab25: $scope.hab25,
                hab26: $scope.hab26,
                hab27: $scope.hab27,
                hab28: $scope.hab28,
                hab29: $scope.hab29,
                hab30: $scope.hab30,
                hab31: $scope.hab31,
                hab32: $scope.hab32,
                hab33: $scope.hab33,
                hab34: $scope.hab34,
                hab35: $scope.hab35,
                hab36: $scope.hab36,
                hab37: $scope.hab37,
                hab38: $scope.hab38,
                hab39: $scope.hab39,
                hab40: $scope.hab40,
                hab41: $scope.hab41,
                hab42: $scope.hab42,
                hab43: $scope.hab43,
                hab44: $scope.hab44,
                hab45: $scope.hab45,
                hab46: $scope.hab46,
                hab47: $scope.hab47,
                hab48: $scope.hab48,
                hab49: $scope.hab49,
                hab50: $scope.hab50,
                hab51: $scope.hab51,
            },

            var: {
                var1: $scope.var1,
                var2: $scope.var2,
                var3: $scope.var3,
                var4: $scope.var4,
                var5: $scope.var5,
                var6: $scope.var6,
                var7: $scope.var7,
                var8: $scope.var8,
                var9: $scope.var9,
                var10: $scope.var10,
                var11: $scope.var11,
                var12: $scope.var12,
                var13: $scope.var13,
                var14: $scope.var14,
                var15: $scope.var15,
                var16: $scope.var16,
                var17: $scope.var17,
                var18: $scope.var18,
                var19: $scope.var19,
                var20: $scope.var20,
                var21: $scope.var21,
                var22: $scope.var22,
                var23: $scope.var23,
                var24: $scope.var24,
                var25: $scope.var25,
                var26: $scope.var26,
                var27: $scope.var27,
                var28: $scope.var28,
                var29: $scope.var29,
                var30: $scope.var30,
                var31: $scope.var31,
                var32: $scope.var32,
                var33: $scope.var33,
                var34: $scope.var34,
            },
            info: {
                info1: $scope.info1,
                info2: $scope.info2,
                info3: $scope.info3,
                info4: $scope.info4,
            }

        };
        $rootScope.status = 'Creating...';
        $http.post('/rest/insert', guest)
            .success(function (data, status, headers, config) {
                $rootScope.guests.push(data);
                $rootScope.status = '';
            });
        $location.path('/');
    }
});

App.controller('UpdateCtrl', function ($routeParams, $rootScope, $scope, $log, $http, $location) {

    for (var i = 0; i < $rootScope.guests.length; i++) {
        if ($rootScope.guests[i].id == $routeParams.id) {
            $scope.guest = angular.copy($rootScope.guests[i]);
        }
    }

    $scope.submitUpdate = function () {
        $rootScope.status = 'Updating...';
        $http.post('/rest/update', $scope.guest)
            .success(function (data, status, headers, config) {
                for (var i = 0; i < $rootScope.guests.length; i++) {
                    if ($rootScope.guests[i].id == $scope.guest.id) {
                        $rootScope.guests.splice(i, 1);
                        break;
                    }
                }
                $rootScope.guests.push(data);
                $rootScope.status = '';
            });
        $location.path('/');
    };

});

