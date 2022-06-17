from flask import Flask, render_template                # Modules  

a = Flask(__name__)        # Constructor       

@a.route("/")      # Hit point / End Point
def home():                       
    return "This is Sample Web Page for SDMIT Students!"         


@a.route("/about")      # Hit point / End Point
def about():                       
    return "Located in Ujire"         
        
@a.route("/contact")      # Hit point / End Point
def contact():                       
    return "Address <br> Mobile No"

@a.route("/sdmpage")      # Hit point / End Point
def index():                       
    return render_template("home.html") 

a.run()                        
