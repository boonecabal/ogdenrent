from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField, SelectField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class NameForm(FlaskForm): 
   name = StringField('What is your name?', validators=[DataRequired()]) 
   submit = SubmitField('Submit')

class CustomerApplicationForm(FlaskForm):
   first_name = StringField('First name', validators=[DataRequired()])
   last_name = StringField('Last name', validators=[DataRequired()]) 
   dob = DateField('Date of Birth', validators=[DataRequired()])
   phone = StringField('Phone #', validators=[DataRequired()])
   ssn = StringField('SSN', validators=[DataRequired()])
   email = StringField('Email', validators=[DataRequired()])
   driver_license = StringField("Driver's License")
   state_id = StringField('State ID', validators=[DataRequired()])

   num_adults = IntegerField('Number of adults living w/you')
   num_kids = IntegerField('Children')
   num_pets = IntegerField('Pets')
   
   prev_addr_street1 = StringField('Last permanent address')
   prev_addr_street2 = StringField('Street#2')
   prev_addr_city = StringField('City')
   prev_addr_state = StringField('State')
   prev_addr_zip = StringField('Zip')

   contact_to_verify_last_addr	= StringField('Contact to verify last address')
   contact_to_verify_last_phone = StringField('Phone')
   current_employer = StringField('Current employer')
   position = StringField('Position')
   emp_contact_name = StringField('Employer contact info: name')
   emp_contact_phone	= StringField('Phone')
	
   time_on_job	= StringField('Time on job')
   monthly_net_income = StringField('Monthly net income')
   paydays	= StringField('Paydays')
	
   receiving_ssi	= BooleanField('Receiving SSI?')
   monthly_ssi_amount = StringField('Monthly amount')
	
   best_hours = StringField('best_hours')
   between_x_AM = StringField('between_x_AM')
   between_y_PM = StringField('between_y_PM')

   has_service_animal = BooleanField('Do you have, or will you be attempting to secure a service/support animal?')
   former_military	= BooleanField('Are you currently on active duty?')
   is_felon = BooleanField('Are you a felon on parole/probation?')
   is_on_registry = BooleanField('Are you on the S.O. registry?')
   po_name	= StringField('If yes, parole officer: name:')
   po_phone = StringField('Phone')
   offender_number	= StringField('Offender number')
	
   auto_make	= StringField('Automobile: make:')
   auto_model = StringField('Model')
   auto_color = StringField('Color')
   auto_plate = StringField('Plate')

   emergency_contact_name = StringField('In case of an emergency, notify: name')
   emergency_contact_phone	= StringField('Phone')
	
   rented_here_before = BooleanField('Have you rented with us before?')
   rented_here_at_addr	= StringField('If yes, address:')

   signature	= StringField('Signature of applicant')
   date_signed	= DateField('Date')

   photo = StringField('Photo')

   submit = SubmitField('Submit')
