import pickle
from flask import Flask, request, render_template


# # Load from file
# pickle_model = None
# pkl_filename = "../housing.pkl"
# with open(pkl_filename, 'rb') as file:
#     pickle_model = pickle.load(file)

# Create an instance of Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("house.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/housing-api', methods =["POST"])
def gfg():
    ktch = request.form["ktch"] 
    car = request.form["car"]
    f1 = request.form["f1"]
    cond = request.form["cond"]
    fbath = request.form["fbath"]
    year = request.form["year"] 
    bed = request.form["bed"] 
    f2 = request.form["f2"]
    lot = request.form["lot"]
    hbath = request.form["hbath"]                                     
    print(ktch)


if __name__=='__main__':
   app.run()
