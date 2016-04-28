var base ="http://0.0.0.0:5000";

angular.module('Data.factory', [])

.factory('Loader',['$ionicLoading', '$timeout', function($ionicLoading, $timeout){
  var LOADERAPI = {
    showLoading: function(text){
      text = text || 'Loading...';
      $ionicLoading.show({
	template: text
      });
    },
    
    hideLoading: function(){
      $ionicLoading.hide();
    },
    
    toggleLoadingWithMessage: function(text, timeout) {
      
      this.showLoading(text);
      
      $timeout(function(){
	$ionicLoading.hide();
      }, timeout || 3000);
    }
  };
  return LOADERAPI;
}])

.factory('LSFactory', [function(){
  var LSAPI = {
    clear: function(){
      localStorage.clear();
    },
    
    get: function(key){
      return JSON.parse(localStorage.getItem(key));
    },
    
    set: function(key, data){
      return localStorage.setItem(key, JSON.stringify(data));
    },
    
    delete: function(key){
      return localStorage.removeItem(key);
    },
  };
  
  return LSAPI;
}])

.factory('UserFactory', ['$http', 'AuthFactory', function($http, AuthFactory){
  
  var UserAPI = {
    
    login: function(user){
       return $http.post(base + '/api/Teacher/login/?user='+user);
    },
    
    register: function(user){
      return $http.post(base+'/api/Teacher/signup/?user='+user);
    },
    
    logout: function(cid){
      return $http.post(base + '/APIlogout/?cid='+cid);
    }
  };
  return UserAPI;
}])

.factory('DatabaseFactory', ['$http', function($http){
  var Products = {
    
    getStudents: function(){
       return $http.post(base+'/api/Fetchstudents/');
    },
    
    getSyllabus: function(){
      return $http.post(base+'/api/FetchSyllabus/');
    },
    
    getTeachers: function (){
      return $http.post(base+'/api/FetchTeachers/');
    }
    };
  return Products;
}])


.factory('AuthFactory', ['LSFactory', function(LSFactory){
  var userKey = 'user';
  var cidKey ='cid';
  var emailKey = 'email';
  var verificationKey = 'verification';
  
  var AuthAPI = {
    
    isLoggedIn : function(){
      return this.getUser() === null ? false: true;
    },
    
    isVerified : function(){
      return this.getVerification() === 'Verified' ? true: false;
    },
    
    setUser: function(user){
      return LSFactory.set(userKey, user);
    },
    
    getUser: function(){
      return LSFactory.get(userKey);
    },
    
    getEmail: function(){
      return LSFactory.get(emailKey);
    },
    
    setEmail: function(email){
      return LSFactory.set(emailKey, email);
    },
    
    getCid: function(){
      return LSFactory.get(cidKey);
    },
    
    setCid: function(cid){
      return LSFactory.set(cidKey, cid);
    },
    
    getVerification: function(){
      return LSFactory.get(verificationKey);
    },
    
    setVerification: function(verification){
      return LSFactory.set(verificationKey, verification);
    },
    
    deleteAuth: function(){
      LSFactory.delete(userKey);
      LSFactory.delete(cidKey);
      LSFactory.delete(emailKey);
      LSFactory.delete(verificationKey);
    }
  };
  
  return AuthAPI;
}])
;