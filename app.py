from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# -------------------------------
# 🔧 Initialize Flask App
# -------------------------------
app = Flask(__name__)

# -------------------------------
# 📊 Database Configuration
# -------------------------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'instance', 'hospital.db')
os.makedirs(os.path.join(BASE_DIR, 'instance'), exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

# Initialize Database
db = SQLAlchemy(app)

# -------------------------------
# 📊 Database Models
# -------------------------------

# 1. Appointment Management
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    doctor_specialty = db.Column(db.String(100), nullable=False)
    preferred_doctor = db.Column(db.String(100))
    appointment_date = db.Column(db.String(50))
    medical_docs = db.Column(db.String(200))

# 2. Patient Management
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    admission_type = db.Column(db.String(50))
    medical_history = db.Column(db.Text)
    insurance_details = db.Column(db.String(100))

# 3. Facility Management
class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bed_type = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.Boolean, default=True)

# 4. Staff Management
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50))
    department = db.Column(db.String(50))
    contact = db.Column(db.String(15))

# 5. Supply Management
class Supply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supply_item = db.Column(db.String(100))
    supply_quantity = db.Column(db.Integer)
    supplier = db.Column(db.String(100))

# 6. Financial Management
class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer)
    bill_amount = db.Column(db.Float)

# 7. Insurance Management
class Insurance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer)
    insurance_company = db.Column(db.String(100))

# 8. Laboratory Management
class Laboratory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer)
    test_type = db.Column(db.String(100))

# 9. Report Management
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(100))

# 10. Vaccination Management
class Vaccination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer)
    vaccine_type = db.Column(db.String(100))

# 11. Support Management
class Support(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100))
    feedback = db.Column(db.Text)

# -------------------------------
# 🛠️ Routes
# -------------------------------

@app.route('/')
def index():
    return render_template('index.html')

# 1. Appointment Management
@app.route('/add-appointment', methods=['POST'])
def add_appointment():
    new_appointment = Appointment(
        patient_name=request.form['patient_name'],
        doctor_specialty=request.form['doctor_specialty'],
        preferred_doctor=request.form['preferred_doctor'],
        appointment_date=request.form['appointment_date'],
        medical_docs=request.form['medical_docs']
    )
    db.session.add(new_appointment)
    db.session.commit()
    flash('✅ Appointment added successfully!', 'success')
    return redirect(url_for('index'))

# 2. Patient Management
@app.route('/add-patient', methods=['POST'])
def add_patient():
    new_patient = Patient(
        patient_name=request.form['patient_name'],
        admission_type=request.form['admission_type'],
        medical_history=request.form['medical_history'],
        insurance_details=request.form['insurance_details']
    )
    db.session.add(new_patient)
    db.session.commit()
    flash('✅ Patient added successfully!', 'success')
    return redirect(url_for('index'))

# 3. Facility Management
@app.route('/add-facility', methods=['POST'])
def add_facility():
    new_facility = Facility(
        bed_type=request.form['bed_type'],
        availability=True
    )
    db.session.add(new_facility)
    db.session.commit()
    flash('✅ Facility added successfully!', 'success')
    return redirect(url_for('index'))

# 4. Staff Management
@app.route('/add-staff', methods=['POST'])
def add_staff():
    new_staff = Staff(
        staff_name=request.form['staff_name'],
        role=request.form['staff_role'],
        department=request.form['staff_department'],
        contact=request.form['staff_contact']
    )
    db.session.add(new_staff)
    db.session.commit()
    flash('✅ Staff added successfully!', 'success')
    return redirect(url_for('index'))

# 5. Supply Management
@app.route('/add-supply', methods=['POST'])
def add_supply():
    new_supply = Supply(
        supply_item=request.form['supply_item'],
        supply_quantity=request.form['supply_quantity'],
        supplier=request.form['supplier']
    )
    db.session.add(new_supply)
    db.session.commit()
    flash('✅ Supply updated successfully!', 'success')
    return redirect(url_for('index'))

# 6. Financial Management
@app.route('/add-finance', methods=['POST'])
def add_finance():
    new_finance = Finance(
        patient_id=request.form['patient_id'],
        bill_amount=request.form['bill_amount']
    )
    db.session.add(new_finance)
    db.session.commit()
    flash('✅ Bill generated successfully!', 'success')
    return redirect(url_for('index'))

# 7. Insurance Management
@app.route('/verify-insurance', methods=['POST'])
def verify_insurance():
    new_insurance = Insurance(
        patient_id=request.form['insurance_patient_id'],
        insurance_company=request.form['insurance_company']
    )
    db.session.add(new_insurance)
    db.session.commit()
    flash('✅ Insurance verified successfully!', 'success')
    return redirect(url_for('index'))

# 8. Laboratory Management
@app.route('/add-lab', methods=['POST'])
def add_lab():
    new_lab = Laboratory(
        patient_id=request.form['lab_patient_id'],
        test_type=request.form['test_type']
    )
    db.session.add(new_lab)
    db.session.commit()
    flash('✅ Lab test added successfully!', 'success')
    return redirect(url_for('index'))

# 9. Report Management
@app.route('/generate-report', methods=['POST'])
def generate_report():
    new_report = Report(
        report_type=request.form['report_type']
    )
    db.session.add(new_report)
    db.session.commit()
    flash('✅ Report generated successfully!', 'success')
    return redirect(url_for('index'))

# 10. Vaccination Management
@app.route('/add-vaccination', methods=['POST'])
def add_vaccination():
    new_vaccine = Vaccination(
        patient_id=request.form['vaccine_patient_id'],
        vaccine_type=request.form['vaccine_type']
    )
    db.session.add(new_vaccine)
    db.session.commit()
    flash('✅ Vaccination scheduled successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
