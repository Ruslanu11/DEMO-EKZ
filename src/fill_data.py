from db.DBmanager import base_manager
from set import gender_data, role_data, user_data, staff_data, patient_data


class DataFiller:
    @staticmethod
    def fill_gender():
        for data in gender_data:
            base_manager.execute("INSERT INTO gender (name) values(?)", (data,))

    @staticmethod
    def fill_staff():
        for data in staff_data:
            base_manager.execute("INSERT INTO staff (name,surname,user_id) values(?,?,?)", data,)

    @staticmethod
    def fill_patient():
        for data in patient_data:
            base_manager.execute("INSERT INTO patient (name, surname, address, phone, gender_id) "
                                 "values(?,?,?,?,?)", data,)

    @staticmethod
    def fill_role():
        for data in role_data:
            base_manager.execute("INSERT INTO role (name) values(?)", (data,))

    @staticmethod
    def fill_user():
        for data in user_data:
            base_manager.execute("INSERT INTO user (login,password,email,role_id) values(?,?,?,?)", data,)



