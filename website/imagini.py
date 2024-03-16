import psycopg2

def write_image(filmid,file_path):

    img =  open(file_path, "rb").read()

    conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
    crsr = conn.cursor()
    try :
        
            crsr.execute("UPDATE filme SET image_data = %s WHERE filmid = %s", (psycopg2.Binary(img), filmid))
            conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        
            print(error)
    finally:
           conn.close()


def write_image2(serialid,file_path):
       
    img =  open(file_path, "rb").read()

    conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
    crsr2 = conn.cursor()
    try :
        
            crsr2.execute("UPDATE seriale SET image_data = %s WHERE serialid = %s", (psycopg2.Binary(img), serialid))
            conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        
            print(error)
    finally:
           conn.close()
              


write_image(1, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/prima_poza.png")
write_image(2, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_fellowship.png")
write_image(3, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_two_towers.png")
write_image(4, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_return_oftheking.png")

write_image(5, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_godfather.png")
write_image(6, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/alien.png")
write_image(7, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/psycho.png")
write_image(8, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/mirror_game.png")
write_image(9, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/life_is_beautiful.png")
write_image(10, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/forrest_gump.png")
write_image(11, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/your_name.png")
write_image(12, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_lion_king.png")
write_image(13, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/spider_man.png")
write_image(14, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/star_wars_ep5.png")
write_image(15, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/star_wars_ep4.png")
write_image(16, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/schindlers_list.png")
write_image(17, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/rocketry.png")
write_image(18, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/braveheart.png")
write_image(19, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/central_intelligence.png")
write_image(20, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/stuber.png")



write_image2(1, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/dirk.png")
write_image2(2, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/angels.png")
write_image2(3, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/bosom_buddies.png")
write_image2(4, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/young_rock.png")
write_image2(5, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/ballers.png")
write_image2(6, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/defenders.png")
write_image2(7, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/see.png")
write_image2(8, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/chillers.png")
write_image2(9, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/daybreak.png")
write_image2(10, "C:/Users/HP/Desktop/Licenta/website/static/assets/img/the_get_down.png")
