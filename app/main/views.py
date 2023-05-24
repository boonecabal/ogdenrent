from datetime import datetime
from flask_login import current_user
from flask import render_template, session, redirect, url_for, flash, request, jsonify
from . import main 
from .forms import NameForm, CustomerApplicationForm, PropertyForm
from .. import db 
from ..models import User, Customer, Property

@main.route('/', methods=['GET', 'POST']) 
def index():
   form = NameForm() 
   if form.validate_on_submit():
      # ...
      return redirect(url_for('.index'))

   return render_template('index.html')

@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
   customers = Customer.query.all()
   form = CustomerApplicationForm()

   properties = Property.query.all()
   properties_form = PropertyForm()

   return render_template(
      'dashboard.html', 
      form=form, 
      properties_form=properties_form, 
      customers=customers, 
      properties=properties)

@main.route('/new_application', methods=['GET', 'POST'])
def new_application():
   form = make_new_application_form(False)

   if form.validate_on_submit():

      # clear database if Clear checkbox is selected
      if request.form.get('clear') != None:
         db.session.query(Customer).delete()
         db.session.commit()

      # add new customer to database
      c = Customer(user=current_user)
      c.first_name = form.first_name.data
      c.last_name = form.last_name.data
      c.dob = form.dob.data
      c.phone = form.phone.data
      c.ssn = form.ssn.data
      c.email = form.email.data

      # num_pets = form.num_pets
      # num_kids = form.num_kids
      # has_pets = form.has_pets
      c.num_pets = 0
      c.num_kids = 0
      c.has_pets = False

      c.prev_addr_street1 = form.prev_addr_street1.data
      c.prev_addr_street2 = form.prev_addr_street2.data
      c.prev_addr_city = form.prev_addr_city.data
      c.prev_addr_state = form.prev_addr_state.data
      c.prev_addr_zip = form.prev_addr_zip.data

      c.photo = url_for('static', filename='img/customers/blank-person.png')

      db.session.add(c)
      db.session.commit()

      flash('Thanks for submitting your name, fiend.  Now leave, please.')

      # return redirect(url_for('main.index'))

   return render_template('new_application.html', form=form)

@main.route('/delete_customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
   c = Customer.query.filter(Customer.id == customer_id).first()
   db.session.delete(c)
   db.session.commit()
   flash('Customer deleted, fiend.  Now leave, please.')
   return redirect(url_for('main.dashboard'))

@main.route('/active_customer/<int:customer_id>', methods=['PUT'])
def get_active_customer(customer_id):
   c = Customer.query.get_or_404(customer_id)
   if c is not None:
      current_user.active_customer_id = c.id
      db.session.add(current_user)
      db.session.commit()

   return jsonify({'active_customer_id': c.id})

@main.route('/customer/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
   c = Customer.query.filter(Customer.id == customer_id).first()

   if c:
      form = CustomerApplicationForm(formdata=request.form, obj=c)

      if request.method == 'GET':
         form.first_name.data = c.first_name
         form.last_name.data = c.last_name
         form.dob.data = c.dob
         form.phone.data = c.phone
         form.ssn.data = c.ssn
         form.email.data = c.email

         form.num_pets = c.form.num_pets 
         form.num_kids = c.form.num_kids 
         form.has_pets = c.form.has_pets 

         form.prev_addr_street1 = c.form.prev_addr_street1 
         form.prev_addr_street2 = c.form.prev_addr_street2 
         form.prev_addr_city = c.form.prev_addr_city 
         form.prev_addr_state = c.form.prev_addr_state 
         form.prev_addr_zip = c.form.prev_addr_zip 

      elif request.method == 'POST' and form.validate():
         save_customer(c, form)
         flash('Customer update, fiend.  Now leave, please.')

      return render_template('edit_customer.html', form=form)
   
   else:
      return 'Error loading #{customer_id}'.format(customer_id=customer_id)

def save_customer(c, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    c.first_name = form.first_name.data
    c.last_name = form.last_name.data
    c.dob = form.dob.data
    c.phone = form.phone.data
    c.ssn = form.ssn.data
    c.email = form.email.data

    if new:
        # Add the new c to the database
        db.session.add(c)

    # commit the data to the database
    db.session.commit()

@main.route('/properties', methods=['GET', 'POST'])
def properties():
   properties = Property.query.all()
   form = PropertyForm()
   return render_template('properties.html', form=form, properties=properties)

@main.route('/property', methods=['GET', 'POST'])
def add_property():
   form = PropertyForm()
   if form.validate_on_submit():
      c = save_property(None, form)

      # redirect back to Dashboard > Properties
      flash('Thanks for submitting your property, fiend.  Now leave, please.')

      return redirect('main.dashboard')

   return render_template('new_property.html', form=form)

@main.route('/property/view/<int:property_id>', methods=['GET'])
def view_property(property_id):
   p = Property.query.filter_by(id=property_id).first()
   form = PropertyForm()
   form.street1.data = p.street1
   form.street2.data = p.street2
   form.city.data = p.city
   form.state.data = p.state
   form.zip_code.data = p.zip_code
   form.lat.data = p.lat
   form.lon.data = p.lon
   return render_template('view_property.html', form=form)

@main.route('/property/edit/<int:property_id>', methods=['GET', 'POST'])
def edit_property(property_id):
   p = Property.query.filter_by(id=property_id).first()
   form = PropertyForm()

   if form.validate_on_submit():
      save_property(p, form)
      flash('Updated property, fiend.  Now leave, please.')

      # redirect to Dashboard > Properties
      return redirect(url_for('main.dashboard'))

   else:
      # fetch existing Property, load form with it
      form.street1.data = p.street1
      form.street2.data = p.street2
      form.city.data = p.city
      form.state.data = p.state
      form.zip_code.data = p.zip_code
      form.lat.data = p.lat
      form.lon.data = p.lon

      return render_template('edit_property.html', form=form, method='PUT', property_id=p.id)

def save_property(p, form):
   if p is None:
      p = Property(form.street1.data, form.street2.data, form.city.data, form.state.data, form.zip_code.data, user=current_user)
   else:
      p.street1 = form.street1.data
      p.street2 = form.street2.data
      p.city = form.city.data
      p.state = form.state.data
      p.zip_code = form.zip_code.data
      p.lon = form.lon.data
      p.lat = form.lat.data

   db.session.add(p)
   db.session.commit()

   return p


def make_new_application_form(load_fields=True):
   form = CustomerApplicationForm()
   if not load_fields:
      return form
   
   form.first_name.data = 'Ted'
   form.last_name.data = 'Bell'
   form.dob.data = datetime.utcnow()
   form.phone.data = '555-555-5555'
   form.ssn.data = '123-45-6789'
   form.email.data = 'ted@example.com'
   
   form.contact_to_verify_last_addr.data = 'C St.'
   form.contact_to_verify_last_phone.data = '555-555-5555'
   form.current_employer.data = 'McDonalds'
   form.position.data = 'Sailor'
   form.emp_contact_name.data = 'Gerald'
   form.emp_contact_phone.data = '444-444-4444'
   form.time_on_job.data = '90'
   form.monthly_net_income.data = '$100,000'
   form.paydays.data = '30'
   form.receiving_ssi.data = False
   form.monthly_ssi_amount.data = '$100,000'

   form.po_name.data = 'Randy Albert'
   form.po_phone.data = '555-555-5555'
   form.offender_number.data = '123456789'

   form.auto_make.data = 'Toyota'
   form.auto_model.data = 'Camry'
   form.auto_color.data = 'Black'
   form.auto_plate.data = 'ABC123'

   form.receiving_ssi.data = False

   form.driver_license.data = '123456789'
   form.state_id.data = '6019325'

   form.num_pets.data = 0
   form.num_kids.data = 0
   form.num_adults.data = 1

   form.prev_addr_street1.data = '123 Main St'
   form.prev_addr_street2.data = 'Apt 1'
   form.prev_addr_city.data = 'New York'
   form.prev_addr_state.data = 'NY'
   form.prev_addr_zip.data = '10001'


   form.emergency_contact_name.data =  'Ted'
   form.emergency_contact_phone.data =  '111-111-1111'

   form.rented_here_before.data = True
   form.rented_here_at_addr.data = '123 Main St'

   form.signature.data	= 'Grant Aster'
   form.date_signed.data	= datetime.utcnow()

   return form