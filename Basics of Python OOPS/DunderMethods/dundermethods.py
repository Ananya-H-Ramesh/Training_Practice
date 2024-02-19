import logging

logging.basicConfig(
        level = logging.INFO,
        format = "%(process)s %(levelname)s %(message)s",
        )

     
class Employee:

    def __init__(self,empID,FirstName,LastName,EmailID):
        self.empID = empID
        self.FirstName=FirstName
        self.LastName=LastName
        self.EmailID = EmailID

    def __str__(self):
        '''Returns String Represenation of Employee Details'''

        return f"{self.empID}\n{self.FirstName}\n{self.EmailID}"
    
    def __del__(self):
        '''Deletes Employee Instance'''
        
        logging.info(f"Deleted {self.empID} Instance")
        

if __name__ == '__main__':

    try:
        emp = Employee(11892,"Ananya","Ramesh","ananya@gmail.com")
        logging.info(emp)
        del()
        
    except Exception as err:
        logging.error("Error: %s", err)
        raise Exception(err)
    