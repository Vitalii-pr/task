### QuickStart
```bash
git clonne https://github.com/Vitalii-pr/task
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

## change db connection in .env

python3 manage.py migrate

python3 manage.py runserver
```


###Testing

```bash
pytest
```
[POST] /api/auth/register/                    data = {"name":"some name", "email":"i@gmaiil.com", "password":"simple_password"}
[POST] /api/auth/login/                       data = {"email":"i@gmail.com", "password":"simple_password"} => response {"refresh":"JWTtoken", "access":"JWTtoken"}
[POST] /api/restaurants/                      data = {"name":"Lviv Croissants", address:"Kozelnytska 2a"}
[GET] /api/menu/                              => response {[menus]}    #get all menus
[GET] /api/get_ranking                        => response {[menus]}    #get all today menus
[POST] /api/vote_for_menu/{menu_id}           => response{"message": "successfully voted"} #vote for menu
[POST] /api/add_menu                          data = {"dishes":"some croissants"}

[POST] /api/restaurants/{restaurant.id}/add_restaurant_admin/?user_id={user_id}






In this app you need to create superuser. With this user you can create restaurants and get list of all users.
Also as superuser you can add some users like admins to some restaurant. 
User can upload menu's to restaurants if he is admin of some restaurant.
Users can vote for some menus.     
Retrieve today menus sorted by votes.      
Retrieve all menus.     
