import requests
from bs4 import BeautifulSoup
    
XML = """
<Contenidos>
<infoDataset>
    <nombre>Museos de la ciudad de Madrid</nombre>
    <id>201132-0</id>
    <uri>
    https://datos.madrid.es/egob/catalogo/201132-0-museos
    </uri>
    <descripcion>
    Datos de los Museos de la ciudad de Madrid. Localización, transportes, horarios, visitas, datos de contacto.
    </descripcion>
</infoDataset>
<contenido>
    <tipo>EntidadesYOrganismos</tipo>
        <atributos idioma="es">
        <atributo nombre="ID-ENTIDAD">4847190</atributo>
        <atributo nombre="NOMBRE">Casa Museo Lope de Vega</atributo>
        <atributo nombre="DESCRIPCION-ENTIDAD">
        <![CDATA[
        'Mi casilla, mi quietud, mi g&uuml;ertecillo y estudio'. Así define su casa Félix Lope de Vega (1562-1635) en una carta dirigida a un amigo. Situada en pleno centro histórico, en el Barrio de las Letras, la Casa Museo Lope de Vega se ubica en el edificio donde el escritor vivió sus últimos 25 años. La recreación de ambientes, cuyo objetivo es que se respire la presencia de Lope, evoca la vida cotidiana del Siglo de Oro y nos acerca a su intimidad. El equipamiento de la casa incorpora obras de arte, mobiliario, enseres y ediciones bibliográficas vinculadas al literato y su tiempo. Visitas Guiadas El acceso al museo se hace mediante visitas guiadas en grupo (máximo 15 personas). Imprescindible reservar con antelación, llamando al teléfono 914 299 216 o escribiendo un correo electrónico a casamuseolopedevega@madrid.org. Las visitas comienzan cada media hora y tienen una duración aproximada de 35 minutos (última visita a las 17 horas). También se realizan visitas en inglés, italiano y francés.
        ]]>
        </atributo>
        <atributo nombre="HORARIO">
        <![CDATA[
        Para la visita es imprescindible reserva anticipada en: casamuseolopedevega@madrid.org o en el teléfono: 914 299 216, en horario del museo. De martes a domingo de 10 a 18 horas (último pase a las 17 horas) Cerrado los lunes, días 1 y 6 de enero, 1 de mayo, 9 de noviembre y 24, 25 y 31 de diciembre.
        ]]>
        </atributo>
        <atributo nombre="TRANSPORTE">
        <![CDATA[
        Metro: Antón Martín (línea 1). Bus: 6, 9, 10, 14, 26, 27, 32, 34, 37, 45, 57.
        ]]>
        </atributo>
        <atributo nombre="ACCESIBILIDAD">0</atributo>
        <atributo nombre="CONTENT-URL">
        http://www.madrid.es/sites/v/index.jsp?vgnextchannel=9e4c43db40317010VgnVCM100000dc0ca8c0RCRD&vgnextoid=4eff8c46145e8110VgnVCM2000000c205a0aRCRD
        </atributo>
        <atributo nombre="LOCALIZACION">
            <atributo nombre="NOMBRE-VIA">CERVANTES</atributo>
            <atributo nombre="CLASE-VIAL">CALLE</atributo>
            <atributo nombre="TIPO-NUM">V</atributo>
            <atributo nombre="NUM">11</atributo>
            <atributo nombre="LOCALIDAD">MADRID</atributo>
            <atributo nombre="PROVINCIA">MADRID</atributo>
            <atributo nombre="CODIGO-POSTAL">28014</atributo>
            <atributo nombre="BARRIO">CORTES</atributo>
            <atributo nombre="DISTRITO">CENTRO</atributo>
            <atributo nombre="COORDENADA-X">440935</atributo>
            <atributo nombre="COORDENADA-Y">4474190</atributo>
            <atributo nombre="LATITUD">40.414358466555235</atributo>
            <atributo nombre="LONGITUD">-3.6974741545860015</atributo>
        </atributo>
        <atributo nombre="DATOSCONTACTOS">
            <atributo nombre="TELEFONO">914 299 216</atributo>
            <atributo nombre="FAX">914 292 601</atributo>
            <atributo nombre="EMAIL">casamuseolopedevega@madrid.org</atributo>
        </atributo>
        <atributo nombre="TIPO">/contenido/entidadesYorganismos/Museos</atributo>
    </atributos>
</contenido>
</Contenidos>
"""


class CargarBaseDatos():

    def ejecutar(self):
        xml = self.buscar()
        
        if not xml:
            print ("Uso buscar2")
            xml = self.buscar2()
        else:
            print ("Uso buscar")

        lista_museos = self.parser(xml)

        self.guardar(lista_museos)

    def buscar(self):
        try:
            cadena = requests.get('https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full')
            
            return cadena.content
        except Exception as e:
            print (e)
            return None

    def buscar2(self):
        return XML

    def parser(self, xml):

        lista_museos = []

        soup = BeautifulSoup(xml, "lxml")
        
        contenidos = soup.find_all('contenido')

        for contenido in contenidos:
            museo = {}

            id_externo = contenido.find('atributo', {'nombre': 'ID-ENTIDAD'})
            nombre = contenido.find('atributo', {'nombre': 'NOMBRE'})
            descripcion_entidad = contenido.find('atributo', {'nombre': 'DESCRIPCION-ENTIDAD'})
            horario = contenido.find('atributo', {'nombre': 'HORARIO'})
            equipamiento = contenido.find('atributo', {'nombre': 'EQUIPAMIENTO'})
            transporte = contenido.find('atributo', {'nombre': 'TRANSPORTE'})
            descripcion = contenido.find('atributo', {'nombre': 'DESCRIPCION'})
            accesibilidad = contenido.find('atributo', {'nombre': 'ACCESIBILIDAD'})
            content_url = contenido.find('atributo', {'nombre': 'CONTENT-URL'})
            localizacion = contenido.find('atributo', {'nombre': 'LOCALIZACION'})
            if localizacion:
                nombre_via = localizacion.find('atributo', {'nombre': 'NOMBRE-VIA'})
                clase_via = localizacion.find('atributo', {'nombre': 'CLASE-VIAL'})
                numero_via = localizacion.find('atributo', {'nombre': 'NUM'})
                localidad = localizacion.find('atributo', {'nombre': 'LOCALIDAD'})
                provincia = localizacion.find('atributo', {'nombre': 'PROVINCIA'})
                codigo_postal = localizacion.find('atributo', {'nombre': 'CODIGO-POSTAL'})
                distrito = localizacion.find('atributo', {'nombre': 'DISTRITO'})
                coordenada_x = localizacion.find('atributo', {'nombre': 'COORDENADA-X'})
                coordenada_y = localizacion.find('atributo', {'nombre': 'COORDENADA-Y'})
                latitud = localizacion.find('atributo', {'nombre': 'LATITUD'})
                longitud = localizacion.find('atributo', {'nombre': 'LONGITUD'})
            datos_contactos = contenido.find('atributo', {'nombre': 'DATOSCONTACTOS'})
            if datos_contactos:
                telefono = datos_contactos.find('atributo', {'nombre': 'TELEFONO'})
                email = datos_contactos.find('atributo', {'nombre': 'EMAIL'})

            tipo = contenido.find('atributo', {'nombre': 'TIPO'})

            museo['id_externo'] = id_externo.text
            museo['nombre'] = nombre.text
            if descripcion_entidad:
                museo['descripcion_entidad'] = descripcion_entidad.text
            if horario:
                museo['horario'] = horario.text
            if equipamiento:
                museo['equipamiento'] = equipamiento.text
            if transporte:
                museo['transporte'] = transporte.text
            if descripcion:
                museo['descripcion'] = descripcion.text
            museo['accesibilidad'] = accesibilidad.text
            museo['content_url'] = content_url.text
            museo['localizacion'] = localizacion.text
            museo['nombre_via'] = nombre_via.text
            museo['clase_via'] = clase_via.text
            if numero_via:
                museo['numero_via'] = numero_via.text
            museo['localidad'] = localidad.text
            museo['provincia'] = provincia.text
            museo['codigo_postal'] = codigo_postal.text
            museo['distrito'] = distrito.text
            museo['coordenada_x'] = coordenada_x.text
            museo['coordenada_y'] = coordenada_y.text
            museo['latitud'] = latitud.text
            museo['longitud'] = longitud.text
            if telefono:
                museo['telefono'] = telefono.text
            if email:
                museo['email'] = email.text
            museo['tipo'] = tipo.text


            lista_museos.append(museo)

        #raise Exception(lista_museos)
        return lista_museos
        """
        nombre = soup.find_all("atributo", "NOMBRE")
        descripcion_entidad = soup.find_all("atributo", "DESCRIPCION-ENTIDAD")
        horario = soup.find_all("atributo", "HORARIO")
        #equipamiento = 
        transporte = soup.find_all("atributo", "TRANSPORTE")
        #descripcion = 
        accesibilidad = soup.find_all("atributo", "ACCESIBILIDAD")
        content_url = soup.find_all("atributo", "CONTENT-URL")
        nombre_via = soup.find_all("atributo", "LOCALIZACION", "NOMBRE-VIA")
        clase_via = soup.find_all("atributo", "LOCALIZACION", "CLASE-VIAL")
        numero_via = soup.find_all("atributo", "LOCALIZACION", "NUM")
        localidad = soup.find_all("atributo", "LOCALIZACION", "LOCALIDAD")
        provincia = soup.find_all("atributo", "LOCALIZACION", "PROVINCIA")
        codigo_postal = soup.find_all("atributo", "LOCALIZACION", "CODIGO-POSTAL")
        distrito = soup.find_all("atributo", "LOCALIZACION", "DISTRITO")
        coordenada_x = soup.find_all("atributo", "LOCALIZACION", "COORDENADA-Y")
        coordenada_y = soup.find_all("atributo", "LOCALIZACION", "COORDENADA-Y")
        latitud = soup.find_all("atributo", "LOCALIZACION", "LATITUD")
        longitud = soup.find_all("atributo", "LOCALIZACION", "LONGITUD")
        telefono = soup.find_all("atributo", "DATOSCONTACTOS", "TELEFONO")
        email = soup.find_all("atributo", "DATOSCONTACTOS", "EMAIL")
        tipo = soup.find_all("atributo", "TIPO")
        """

    def guardar(self, lista_museos):
        
        for museo in lista_museos:
            m = Museo.objects.filter(id_externo=museo.get('id_externo')).first()
            if not m:
                m = Museo()

            m.id_externo = museo.get('id_externo')
            m.nombre = museo.get('nombre')
            m.descripcion_entidad = museo.get('descripcion_entidad')
            m.horario = museo.get('horario')
            m.equipamiento = museo.get('equipamiento')
            m.transporte = museo.get('transporte')
            m.descripcion = museo.get('descripcion')
            m.accesibilidad = museo.get('accesibilidad')
            m.content_url = museo.get('content_url')
            m.nombre_via = museo.get('nombre_via')
            m.clase_via = museo.get('clase_via')
            m.numero_via = museo.get('numero_via')
            m.localidad = museo.get('localidad')
            m.provincia = museo.get('provincia')
            m.codigo_postal = museo.get('codigo_postal') 
            m.barrio = museo.get('barrio')
            m.distrito = museo.get('distrito')
            m.coordenada_x = museo.get('coordenada_x')
            m.coordenada_y = museo.get('coordenada_y')
            m.latitud = museo.get('latitud')
            m.longitud = museo.get('longitud')
            m.telefono = museo.get('telefono')
            m.email = museo.get('email')
            m.tipo = museo.get('tipo')

            m.save()

        #return m