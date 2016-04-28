angular.module('starter.controllers', [])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {
  $scope.LoggedIn = true;
  $scope.Logout = function()
  {
    $scope.LoggedIn = false;
  };
})

.controller('Teachers', function($scope, $stateParams, DatabaseFactory) {
  DatabaseFactory.getTeachers()
  .success(function(response){
    console.log(JSON.stringify(response));
    $scope.teachers= response;
  })
  .error(function(error){
    console.log(response);
  });
  console.log('Teachers');
})

.controller('Students', function($scope, $stateParams, DatabaseFactory) {
  $scope.teachers = [1,2,3,4,5,6,7];
  DatabaseFactory.getStudents()
  .success(function(response){
    console.log(response);
    $scope.students = response;
  })
  .error(function(error){
    console.log(response);
  });
  console.log('Students');
})

.controller('LoginSignup', function($scope, UserFactory, Loader, $state, $rootScope) {
  $scope.user={
    'name': '',
    'address': '',
    'city': '',
    'state': '',
    'Email': '',
    'Password': '',
    'uidtype': '',
    'idnum': '',
    'Mobile': ''
  };
  console.log('Login Signup');
  $scope.Login = function()
  {
    
    UserFactory.login(JSON.stringify($scope.user))
    .success(function(response){
      console.log(response);
      if (response == "Login Success")
      {
	Loader.toggleLoadingWithMessage(response);
	
	console.log($rootScope.LoggedIn);
	$state.go('app.home');
      }
      else{
	Loader.toggleLoadingWithMessage(response);
      }
    })
    .error(function(error){
      console.log(error);
    });
  };
  $scope.Signup = function()
  {
    UserFactory.register(JSON.stringify($scope.user))
    .success(function(response){
      console.log(response);
      if (response == "Registration Successfull")
      {
	Loader.toggleLoadingWithMessage(response);
	$state.go('app.home');
      }
      else{
	Loader.toggleLoadingWithMessage(response);
      }
    })
    .error(function(error){
      console.log(error);
    });
  };
})

.controller('Syllabus', function($scope, $stateParams) {
  $scope.teachers = [1,2,3,4,5,6,7];
  console.log('Syllabus');
  $scope.Syllabus = [{"Sem": "3", "Subjects": ["Data Structures","Data Structures (Practical)", "Peripheral Devices & Interfaces", "Hardware Lab (Practical)","Engineering  Mathematics – III", "Digital Electronics", "Digital Electronics  (Practical)", "Microprocessors", "Microprocessors (Practical)"]}, {"Sem": "4", "Subjects": ["Analysis & Design of Algorithms","Analysis & Design of Algorithms (Practical)", "Database Management System", "Database Management System (Practical)","Object Oriented Programming", "Object Oriented Programming (Practical)", "Cyber Law & IPR", "Computer Architecture & Organization"]}, {"Sem": "5", "Subjects": ["Operating  System","Operating  System (Practical)", "Software Engineering", "Software Engineering (Practical)","Computer Network", "Computer Network (Practical)", "Principle of Programming Languages", "Discrete Structures and Computational Logic", "Industrial Training (After 4th Sem)"]}, {"Sem": "6", "Subjects": ["Web Technologies","Web Technologies (Practical)", "Distributed Systems", "Computer Graphics","Computer Graphics (Practical)", "Artificial Intelligence", "Artificial Intelligence (Practical)", "Modeling & Simulation", "Modeling & Simulation (Practical)"]}, {"Sem": "7", "Subjects": ["Compiler Design","Compiler Design (Practical)", "Multimedia System Design", "Software Testing & Quality Assurance","Software Testing & Quality Assurance (Practical)", "Elective -I", "Project – I", "Seminar", "Industrial Training (After 6thSemester)"]}, {"Sem": "8", "Subjects": ["Advanced Database Systems","Digital Image Processing", "Digital Image Processing (Practical)", "Elective –II","Elective II (Practical)", "Elective III", "Project – II"]}];
})
.controller('PlaylistCtrl', function($scope, $stateParams) {
});
