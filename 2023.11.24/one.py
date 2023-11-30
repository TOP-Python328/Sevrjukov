class Class_sample:
    def __init__(self, name):
        self.name = name
        self.cls_fields = {}
        self.attributes = {}

class ClassBuilder:
    def __init__(self, name):
        self.obj = Class_sample(name)
    
    def add_cls_field(self, field_name, field_value):
        self.obj.cls_fields[field_name] = field_value
        self.fields = ''.join(f"{k} = {v}" 
                        for k, v in self.obj.cls_fields.items())
        
        return self
    
    def add_inst_attr(self, attr_name, attr_value):
        self.obj.attributes[attr_name] = attr_value
        self.attrs = ''.join(f"self.{k} = {v}"
                        for k, v in self.obj.attributes.items())
        
        return self

    def __str__(self) -> str:
        if len(self.obj.attributes) > 0 and len(self.obj.cls_fields) > 0:
            return f'''
class {self.obj.name}:
   {self.fields}
   def __init__(self):
       {self.attrs}'''
        
        elif len(self.obj.attributes) > 0 and len(self.obj.cls_fields) == 0:
            return f'''
class {self.obj.name}:
   def __init__(self):
       {self.attrs}'''
        
        elif len(self.obj.attributes) == 0 and len(self.obj.cls_fields) > 0:
            return f'''
class {self.obj.name}:
   {self.fields}'''
        
        elif len(self.obj.attributes) == 0 and len(self.obj.cls_fields) == 0:
            return f'''
class {self.obj.name}:
    pass'''


# cb = ClassBuilder('Test').add_cls_field('__protected', []).add_inst_attr('foo', 'bar')
# print(cb)