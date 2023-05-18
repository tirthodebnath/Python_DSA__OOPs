class someSkunkFunk:
    
    '''
    Type Safety Test
    '''
    
    def __init__(self,name: str,exp: int,salary: float,hike: float,hike_cycle: int= 1):
        
        # Validation
        assert type(name) == str, f"Name has to be str, received: {type(name)} !"
        assert type(exp) == int, f"Experience has to be int, received: {type(exp)} !"
        assert type(salary) == int or type(salary) == float, f"Salary has to be int or float, received: {type(salary)} !"
        assert type(hike) == int or type(hike) == float, f"Hike has to be int float, received: {type(hike)} !"
        assert type(hike_cycle) == int, f"Hike Cycle has to be int, received: {type(hike_cycle)} !"
        assert exp >= 0, f"Experience cannot be negative, parameter received: {exp}."
        assert salary >= 0, f"Salary cannot be negative, parameter received: {salary}."
        assert hike >= 0, f"Hike cannot be negative, parameter received: {hike}."
        assert hike_cycle >= 0, f"Experience cannot be negative, parameter received: {hike_cycle}."
        
        # Assigning to self
        self.name = name
        self.exp = exp
        self.salary = salary
        self.hike = hike
        self.hike_cycle = hike_cycle
        
    def initialSalary(self)->float:        
        return round(self.salary/((1 +(self.hike/self.hike_cycle))**self.exp),2)
    
    def inSalLst(self):
        return [self.name,self.initialSalary()]
