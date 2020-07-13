  for(var i = 0; i < 10; i++) {
    console.log(i);
    setTimeout(function() {
      console.log('The number is ' + i);
    },1000);
  }
  //console.log(i);