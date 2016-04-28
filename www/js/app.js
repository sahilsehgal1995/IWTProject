// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.controllers' is found in controllers.js
angular.module('starter', ['ionic', 'starter.controllers', 'Data.factory'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);

    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})

.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider

    .state('app', {
    url: '/app',
    abstract: true,
    templateUrl: 'templates/menu.html',
    controller: 'AppCtrl'
  })

  .state('app.home', {
    url: '/home',
    views: {
      'menuContent': {
        templateUrl: 'templates/home.html'
      }
    }
  })
  
  .state('app.progoutcome', {
    url: '/progoutcome',
    views: {
      'menuContent': {
        templateUrl: 'templates/progoutcome.html'
      }
    }
  })
  
  .state('app.courses', {
    url: '/courses',
    views: {
      'menuContent': {
        templateUrl: 'templates/Courses.html'
      }
    }
  })
  
  .state('app.teachers', {
    url: '/teachers',
    views: {
      'menuContent': {
        templateUrl: 'templates/teachers.html',
	controller: "Teachers"
      }
    }
  })
  
  .state('app.students', {
    url: '/students',
    views: {
      'menuContent': {
        templateUrl: 'templates/Students.html',
	controller: "Students"
      }
    }
  })
  
  .state('app.syllabus', {
    url: '/syllabus',
    views: {
      'menuContent': {
        templateUrl: 'templates/syllabus.html',
	controller: "Syllabus"
      }
    }
  })
  
  .state('app.login', {
    url: '/login',
    views: {
      'menuContent': {
        templateUrl: 'templates/login.html',
	controller: "LoginSignup"
      }
    }
  })
  
  .state('app.signup', {
    url: '/signup',
    views: {
      'menuContent': {
        templateUrl: 'templates/signup.html',
	controller: 'LoginSignup'
      }
    }
  })
  
  .state('app.single', {
    url: '/playlists/:playlistId',
    views: {
      'menuContent': {
        templateUrl: 'templates/playlist.html',
        controller: 'PlaylistCtrl'
      }
    }
  });
  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/app/home');
});
