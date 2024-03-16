import psycopg2
from PIL import Image
import io


def read_image(filmid):
    conn = psycopg2.connect("postgresql://postgres:postgres2@localhost:5432/licenta_db")
    crsr = conn.cursor()
    try:
        crsr.execute("SELECT image_data FROM filme WHERE filmid = %(filmid)s", {'filmid': filmid})
        image_data = crsr.fetchone()[0]
        image = Image.open(io.BytesIO(image_data))
        image.show()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

read_image(1)
read_image(2)
read_image(3)
read_image(4)