from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
# from wtforms import Form, StringField
# from wtforms.validators import DataRequired
# from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
# from flask_appbuilder.forms import DynamicForm


# class MyForm(DynamicForm):
#     field1 = StringField(('Field1'),
#         description=('Your field number one!'),
#         validators = [DataRequired()], widget=BS3TextFieldWidget())
#     field2 = StringField(('Field2'),
#         description=('Your field number two!'), widget=BS3TextFieldWidget())

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name


class Contact(Model):
    id = Column(Integer, primary_key=True)
    name =  Column(String(150), unique = True, nullable=False)
    address =  Column(String(564), default='Street ')
    birthday = Column(Date)
    personal_phone = Column(String(20))
    personal_cellphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey('contact_group.id'))
    contact_group = relationship("ContactGroup")

    def __repr__(self):
        return self.name