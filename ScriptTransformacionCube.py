import psycopg2
import csv

#0ID,1"Name",2"Sex",3"Age",4"Height",5"Weight",6"Team",7"NOC",8"Games",9"Year",10"Season",11"City",12"Sport",13"Event",14"Medal"

archivo = open("athlete_events.csv")
reader = csv.reader(archivo,delimiter=',')

conn = psycopg2.connect(user = "postgres",
                        password = "oracle2020",
                        host = "localhost",
                        port = "5432",
                        database = "cubo_olimpicos")
  
cur = conn.cursor()
contador = 0
for linea in reader:
    idTiempo = 0
    idDeporte = 0
    idLugar = 0
    idDeportista = 0
    contador=contador+1
    
    if(linea[5]=="NA"):
        linea[5]="0"
    if(linea[4]=="NA"):
        linea[4]="0"
    if(linea[3]=="NA"):
        linea[3]="0"
    auxId=0
    aux=0

    #Insertar deportista
    auxId=0;
    auxRow=None;
    sqlquery = "SELECT * FROM Deportista WHERE n_nombre=%s"
    sqlinsert = "INSERT INTO Deportista values(%s,%s,%s,%s);"
    cur.execute(sqlquery, (linea[1],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[1]
        idDeportista = auxRow[1]
    if(auxId==0):
        cur.execute(sqlinsert, (linea[1],contador,float(linea[3]),linea[2]))
        conn.commit()
        cur.execute(sqlquery, (linea[1],))
        auxRow = cur.fetchone()
        if(auxRow!=None):
            auxId=auxRow[1]
            idDeportista = auxRow[1]

    #Insertar deporte
    auxId=0;
    auxRow=None;
    sqlquery = "SELECT * FROM Deporte WHERE n_nombre=%s"
    sqlinsert = "INSERT INTO Deporte values(%s,%s);"
    cur.execute(sqlquery, (linea[12],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[1]
        idDeporte=auxRow[1]
    if(auxId==0):
        cur.execute(sqlinsert, (linea[12],contador))
        conn.commit()
        cur.execute(sqlquery, (linea[12],))
        auxRow = cur.fetchone()
        if(auxRow!=None):
            auxId=auxRow[1]
            idDeporte=auxRow[1]

    #Insertar lugar
    auxId=0;
    auxRow=None;
    sqlquery = "SELECT * FROM Lugar WHERE n_ciudad=%s"
    sqlinsert = "INSERT INTO Lugar values(%s,%s);"
    cur.execute(sqlquery, (linea[11],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[1]
        idLugar=auxRow[1]
    if(auxId==0):
        cur.execute(sqlinsert, (linea[11],contador))
        conn.commit()
        cur.execute(sqlquery, (linea[11],))
        auxRow = cur.fetchone()
        if(auxRow!=None):
            auxId=auxRow[1]
            idLugar=auxRow[1]

    #Insertar tiempo
    auxId=0;
    auxRow=None;
    sqlquery = 'SELECT * FROM Tiempo WHERE "n_año"=%s'
    sqlinsert = "INSERT INTO Tiempo values(%s,%s,%s,%s,%s);"
    
    cur.execute(sqlquery, (linea[9],))
    auxRow = cur.fetchone()
    if(auxRow!=None):
        auxId=auxRow[4]
        idTiempo=auxRow[4]
    if(auxId==0):
        anio = int(linea[9])
        quinquenio = int(anio/5)
        trienio = int(anio/3)
        decada = int(anio/10)
        cur.execute(sqlinsert, (decada,quinquenio,trienio,anio,contador))
        conn.commit()
        cur.execute(sqlquery, (linea[9],))
        auxRow = cur.fetchone()
        print(auxRow)
        if(auxRow!=None):
            auxId=auxRow[4]
            idTiempo=auxRow[4]
    
    #Insertar ganadores
    sqlinsert = "INSERT INTO Ganadores values(%s,%s,%s,%s,%s,%s);"
    cur.execute(sqlinsert, (linea[14],contador,idTiempo,idDeporte,idLugar,idDeportista))
    conn.commit()
    
cur.close()
conn.close()
