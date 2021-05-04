from flask import Flask, render_template, request
from blueprints.Zachary.BubbleSort import BubbleSort
# projects definitions are placed in different file
import projects
from blueprints.Abhijay.__init__ import people_Abhijay_bp
from blueprints.Aiden.__init__ import people_Aiden_bp
from blueprints.Ak.__init__ import people_Ak_bp
from blueprints.Megan.__init__ import people_Megan_bp
from blueprints.Zachary.__init__ import people_Zachary_bp


app = Flask(__name__)
app.register_blueprint(people_Abhijay_bp, url_prefix='/abhijay')
app.register_blueprint(people_Aiden_bp, url_prefix='/aiden')
app.register_blueprint(people_Ak_bp, url_prefix='/ak')
app.register_blueprint(people_Megan_bp, url_prefix='/megan')
app.register_blueprint(people_Zachary_bp, url_prefix='/zachary')

@app.route('/')
def base_route():
    return render_template("base.html", projects=projects.setup())

@app.route('/Mini-lab-storage')
def labstorage_route():
    return render_template("labstorage.html", projects=projects.setup())

@app.route('/Mini-lab-storage-Zach')
def zachlabstorage_route():
    return render_template("Bubble_sort_zach.html", projects=projects.setup())

@app.route('/bubbleSort', methods=["GET", "POST"])
def B_Sort():
    data = []
    original_data = []

    if request.form:
        data_to_sort = request.form.get("dataToSort")
        data = data_to_sort.split()
        original_data = data_to_sort.split()
        if(request.form["data_type"] == "integer"):
        # Need to convert all strings to numbers
            try:
                for i in range(0, len(data)):
                    data[i] = int(data[i])
                    original_data[i] = int(data[i])
            except ValueError:
                return render_template("Bubble_sort_zach.html", output_list="Please enter Strings or Integers only", original_list="Error")
        try:
            BubbleSort(data, True)
            print(data)
        except ValueError:
            return render_template("Bubble_sort_zach.html", output_list="Please enter Strings or Integers only", original_list="Error")
    return render_template("Bubble_sort_zach.html", output_list=data, original_list=original_data)

@app.route('/bubbleSort', methods=["GET", "POST"])
def B_Sort():
    data = []
    original_data = []

    if request.form:
        data_to_sort = request.form.get("dataToSort")
        data = data_to_sort.split()
        original_data = data_to_sort.split()
        if(request.form["data_type"] == "integer"):
            # Need to convert all strings to numbers
            try:
                for i in range(0, len(data)):
                    data[i] = int(data[i])
                    original_data[i] = int(data[i])
            except ValueError:
                return render_template("Ak bubble sort.html", output_list="Please enter Strings or Integers only", original_list="Error")
        try:
            BubbleSort(data, True)
            print(data)
        except ValueError:
            return render_template("Ak bubble sort.html", output_list="Please enter Strings or Integers only", original_list="Error")
    return render_template("Ak bubble sort.html", output_list=data, original_list=original_data)



if __name__ == "__main__":
    # runs the application on the development server
    app.run(port='5000', host='127.0.0.1', debug=True)
