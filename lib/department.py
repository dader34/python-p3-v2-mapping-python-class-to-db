from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        );
        ''')
        
    @classmethod
    def drop_table(cls):
        CURSOR.execute('''
        DROP TABLE IF EXISTS departments;
    ''')
        
    def save(self):
        CURSOR.execute('''
        INSERT INTO departments (name,location) VALUES ( ? , ? )

        ''',(self.name,self.location))
        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls,name,location):
        department = cls(name,location)
        department.save()
        return department
    
    def update(self):
        CURSOR.execute('''
        UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        ''',(self.name,self.location,self.id))

    def delete(self):
        CURSOR.execute('''
        DELETE FROM departments WHERE id = ?
        ''',(self.id,))


    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
