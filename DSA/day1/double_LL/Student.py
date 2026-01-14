class Students:
    def __init__(self, id, name, grades):
        self._id = id
        self._name = name
        for i in grades:
            if isinstance(i,float)==False and len(grades)!=5:
                False
            else:
                self._grades = grades
       
    @property
    def Get_id(self):
        return self._id
    
    @property
    def Get_name(self):
        return self._name
    @property
    def Get_grades(self):
        return self._grades
    
    def Get_average(self):
        if len(self._grades) < 5:
            return False
        avg = 0
        for i in self._grades:
            avg += i
        avg = avg/len(self._grades)
        return avg
    
    @Get_id.setter
    def Set_id(self, id):
        self._id = id
    
    @Get_name.setter
    def Set_name(self, name):
        self._name = name
    
    @Get_grades.setter
    def Set_grades(self, grades:list[float]):
        if isinstance(grades, list) and len(grades)==5:
            for i in grades:
                if isinstance(i,float)==False:
                    return False
                self._grades = grades
                return True
        return False

    