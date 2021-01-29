# importing the necessary dependencies
import pickle
import numpy as np

from flask import Flask, render_template, request
from flask_cors import cross_origin


app = Flask(__name__)  # initializing a flask app

model = pickle.load(open('job_change1.pickle', 'rb'))


@app.route('/', methods=['GET'])  # the home page
@cross_origin()
def homePage():
    return render_template("home.html")


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == 'POST':

        city_development_index = float(request.form['city_development_index'])
        gender = request.form['gender']
        relevent_experience = request.form['relevent_experience']
        enrolled_university = request.form['enrolled_university']
        education_level = request.form['education_level']
        major_discipline = request.form['major_discipline']
        experience = int(request.form['experience'])
        company_size = request.form['company_size']
        company_type = request.form['company_type']
        last_new_job = int(request.form['last_new_job'])
        training_hours = int(request.form['training_hours'])

        Other = 0
        Male = 0
        if gender == 'Male':
            Male = 1
        else:
            Other = 1

        Yes = 0
        if relevent_experience == 'Yes':
            Yes = 1

        no_enrollment = 0
        Part_time_course = 0
        if enrolled_university == 'no_enrollment':
            no_enrollment = 1
        else:
            Part_time_course = 1

        Primary_School = 0
        Masters = 0
        High_School = 0
        Phd = 0
        if education_level == 'Primary_School':
            Primary_School = 1
        elif education_level == 'Masters':
            Masters = 1
        elif education_level == 'High_School':
            High_School = 1
        else:
            Phd = 1

        STEM = 0
        Buisness_Degree = 0
        Humanities = 0
        No_Major = 0
        Other_major = 0
        if major_discipline == 'STEM':
            STEM = 1
        elif major_discipline == 'Buisness_Degree':
            Buisness_Degree = 1
        elif major_discipline == 'Humanities':
            Humanities = 1
        elif major_discipline == 'No_Major':
            No_Major = 1
        else:
            Other_major = 1

        around_50 = 0
        around_100 = 0
        around_500 = 0
        around_1000 = 0
        around_5000 = 0
        around_10000 = 0
        more_than_10000 = 0

        if company_size == 'around_50':
            around_50 = 1
        elif company_size == 'around_100':
            around_100 = 1
        elif company_size == 'around_500':
            around_500 = 1
        elif company_size == 'around_1000':
            around_1000 = 1
        elif company_size == 'around_5000':
            around_5000 = 1
        elif company_size == 'around_10000':
            around_10000 = 1
        else:
            more_than_10000 = 1

        Pvt_Ltd = 0
        Funded_Startup = 0
        Other_type = 0
        Public_Sector = 0
        NGO = 0
        if company_type == 'Pvt_Ltd':
            Pvt_Ltd = 1
        elif company_type == 'Funded_Startup':
            Funded_Startup = 1
        elif company_type == 'Other_type':
            Other = 1
        elif company_type == 'Public_Store':
            Public_Sector = 1
        else:
            NGO = 1

        output = int(model.predict(np.array([[city_development_index, experience, last_new_job,
                                training_hours, High_School, Masters, Phd,
                                Primary_School, around_100, around_1000, around_10000,
                                around_50, around_500, around_5000, more_than_10000,
                                Funded_Startup, NGO, Other_type, Public_Sector, Pvt_Ltd,
                                Buisness_Degree, Humanities, No_Major, Other_major, STEM,
                                Part_time_course, no_enrollment, Yes, Male, Other]]))[0])

        if output == 1:
            return render_template('home.html', prediction_text="Yes,the person is looking for a new job")
        else:
            return render_template('home.html', prediction_text="Nope,the person is not looking for a new job")


if __name__=="__main__":
    app.run(debug=True)

