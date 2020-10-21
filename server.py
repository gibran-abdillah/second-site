from app import app 
from modules.controllers import * # di controllers, bakal render dari dir ini. bukan di dir modules

if __name__ == '__main__':
    app.run(debug=True)

