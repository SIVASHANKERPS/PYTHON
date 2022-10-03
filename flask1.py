from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
    "result": [
        {
            "name": "siva", 
            "current learning": "python", 
            "emotion": "happy"
        }, 
        {
            "name": "vishal", 
            "current learning": "python", 
            "emotion": "happy"
        }, 
        {
            "name": "sneha", 
            "current learning": "html", 
            "emotion": "happy"
        }
        ]
    }
        
  
        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True)