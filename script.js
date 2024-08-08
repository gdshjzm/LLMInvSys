document.addEventListener('DOMContentLoaded', function() {   
    document.getElementById('calculatorForm').addEventListener('submit', function(event) {  
        event.preventDefault();  
  
        var num1 = document.getElementById('num1').value;  
        var num2 = document.getElementById('num2').value;  
        var operation = event.submitter.value; 
  
        var url = `http://localhost:3000/${operation}/${num1}/${num2}`;  
  
        fetch(url)  
            .then(response => response.text())  
            .then(data => {  
                document.getElementById('CalResult').innerText = 'Result: ' + data;  
            })  
            .catch(error => {  
                console.error('Error:', error);  
                document.getElementById('CalResult').innerText = 'Error in calculation';  
            });  
    });  

    document.getElementById('FactorialForm').addEventListener('submit', function(event) {  
        event.preventDefault();  
  
        var num3 = document.getElementById('num3').value;  
  
        var url = `http://localhost:3000/factorial/${num3}`;  
  
        fetch(url)  
            .then(response => response.text())  
            .then(data => {  
                document.getElementById('FacResult').innerText = 'Result: ' + data;  
            })  
            .catch(error => {  
                console.error('Error:', error);  
                document.getElementById('FacResult').innerText = 'Error in calculating factorial';  
            });  
    });  
});