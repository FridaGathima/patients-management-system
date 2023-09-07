
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
# import click
   
# @click.command()
# def hello():
#     click.echo('Hello World!')

# if __name__ == '__main__':
#     hello()

engine = create_engine('sqlite:///patients_management.db')
Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    id_number = Column(Integer)
    phone_number = Column(Integer)
    age = Column(Integer)
    gender = Column(CHAR)
    ailment_name = Column(String)
    ailment_id = Column(Integer, ForeignKey("ailments.id"))
    doctor_name = Column(String)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    def __init__ (self, id,  first_name, last_name, id_number, phone_number, age, gender, diagnosis_name, diagnosis_id, doctor_name, doctor_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.phone_number = phone_number
        self.age = age
        self.gender = gender
        self.diagnosis_name = diagnosis_name
        self.diagnosis_id = diagnosis_id
        self.doctor_name = doctor_name
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"({self.id} {self.first_name} {self.last_name} {self.id_number} {self.phone_number} {self.age} {self.gender} {self.diagnosis_name} {self.diagnosis_id} {self.doctor_name} {self.doctor_id})"
    

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    id_number = Column(Integer)
    phone_number = Column(Integer)

    def __init__ (self, id,  first_name, last_name, id_number, phone_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.phone_number = phone_number

    def __repr__(self):
        return f"({self.id} {self.first_name} {self.last_name} {self.id_number} {self.phone_number})"
    

class Ailment(Base):
    __tablename__ = "ailments"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__ (self, id,  name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"({self.id} {self.name})"
    
# patients = [
#     Patient(first_name="Bob", last_name="Smith", id_number=4444, phone_number=123456, age=26, gender= "M", ailment_name="cold", ailment_id=1, doctor_name="Mike", doctor_id=2 )
# ]

# sessionmaker = sessionmaker(bind=create_engine('sqlite:///patients_management.db'))

# def create_users():
#     with sessionmaker as session:
#         for patient in patients:
#             session.commit()

# create_users()


# # engine = create_engine("")

    
