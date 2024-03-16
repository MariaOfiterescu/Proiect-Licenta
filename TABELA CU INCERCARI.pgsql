select * from Filme;

select * from genuri;

select * from filmegenuri;

SELECT * FROM Filme F
JOIN FilmeGenuri FG ON F.genid = FG.genid
JOIN Genuri G ON FG.genid = G.genid
JOIN Actori A ON F.actorid = A.actorid
JOIN FilmeActori FA ON A.actorid = FA.actorid
WHERE (genid~%(gen1)s or genid~%(gen2)s or genid~%(gen3)s) 
and (an_aparitie~%(an_aparitie1)s or an_aparitie~%(an_aparitie2)s or an_aparitie~%(an_aparitie3)s)  
and (actorid~%(actor1)s or actorid~%(actor2)s or actorid~%(actor3)s or actorid~%(actor4)s or actorid~%(actor5)s) 
and (categorie_varsta~%(categorie_varsta1)s or categorie_varsta~%(categorie_varsta2)s )",
{'gen1': gen[0],'gen2': gen[1],'gen3': gen[2],'an_aparitie1': an_aparitie[0],'an_aparitie2': an_aparitie[1], 'an_aparitie3':an_aparitie[2],'actor1': actor[0], 'actor2': actor[1],'actor3': actor[2],'actor4': actor[3],'actor5': actor[4] ,'categorie_varsta1':categorie_varsta[0],'categorie_varsta2':categorie_varsta[1] })

select * from filme
where an_aparitie = 2002;

SELECT genid from genuri WHERE numegen = 'Actiune'
select * from actori

SELECT * FROM Filme F,FilmeGenuri FG, Genuri G, Actori A,FilmeActori FA 
WHERE F.genid = FG.genid, FG.genid = G.genid, F.actorid = A.actorid, A.actorid = FA.actorid



ALTER TABLE actori
ADD COLUMN nume_prenume varchar(500);

UPDATE actori
SET nume_prenume = nume || ' ' || prenume;

select * from actori;

ALTER TABLE director
ADD COLUMN nume_prenume varchar(500)

select * from director

UPDATE director
SET nume_prenume = nume || ' ' || prenume;

SELECT titlu from Filme WHERE genid = 1 and an_aparitie = 2008 and categorie_varsta='PG-13' and actorid = 1

SELECT titlu from Filme WHERE 
(genid = 1 or genid = 2 or genid = 3) and (an_aparitie = 2002 or an_aparitie = 2003 or an_aparitie = 2008) 
    and categorie_varsta='PG-13' and (actorid = 3 or actorid = 4 or actorid = 5 or actorid = 6 or actorid = 7)


select * from filmeactori
SELECT * from filmegenuri

SELECT distinct titlu,  string_agg(A.nume_prenume,', ') as actori from Filme F 
Join filmeactori FA on F.filmid = FA.filmid
JOIN Actori A on FA.actorid = A.actorid
WHERE 
(genid = 1 or genid = 2 or genid = 3) and (an_aparitie = 2002 or an_aparitie = 2003 or an_aparitie = 2008) 
    and categorie_varsta='PG-13' 
group by titlu 

select titlu from filme F
join filmegenuri FG on F.filmid = FG.filmid
join genuri G on FG.genid = G.genid
where G.genid = 9

SELECT A.nume_prenume FROM Actori A
join filmeactori FA on A.actorid = FA.actorid
join Filme F on FA.filmid = F.filmid
where F.filmid = 3


ALTER TABLE filme
ADD COLUMN image_data bytea;

INSERT INTO filme (image_data)
VALUES ("C:\Users\HP\Desktop\Licenta\website\static\assets\img\prima_poza.png")


/static/image.png 
url('/static/image.png')

UPDATE filme
SET image_data = pg_read_binary_file("C://Users/HP/Desktop/Licenta/website/static/assets/img/prima_poza")
where filmid = 1

UPDATE filme
SET image_data = (
  SELECT pg_read_binary_file('C:\Users\HP\Desktop\Licenta\website\static\assets\img\prima_poza.png')
  FROM filme
  WHERE filme.filmid = 1
)


UPDATE filme
SET image_data = lo_import('C:\Users\HP\Desktop\Licenta\website\static\assets\img\prima_poza.png')
where filmid = 1


select * from users

select * from genuri

select * from filme


ALTER TABLE seriale
ADD COLUMN image_data bytea;

select * from seriale

 SELECT  titlu, numar_episoade, descriere, actori, ani_desfasurare,statusul, director, genuri, categorie_varsta, encode(image_data, 'base64') as imagine 
        FROM Seriale 
        WHERE ( (genuri ~'Actiune' or genuri ~ 'Aventura' or genuri ~ 'Drama') 
        and (ani_desfasurare =2016 ) 
        and (categorie_varsta = 'R' )
        and (actori ~ 'Elijah Wood' ))


select * from filme