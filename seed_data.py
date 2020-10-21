from modules.models import User,db

'''
create admin user
# membuat user admin 
'''

def seed_data():
    user = User.query.all() # show all user(s)
    try:
        if not user:
            create_admin = User()
            create_admin.username = 'gibran'
            create_admin.set_password('gibran')
            create_admin.email = 'kelincipercobaan417@gmail.com'
            create_admin.nama_lengkap = 'Gibran Abdillah'
            create_admin.is_admin = True
            db.session.add(create_admin)
            db.session.commit()
            print('Done create user')
    except Exception as e:
        print('Cant create user',e)

        
