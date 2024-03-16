from argparse import REMAINDER
from flask import Blueprint, render_template,flash,url_for,request, make_response, redirect, Flask, session
from tkinter import messagebox
from flask_paginate import Pagination, get_page_parameter
import psycopg2
import json
import base64


def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)

auth = Blueprint('auth', __name__)

@auth.route('/home', methods=['POST', 'GET'])
def home():
        email = session[session['userid']]['email']
        if email:
                return render_template('home.html', email = email)
        else:
                return render_template('home.html')
        
@auth.route('/homeAdm', methods=['post', 'get'])
def homeAdm():
    return render_template('homeAdm.html')

@auth.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
         email = request.form.get('email')
         password1 = request.form.get('password1')
         print(email)
         print(password1)
         if email == 'admin@admin' and password1 == 'admin':
                return redirect(url_for('auth.homeAdm'))
         conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
         crsr = conn.cursor()
         crsr.execute("select email,password1,userid from Users where email=%(email)s and password1=%(password1)s", {'email': email, 'password1': password1})
         data = crsr.fetchall()
         if not email and not password1:
            flash('Trebuie să completați câmpurile!', category='error')
         elif not email and password1:
                flash('Trebuie să introduceți email-ul!', category='error')
         elif not password1 and email:
                flash('Trebuie să introduceți parola!', category='error')
         elif crsr.fetchall() is None:
                flash('Credențialele introduse nu sunt corecte!', category='error')     
         else:
                user_id = str(data[0][2])
                session['userid'] = user_id
                if user_id not in session:
                      session[user_id] = {'email': email, 'lista_filme': [], 'filme_neprelucrate': [],
                                    'lista_seriale': [], 'seriale_neprelucrate': []}
                if email not in session:
                      session[email] = True
                      flash('V-ați logat cu succes!', category='success')
                      return redirect(url_for("auth.formular"))
                return redirect(url_for("auth.formular_rezultate"))
         crsr.close()
         conn.close()
    return render_template("login.html")


@auth.route('/logout', methods = ['GET', 'POST'])
def logout():
     session.pop('email', None)
     return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print(email)
        print(firstName)
        print(password1)
        print(password2)
        
        conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
        crsr = conn.cursor()
        crsr.execute("select email,firstName,password1 from Users where email=%(email)s and firstName=%(firstName)s and password1 = %(password1)s", {'email': email, 'firstName' : firstName, 'password1':password1})
        
        if email is not None and len(email) < 4:
                flash('Email-ul trebuie să aibă mai mult de 3 caractere!', category = 'error')
        elif firstName is not None and len(firstName) <2:
                flash('Prenumele trebuie să aibă mai mult de un caracter!',category = 'error')     
        elif  password1 != password2:
                flash('Parolele nu se potrivesc', category = 'error')
        elif password1 is not None and  len(password1) <7:
                flash('Parola trebuie să aibă cel puțin 7 caractere!', category = 'error')
      

        else:
                flash('Cont creat cu succes!', category = 'success')
                crsr = conn.cursor()
                crsr.execute("insert into Users(email,firstName,password1) VALUES(%(email)s,%(firstName)s, %(password1)s)", {'email': email,'firstName':firstName, 'password1': password1}) 
                conn.commit()
                crsr.close()
                conn.close()
                #return render_template('login.html')    
    return render_template("sign_up.html") 

@auth.route('/formular', methods=['GET', 'POST'])
def formular():
    if request.method == 'POST':
        session.permanent = True
        conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
        crsr2 = conn.cursor()
        crsr3 = conn.cursor()
        crsr4 = conn.cursor()
        crsr5 = conn.cursor()
        crsr6 = conn.cursor()
        crsr7 = conn.cursor()
        gen = request.form.getlist('gen_favorit')
        an_aparitie = request.form.getlist('an_favorit')

        an_aparitie_int = []
        for an in an_aparitie:
            an_int = int(an)
            an_aparitie_int.append(an_int)

        actor = request.form.getlist('actor_favorit')
        categorie_varsta = request.form.getlist('categ_fav')
        print(gen)
        print(an_aparitie)
        print(actor)
        print(categorie_varsta)

        listaux = []
        if len(gen) == 3:
                listaux.append(gen[0])
                listaux.append(gen[1])
                listaux.append(gen[2])
        elif len(gen) == 2:
                listaux.append(gen[0])
                listaux.append(gen[1])
                listaux.append('None')
        elif len(gen) == 1: 
                listaux.append(gen[0])
                listaux.append('None')
                listaux.append('None')
        else:
                listaux.append('None')
                listaux.append('None')
                listaux.append('None')
                #flash('Nu a fost selectat niciun gen !', category = 'error')

        print(listaux)
        
       # crsr.execute("SELECT * FROM Filme F JOIN FilmeGenuri FG ON F.genid = FG.genid JOIN Genuri G ON FG.genid = G.genid JOIN Actori A ON F.actorid = A.actorid JOIN FilmeActori FA ON A.actorid = FA.actorid WHERE (F.genid=%(gen1)s or F.genid=%(gen2)s or F.genid=%(gen3)s) and (F.an_aparitie=%(an_aparitie1)s or F.an_aparitie=%(an_aparitie2)s or F.an_aparitie=%(an_aparitie3)s)  and (A.actorid=%(actor1)s or A.actorid=%(actor2)s or A.actorid=%(actor3)s or A.actorid=%(actor4)s or A.actorid=%(actor5)s) and (F.categorie_varsta=%(categorie_varsta1)s or F.categorie_varsta=%(categorie_varsta2)s )",{'gen1': gen[0],'gen2': gen[1],'gen3': gen[2],'an_aparitie1': an_aparitie[0],'an_aparitie2': an_aparitie[1], 'an_aparitie3':an_aparitie[2],'actor1': actor[0], 'actor2': actor[1],'actor3': actor[2],'actor4': actor[3],'actor5': actor[4] ,'categorie_varsta1':categorie_varsta[0],'categorie_varsta2':categorie_varsta[1] })
        crsr2.execute("SELECT genid from genuri WHERE (numegen = %(gen1)s or numegen = %(gen2)s or numegen = %(gen3)s)", {'gen1': listaux[0], 'gen2':listaux[1], 'gen3':listaux[2]})
        id_tuple=crsr2.fetchall()
        if id_tuple:
            if len(gen) == 3 :
                id_value1 = str(id_tuple[0][0])
                id_value2 = str(id_tuple[1][0])
                id_value3 = str(id_tuple[2][0])
            elif len(gen) == 2 :
                id_value1 = str(id_tuple[0][0])
                id_value2 = str(id_tuple[1][0])
                id_value3 = 0
            elif len(gen) == 1:
                id_value1 = str(id_tuple[0][0])
                id_value2 = 0
                id_value3 = 0
        else:
                id_value1 = 0
                id_value2 = 0
                id_value3 = 0
                flash('Nu fost selectat niciun gen ! Nu s-au găsit rezultate!', category = 'error')
                return render_template('formular_rezultate.html')
               


        listaux2 = []
        if len(actor) == 5:
                listaux2.append(actor[0])
                listaux2.append(actor[1])
                listaux2.append(actor[2])
                listaux2.append(actor[3])
                listaux2.append(actor[4])
        elif len(actor) == 4:
                listaux2.append(actor[0])
                listaux2.append(actor[1])
                listaux2.append(actor[2])
                listaux2.append(actor[3])
                listaux2.append('None')
        elif len(actor) == 3: 
                listaux2.append(actor[0])
                listaux2.append(actor[1])
                listaux2.append(actor[2])
                listaux2.append('None')
                listaux2.append('None')
        elif len(actor) == 2: 
                listaux2.append(actor[0])
                listaux2.append(actor[1])
                listaux2.append('None')
                listaux2.append('None')
                listaux2.append('None')
        elif len(actor) == 1: 
                listaux2.append(actor[0])
                listaux2.append('None')
                listaux2.append('None')
                listaux2.append('None')
                listaux2.append('None')              
        else:
                listaux2.append('None')
                listaux2.append('None')
                listaux2.append('None')
                listaux2.append('None')
                listaux2.append('None') 
                print('n-a fost selectat nimic la actor')

        print(listaux2)
        

        crsr4.execute("SELECT actorid from actori WHERE (nume_prenume = %(actor1)s or nume_prenume = %(actor2)s or nume_prenume = %(actor3)s or nume_prenume = %(actor4)s or nume_prenume = %(actor5)s )",{'actor1': listaux2[0], 'actor2': listaux2[1], 'actor3': listaux2[2], 'actor4': listaux2[3], 'actor5': listaux2[4]})
        idA_tuple=crsr4.fetchall()

        if idA_tuple:
                idA_value1 = str(idA_tuple[0][0]) if len(idA_tuple) >= 1 else 0
                idA_value2 = str(idA_tuple[1][0]) if len(idA_tuple) >= 2 else 0
                idA_value3 = str(idA_tuple[2][0]) if len(idA_tuple) >= 3 else 0
                idA_value4 = str(idA_tuple[3][0]) if len(idA_tuple) >= 4 else 0
                idA_value5 = str(idA_tuple[4][0]) if len(idA_tuple) >= 5 else 0
        else:
                idA_value1 = 0
                idA_value2 = 0
                idA_value3 = 0
                idA_value4 = 0
                idA_value5 = 0

                flash('Nu fost selectat niciun actor! Nu s-au găsit rezultate!', category='error')
                return render_template('formular_rezultate.html')

        '''
        
        if idA_tuple:
            if len(actor) == 5:
                idA_value1 = str(idA_tuple[0][0])
                idA_value2 = str(idA_tuple[1][0])
                idA_value3 = str(idA_tuple[2][0])
                idA_value4 = str(idA_tuple[3][0])
                idA_value5 = str(idA_tuple[4][0])
            elif len(actor) == 4:
                idA_value1 = str(idA_tuple[0][0])
                idA_value2 = str(idA_tuple[1][0])
                idA_value3 = str(idA_tuple[2][0])
                idA_value4 = str(idA_tuple[3][0])
                idA_value5 = 0
            elif len(actor) == 3: 
                idA_value1 = str(idA_tuple[0][0])
                idA_value2 = str(idA_tuple[1][0])
                idA_value3 = str(idA_tuple[2][0])
                idA_value4 = 0
                idA_value5 = 0
            elif len(actor) == 2: 
                idA_value1 = str(idA_tuple[0][0])
                idA_value2 = str(idA_tuple[1][0])
                idA_value3 = 0
                idA_value4 = 0
                idA_value5 = 0
            elif len(actor) == 1: 
                idA_value1 = str(idA_tuple[0][0])
                idA_value2 = 0
                idA_value3 = 0
                idA_value4 = 0
                idA_value5 = 0 
            else:
                idA_value1 = 0
                idA_value2 = 0
                idA_value3 = 0
                idA_value4 = 0
                idA_value5 = 0 
                flash('Nu fost selectat niciun actor ! Nu s-au găsit rezultate!', category = 'error')
                return render_template('formular_rezultate.html')

         '''   

        listaux3 = []
        if len(an_aparitie) == 3:
                listaux3.append(an_aparitie[0])
                listaux3.append(an_aparitie[1])
                listaux3.append(an_aparitie[2])
        elif len(an_aparitie) == 2:
                listaux3.append(an_aparitie[0])
                listaux3.append(an_aparitie[1])
                listaux3.append(0)
        elif len(an_aparitie) == 1: 
                listaux3.append(an_aparitie[0])
                listaux3.append(0)
                listaux3.append(0)
        else:
                listaux3.append(0)
                listaux3.append(0)
                listaux3.append(0)
                print('n-a fost selectat nimic la gen')

        print(listaux3)

        crsr5.execute("SELECT an_aparitie from filme WHERE (an_aparitie= %s or an_aparitie = %s or an_aparitie = %s)",[ listaux3[0], listaux3[1], listaux3[2] ])
        idAN_tuple=crsr5.fetchall()

        print(idAN_tuple)
        if idAN_tuple :
            if len(an_aparitie) == 3 :
                idAN_value1 = str(idAN_tuple[0][0])
                idAN_value2 = str(idAN_tuple[1][0])
                idAN_value3 = str(idAN_tuple[2][0])
            elif len(an_aparitie) == 2:
                idAN_value1 = str(idAN_tuple[0][0])
                idAN_value2 = str(idAN_tuple[1][0])
                idAN_value3 = 0
            elif len(an_aparitie) == 1:
                idAN_value1 = str(idAN_tuple[0][0])
                idAN_value2 = 0
                idAN_value3 = 0
        else :
                idAN_value1 = 0
                idAN_value2 = 0
                idAN_value3 = 0
                flash('Nu fost selectat niciun an de apariție ! Nu s-au găsit rezultate!', category = 'error')
                return render_template('formular_rezultate.html')

        
        listaux4 = []
    
        if len(categorie_varsta) == 2:
                listaux4.append(categorie_varsta[0])
                listaux4.append(categorie_varsta[1])
        elif len(categorie_varsta) == 1: 
                listaux4.append(categorie_varsta[0])
                listaux4.append('None')
        else:
                listaux4.append('None')
                listaux4.append('None')
                print('Nu fost selectat nimic la categorie !')

        print(listaux4)
              

        crsr6.execute("SELECT distinct categorie_varsta from filme WHERE (categorie_varsta= %(categorie_varsta1)s or categorie_varsta = %(categorie_varsta2)s )",{'categorie_varsta1': listaux4[0], 'categorie_varsta2': listaux4[1]})
        idCATEGORIE_tuple=crsr6.fetchall()
        print(idCATEGORIE_tuple)
        if idCATEGORIE_tuple : 
            if len(categorie_varsta) == 2:
                idCATEG_value1 = str(idCATEGORIE_tuple[0][0])
                idCATEG_value2 = str(idCATEGORIE_tuple[1][0])
            elif len(categorie_varsta) == 1:
                idCATEG_value1 = str(idCATEGORIE_tuple[0][0])
                idCATEG_value2 = 'None'        
        else:

                print('Nu fost selectat nimic la categorie !')
                flash('Nu fost selectată nicio categorie ! Nu s-au găsit rezultate!', category = 'error')
                return render_template('formular_rezultate.html') 

        


# ----------------------------------QUERY FILME ------------------------------------------------------

        crsr3.execute("SELECT DISTINCT titlu, descriere, durata, an_aparitie, string_agg(DISTINCT categorie_varsta, ', ') AS categorie, string_agg(DISTINCT A.nume_prenume, ', ') AS actori, encode(image_data, 'base64') as imagine from Filme F JOIN filmeactori FA on F.filmid = FA.filmid JOIN Actori A on FA.actorid = A.actorid JOIN filmegenuri FG on F.filmid = FG.filmid JOIN genuri G on FG.genid = G.genid WHERE (G.genid = %(id_value1)s or G.genid = %(id_value2)s or G.genid = %(id_value3)s) or (an_aparitie = %(idAN_value1)s or an_aparitie = %(idAN_value2)s or an_aparitie = %(idAN_value3)s) or (F.categorie_varsta=%(idCATEG_value1)s OR F.categorie_varsta=%(idCATEG_value2)s) or (A.actorid = %(idA_value1)s or A.actorid = %(idA_value2)s or A.actorid = %(idA_value3)s or A.actorid = %(idA_value4)s or A.actorid = %(idA_value5)s) GROUP BY titlu, descriere,durata,an_aparitie,categorie_varsta,encode(image_data, 'base64') """,{'id_value1': id_value1,'id_value2': id_value2,'id_value3': id_value3, 'idAN_value1': idAN_value1, 'idAN_value2': idAN_value2,'idAN_value3': idAN_value3, 'idCATEG_value1': idCATEG_value1,'idCATEG_value2': idCATEG_value2, 'idA_value1': idA_value1,'idA_value2': idA_value2,'idA_value3': idA_value3,'idA_value4': idA_value4,'idA_value5': idA_value5})
        nume_tuple=crsr3.fetchall()
        my_json_string = json.dumps(nume_tuple)
        my_list = json.loads(my_json_string)
        result_list = [(x[0], x[1], x[2], x[3], x[4], x[5], x[6]) for x in my_list]
        for x in my_list:
                image_bytes = bytes(x[6], encoding='utf-8')
                decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                x[6] = decoded_image


        user_id = session['userid']
        if user_id is not None:
                session[user_id]['lista_filme'] = result_list
                session[user_id]['filme_neprelucrate'] = nume_tuple

        



# ----------------------------------QUERY SERIALE ------------------------------------------------------


        crsr7.execute(  """
        SELECT DISTINCT titlu, numar_episoade, descriere, actori, ani_desfasurare,statusul, categorie_varsta, encode(image_data, 'base64') as imagine, genuri
        FROM Seriale S 
        WHERE (genuri ~%(gen1)s or genuri ~%(gen2)s or genuri ~%(gen3)s) 
        or (ani_desfasurare =%(an_aparitie1)s or ani_desfasurare =%(an_aparitie2)s or ani_desfasurare =%(an_aparitie3)s) 
        or (categorie_varsta =%(categorie_varsta1)s OR categorie_varsta =%(categorie_varsta2)s)
        or (actori ~%(actor1)s or actori ~%(actor2)s or actori ~%(actor3)s or actori ~%(actor4)s or actori ~%(actor5)s)""",
        {
                'gen1': listaux[0],
                'gen2': listaux[1],
                'gen3': listaux[2],
                'actor1': listaux2[0],
                'actor2': listaux2[1],
                'actor3': listaux2[2],
                'actor4': listaux2[3],
                'actor5': listaux2[4],
                'an_aparitie1': listaux3[0],
                'an_aparitie2': listaux3[1],
                'an_aparitie3': listaux3[2],
                'categorie_varsta1': listaux4[0],
                'categorie_varsta2': listaux4[1]
        }
        
        )
     
        nume_tuple2 = crsr7.fetchall()
        my_json_string2 = json.dumps(nume_tuple2)
        my_list2 = json.loads(my_json_string2)
        result_list2 = [(y[0], y[1], y[2], y[3], y[4], y[5], y[6],y[7], y[8]) for y in my_list2]
        for y in my_list2:
                image_bytes = bytes(y[7], encoding='utf-8')
                decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                y[7] = decoded_image

        if user_id is not None:
                session[user_id]['lista_seriale'] = result_list2
                session[user_id]['seriale_neprelucrate'] = nume_tuple2

#-------------------------------------REDIRECTIONARE ---------------------------------------------------------
        if not session[user_id]['seriale_neprelucrate'] and not session[user_id]['filme_neprelucrate']:
                flash('Nu s-au găsit rezultate!', category = 'error')
                return redirect(url_for('auth.formular_rezultate')) 
        elif session[user_id]['filme_neprelucrate'] and not session[user_id]['seriale_neprelucrate'] :
                flash('Nu s-au găsit seriale!', category = 'error') 
                return redirect(url_for('auth.formular_rezultate'))
        elif not session[user_id]['filme_neprelucrate'] and session[user_id]['seriale_neprelucrate'] :
                flash('Nu s-au găsit filme!', category = 'error') 
                return redirect(url_for('auth.formular_rezultate'))
        elif session[user_id]['filme_neprelucrate'] and session[user_id]['seriale_neprelucrate']:
                return redirect(url_for('auth.formular_rezultate'))    


    return render_template('formular.html', email=session[session['userid']]['email'])

@auth.route("/add-to-favorites", methods=["POST"])
def add_to_favorites():
    user_id = session.get('userid') # Replace this with your logic to retrieve the user ID
    movie_index = int(request.json.get("movieIndex"))
    movie = session['filme_toate'][movie_index]  # Retrieve the selected movie from your data source

    session.setdefault(user_id, {}).setdefault("lista_filme", []).append(movie)

    flash('Filmul a fost adăugat cu succes în Recomandări!', category = 'success') 
    return "Movie added to favorites", 200


@auth.route("/add-to-favorites1", methods=["POST"])
def add_to_favorites1():
    user_id = session.get('userid') # Replace this with your logic to retrieve the user ID
    series_index = int(request.json.get("seriesIndex"))
    series = session['seriale_toate'][series_index]  # Retrieve the selected movie from your data source

    session.setdefault(user_id, {}).setdefault("lista_seriale", []).append(series)
    
    flash('Serialul a fost adăugat cu succes în Recomandări!', category = 'success') 
    return "Serial added to favorites", 200


@auth.route("/delete-from-favorites", methods=["POST"])
def delete_from_favorites():
    user_id = session.get('userid')  # Replace this with your logic to retrieve the user ID
    movie_index = int(request.json.get("movieIndex"))
    movies = session.setdefault(user_id, {}).setdefault("lista_filme", [])
    
    if movie_index < len(movies):
        deleted_movie = movies.pop(movie_index)
        flash('Filmul a fost șters cu succes!', category = 'success') 
        return f"Movie '{deleted_movie}' deleted from favorites", 200
    else:
        return "Invalid movie index", 400


@auth.route("/delete-from-favorites1", methods=["POST"])
def delete_from_favorites1():
    user_id = session.get('userid')  # Replace this with your logic to retrieve the user ID
    series_index = int(request.json.get("seriesIndex"))
    series = session.setdefault(user_id, {}).setdefault("lista_seriale", [])
    
    if series_index < len(series):
        deleted_series = series.pop(series_index)
        flash('Serialul a fost șters cu succes!', category = 'success') 
        return f"Series '{deleted_series}' deleted from favorites", 200
    else:
        return "Invalid series index", 400

@auth.route('/addMovie', methods=['post', 'get'])
def addMovie():
    if request.method == 'POST':
        iD = request.form.get('idName')
        movie = request.form.get('movieName')
        descr = request.form.get('descrName')
        dur = request.form.get('durName')
        an = request.form.get('anName')
        categ = request.form.get('categName')
        act = request.form.get('actName')
        gen = request.form.get('genName')
        dire = request.form.get('dirName')
        scen = request.form.get('scenName')

        conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
        crsr = conn.cursor()
        crsr1 = conn.cursor()
        crsr2 = conn.cursor()
        crsr3 = conn.cursor()
        
        imagine = request.files.get('filmPhoto')
        img = imagine.read()

        try:
            crsr.execute("INSERT INTO Filme (filmid, directorid, genid, actorid, scenariuid, titlu, durata, descriere, an_aparitie, categorie_varsta, image_data) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (iD,dire, gen,act, scen ,movie,dur,descr,an,categ,psycopg2.Binary(img)))
            crsr1.execute("insert into filmegenuri (filmid, genid) values (%s,%s)", (iD, gen))
            crsr2.execute("insert into filmeactori (filmid, actorid) values (%s,%s)", (iD, act))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            conn.close()

        flash('Film adăugat cu succes!', category='success')
        return redirect(url_for('auth.filmeAdm'))
    
    if request.method == 'GET':
        conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
        crsr = conn.cursor() 
        crsr1 = conn.cursor()
        crsr2 = conn.cursor()
        crsr3 = conn.cursor()
        crsr.execute("select distinct scenariuid, nume from Scenariu")
        crsr1.execute("select distinct actorid, nume_prenume from Actori")
        crsr2.execute("select distinct directorid, nume_prenume from Director")
        crsr3.execute("select distinct genid, numegen from Genuri")
        datescen = crsr.fetchall()
        dateactor = crsr1.fetchall()
        datedir = crsr2.fetchall()
        dategen = crsr3.fetchall()
        conn.close()

        date_json = json.dumps(datescen)
        list_scen= json.loads(date_json)

        date_json1 = json.dumps(dateactor)
        list_act= json.loads(date_json1)

        date_json2 = json.dumps(datedir)
        list_dir= json.loads(date_json2)

        date_json3 = json.dumps(dategen)
        list_gen= json.loads(date_json3)


        scenarii = [(x[0], x[1]) for x in list_scen]
        actori = [(y[0], y[1]) for y in list_act]
        director = [(z[0], z[1]) for z in list_dir]
        genuri = [(w[0], w[1]) for w in list_gen]

        return render_template('addMovie.html', scenarii=scenarii, actori=actori, director=director, genuri=genuri)
    
@auth.route('/addSerial', methods=['post', 'get'])
def addSerial():
    if request.method == 'POST':
        idName= request.form['idName']
        serName = request.form['serName']
        nrepName = request.form['nrepName']
        descrName = request.form['descrName']
        actName = request.form['actName']
        aniiName = request.form['aniiName']
        statName = request.form['statName']
        scrName = request.form['scrName']
        dirName = request.form['dirName']
        genName = request.form['genName']
        categName = request.form['categName']

        conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
        crsr = conn.cursor()
        
        imagine = request.files['serialPhoto']
        img = imagine.read()

        try:
            crsr.execute("INSERT INTO Seriale (serialid, titlu, numar_episoade, descriere, actori, ani_desfasurare, statusul, scriitori, director, genuri, categorie_varsta,image_data) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (idName,serName, nrepName,descrName, actName ,aniiName,statName,scrName,dirName,genName,categName,psycopg2.Binary(img)))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            conn.close()

        flash('Serial adăugat cu succes!', category='success')
        return redirect(url_for('auth.serialeAdm'))
    
    return render_template('addSerial.html')

@auth.route('/update_movie', methods=['POST'])
def update_movie():
        if request.method == 'POST': 
                title = request.form.get('title')
                duration = request.form.get('duration')
                description = request.form.get('description')
                release_year = request.form.get('release_year')
                age_category = request.form.get('age_category')
                movie_id = request.form.get('movie_id')
                
                conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
                crsr = conn.cursor()
                try:
                        crsr.execute("""
                        UPDATE Filme
                        SET titlu = %s, durata = %s, descriere = %s,an_aparitie = %s,categorie_varsta = %s
                        WHERE filmid = %s
                        """, (title, duration, description,release_year,age_category,movie_id))
                        conn.commit()
                        flash('Film modificat cu succes!', category='success')
                        return redirect(url_for('auth.filmeAdm'))
                except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                        conn.rollback()
                        flash('Eroare la modificarea filmului!', category='error')
                        return redirect(url_for('auth.filmeAdm'))
                finally:
                        conn.close()
        return render_template('filmeAdm.html')

@auth.route('/update_serial', methods=['POST'])
def update_serial():
        if request.method == 'POST': 
                title = request.form.get('title')
                eps = request.form.get('eps')
                descr = request.form.get('descr')
                actori = request.form.get('actori')
                ani_desf = request.form.get('ani_desf')
                stat = request.form.get('stat')
                scriit = request.form.get('scriit')
                dire = request.form.get('dir')
                genuri = request.form.get('genuri')
                categ_varsta = request.form.get('categ_varsta')
                serial_id = request.form.get('serial_id')
                
                conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
                crsr = conn.cursor()
                try:
                        crsr.execute("""
                        UPDATE Seriale
                        SET titlu = %s, numar_episoade = %s, descriere = %s,actori = %s,ani_desfasurare = %s,statusul = %s,scriitori = %s,director = %s,
                        genuri = %s,categorie_varsta = %s
                        WHERE serialid = %s
                        """, (title, eps, descr,actori,ani_desf,stat,scriit, dire,genuri,categ_varsta,serial_id))
                        conn.commit()
                        flash('Serial modificat cu succes!', category='success')
                        return redirect(url_for('auth.serialeAdm')) 
                except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                        conn.rollback()
                        flash('Eroare la modificarea serialului!', category='error')
                        return redirect(url_for('auth.serialeAdm'))
                finally:
                        conn.close()
        return render_template('serialeAdm.html')

@auth.route('/delete_movie', methods=['POST'])
def delete_movie():
        if request.method == 'POST': 
                movie_id = request.json["movie_id"]
                
                conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
                crsr = conn.cursor()
                try:
                        crsr.execute("delete from Filme WHERE filmid = %s", (movie_id,))
                        conn.commit()
                        flash('Film șters cu succes!', category='success')
                        return redirect(url_for('auth.filmeAdm')) 
                except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                        conn.rollback()
                        flash('Eroare la ștergerea filmului!', category='error')
                        return redirect(url_for('auth.filmeAdm'))
                finally:
                        conn.close()
        return render_template('filmeAdm.html')

@auth.route('/delete_serial', methods=['POST'])
def delete_serial():
        if request.method == 'POST': 
                serial_id = request.json["serial_id"]
                
                conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
                crsr = conn.cursor()
                try:
                        crsr.execute("delete from Seriale WHERE serialid = %s", (serial_id,))
                        conn.commit()
                        flash('Serial șters cu succes!', category='success')
                        return redirect(url_for('auth.serialeAdm')) 
                except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                        conn.rollback()
                        flash('Eroare la ștergerea serialului!', category='error')
                        return redirect(url_for('auth.serialeAdm'))
                finally:
                        conn.close()
        return render_template('serialeAdm.html')

@auth.route('/filme', methods=['GET', 'POST'])
def filme(): 
    if request.method == 'GET':
            conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
            crsr = conn.cursor()
            crsr2 = conn.cursor()
            
            crsr.execute("SELECT DISTINCT titlu, descriere, durata, an_aparitie, categorie_varsta, string_agg(DISTINCT A.nume_prenume, ', ') AS actori, encode(image_data, 'base64') as imagine, string_agg(DISTINCT G.numegen, ', ') AS Genuri, D.nume_prenume from Filme F JOIN filmeactori FA on F.filmid = FA.filmid JOIN Actori A on FA.actorid = A.actorid JOIN filmegenuri FG on F.filmid = FG.filmid JOIN genuri G on FG.genid = G.genid JOIN director D on F.directorid = D.directorid GROUP BY titlu, descriere,durata,an_aparitie,categorie_varsta,encode(image_data, 'base64'), D.nume_prenume")
            
            crsr2.execute("SELECT distinct titlu, numar_episoade, descriere,actori,ani_desfasurare, statusul, categorie_varsta, encode(image_data, 'base64') as imagine, scriitori, genuri, director from Seriale S")
            
            
            nume_tuple=crsr.fetchall()
            nume_tuple2 = crsr2.fetchall()

            conn.close()

            if not nume_tuple :
                    flash('Nu s-au găsit rezultate!', category = 'error')
                    return render_template('formular_rezultate.html')
            else:
                
                    my_json_string = json.dumps(nume_tuple)
                    my_list = json.loads(my_json_string)
                    result_list2 = [(x[0], x[1], x[2], x[3], x[4], x[5], x[6],x[7],x[8]) for x in my_list]
                    for x in my_list:
                        
                        # Convert the image data to bytes
                        image_bytes = bytes(x[6], encoding='utf-8')
                        # Encode the bytes as base64
                        decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                        x[6] = decoded_image
                        # Add the encoded image to the result list
                        #result_list.append((x[0], x[1], x[2], x[3], x[4], x[5], decoded_image))

           
            session['filme_toate'] = result_list2
            lungime2 = len(result_list2)

            if not nume_tuple2 :
                    flash('Nu s-au găsit rezultate!', category = 'error')
                    return render_template('formular_rezultate.html')
            else:
                
                    my_json_string2 = json.dumps(nume_tuple2)
                    my_list2 = json.loads(my_json_string2)
                    result_list3 = [(x[0], x[1], x[2], x[3], x[4], x[5], x[6],x[7],x[8],x[9], x[10]) for x in my_list2]
                    for x in my_list2:
                        
                        # Convert the image data to bytes
                        image_bytes = bytes(x[9], encoding='utf-8')
                        # Encode the bytes as base64
                        decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                        x[9] = decoded_image


                        # Combinați cele două liste
                        combined_list = result_list2 + result_list3

                        # Calculați numărul total de pagini și lista de elemente pentru paginare
                        per_page = 10  # Numărul de elemente afișate pe pagină
                        page = request.args.get(get_page_parameter(), type=int, default=1)
                        start = (page - 1) * per_page
                        end = start + per_page
                        paginated_results = combined_list[start:end]

                        # Crearea obiectului de paginare
                        pagination = Pagination(page=page, total=len(combined_list), per_page=per_page, css_framework='bootstrap4')


            lungime3 = len(result_list3)
            session['seriale_toate'] = result_list3

            return render_template('filme.html',lungime2 = lungime2, lungime3=lungime3,result_list3 = result_list3, result_list2=result_list2, pagination=pagination, email = session[session['userid']]['email'])

    return render_template('filme.html', email = session[session['userid']]['email'])   


@auth.route('/serialeAdm', methods=['GET', 'POST'])
def serialeAdm(): 
    if request.method == 'GET':
            conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
            crsr2 = conn.cursor()
            
            crsr2.execute("SELECT distinct titlu, numar_episoade, descriere,actori,ani_desfasurare, statusul, categorie_varsta, encode(image_data, 'base64') as imagine, scriitori, genuri, director, serialid from Seriale S")
            nume_tuple2 = crsr2.fetchall()
            #nume_tuple = list(nume_tuple)
            #print(nume_tuple)
            conn.close()

            if not nume_tuple2 :
                    flash('Nu s-au găsit rezultate!', category = 'error')
                    return render_template('serialeAdm.html')
            else:
                
                    my_json_string2 = json.dumps(nume_tuple2)
                    my_list2 = json.loads(my_json_string2)
                    result_list3 = [(x[0], x[1], x[2], x[3], x[4], x[5], x[6],x[7],x[8],x[9], x[10], x[11]) for x in my_list2]
                    for x in my_list2:
                        
                        # Convert the image data to bytes
                        image_bytes = bytes(x[9], encoding='utf-8')
                        # Encode the bytes as base64
                        decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                        x[9] = decoded_image
                        # Add the encoded image to the result list
                        #result_list.append((x[0], x[1], x[2], x[3], x[4], x[5], decoded_image))

            lungime3 = len(result_list3)
            session['seriale_toate'] = result_list3
              
            return render_template('serialeAdm.html', lungime3=lungime3,result_list3 = result_list3)

    return render_template('serialeAdm.html')


@auth.route('/filmeAdm', methods=['GET', 'POST'])
def filmeAdm(): 
    if request.method == 'GET':
            conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
            crsr = conn.cursor()
            
            crsr.execute("SELECT DISTINCT titlu, descriere, durata, an_aparitie, categorie_varsta, string_agg(DISTINCT A.nume_prenume, ', ') AS actori, encode(image_data, 'base64') as imagine, string_agg(DISTINCT G.numegen, ', ') AS Genuri, D.nume_prenume, F.filmid from Filme F JOIN filmeactori FA on F.filmid = FA.filmid JOIN Actori A on FA.actorid = A.actorid JOIN filmegenuri FG on F.filmid = FG.filmid JOIN genuri G on FG.genid = G.genid JOIN director D on F.directorid = D.directorid GROUP BY titlu, descriere,durata,an_aparitie,categorie_varsta,encode(image_data, 'base64'), D.nume_prenume, F.filmid")            
            nume_tuple=crsr.fetchall()
            conn.close()
            if not nume_tuple :
                    flash('Nu s-au găsit rezultate!', category = 'error')
                    return render_template('filmeAdm.html')
            else:
                
                    my_json_string = json.dumps(nume_tuple)
                    my_list = json.loads(my_json_string)
                    result_list2 = [(x[0], x[1], x[2], x[3], x[4], x[5], x[6],x[7],x[8],x[9]) for x in my_list]
                    for x in my_list:
                        
                        # Convert the image data to bytes
                        image_bytes = bytes(x[6], encoding='utf-8')
                        # Encode the bytes as base64
                        decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                        x[6] = decoded_image
                        # Add the encoded image to the result list
                        #result_list.append((x[0], x[1], x[2], x[3], x[4], x[5], decoded_image))
            session['filme_toate'] = result_list2
            lungime2 = len(result_list2)
              
            return render_template('filmeAdm.html',lungime2 = lungime2, result_list2=result_list2)

    return render_template('filmeAdm.html')   


@auth.route('/usersAdm', methods=['post', 'get'])
def usersAdm():
    if request.method == 'GET':
        conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
        crsr = conn.cursor()

        crsr.execute("select distinct firstname, email, userid from Users")
        dateUsers = crsr.fetchall()

        if not dateUsers:
            flash('Nu s-au putut accesa datele utilizatorilor!', category='error')
            return render_template('usersAdm.html')
        else:
            date_json = json.dumps(dateUsers)
            list_users= json.loads(date_json)
            utilizatori = [(x[0], x[1],x[2]) for x in list_users]

            # Paginate the user list
            page = request.args.get(get_page_parameter(), type=int, default=1)
            per_page = 5
            start = (page - 1) * per_page
            end = start + per_page
            utilizatori_afisati = utilizatori[start:end]

            # Create pagination object
            pagination = Pagination(page=page, total=len(utilizatori), per_page=per_page)
          
        

            session['utilizatori'] = utilizatori
            lenUsers = len(utilizatori)
            conn.close()
            return render_template('usersAdm.html', dateUsers=dateUsers, lenUsers=lenUsers, utilizatori=utilizatori_afisati, pagination = pagination)
    return render_template('usersAdm.html')


@auth.route('/delete_user', methods=['POST'])
def delete_user():
        if request.method == 'POST': 
                user_id = request.json["user_id"]
                
                conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
                crsr = conn.cursor()
                try:
                        crsr.execute("delete from users WHERE userid = %s", (user_id,))
                        conn.commit()
                        flash('Utilizator șters cu succes!', category='success')
                        return redirect(url_for('auth.usersAdm')) 
                except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                        conn.rollback()
                        flash('Eroare la ștergerea utilizatorului!', category='error')
                        return redirect(url_for('auth.usersAdm'))
                finally:
                        conn.close()
        return render_template('usersAdm.html')


@auth.route('/formular_rezultate', methods=['GET', 'POST'])
def formular_rezultate():
    user_id = session['userid']
    return render_template('formular_rezultate.html', lungime=int(len(session[user_id]['lista_filme'])),
                           result_list=session[user_id]['lista_filme'], filme=session[user_id]['filme_neprelucrate'],
                           lungime2=int(len(session[user_id]['lista_seriale'])),
                           result_list2=session[user_id]['lista_seriale'], seriale=session[user_id]['seriale_neprelucrate'],
                           email=session[user_id]['email'])
