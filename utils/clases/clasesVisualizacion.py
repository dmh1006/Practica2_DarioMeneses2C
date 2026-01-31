from IPython.display import display
from ipywidgets import HTML ,Button, HBox, VBox


class VisualizadorHospital():

    def __init__(self,soluciones, mapa):
        self.soluciones=soluciones
        self.mapa=mapa
        self.visor=HTML()

    def on_button_clicked(self,b,soluciones):
        desc=b.description
        if desc==">":
            mov=1
        elif desc=="<":
            mov=-1
        soluciones.actualiza(mov)
        self.visor.value = self.pinta_hospitalHTML(soluciones.getMapaActual())

    def pinta_hospitalHTML(self, mapaHospital):

        cadenaHTML = '<table cellspacing="0" cellpadding="0" style="border-collapse: collapse;"><tr>'

        # Plantillas de imágenes sin bordes ni separación
        img_tpl = '<td style="padding:0; margin:0;"><img src="{}" height="20" width="20" style="display:block;"></td>'

        # Rutas a las imágenes
        img_map = {
            "M": "./images_hospital/muro.png",
            "P": "./images_hospital/pasillo.png",
            "I": "./images_hospital/informacion.png",
            "D1": "./images_hospital/despacho.png",
            "D2": "./images_hospital/despacho.png",
            "D3": "./images_hospital/despacho.png",
            "D4": "./images_hospital/despacho.png",
            "D5": "./images_hospital/despacho.png",
            "D6": "./images_hospital/despacho.png",
            "D7": "./images_hospital/despacho.png",
            "D8": "./images_hospital/despacho.png",
            "D9": "./images_hospital/despacho.png",
            "D10": "./images_hospital/despacho.png",
            "D11": "./images_hospital/despacho.png",
            "D12": "./images_hospital/despacho.png",
            "D13": "./images_hospital/despacho.png",
            "D14": "./images_hospital/despacho.png",
            "D15": "./images_hospital/despacho.png",
            "D16": "./images_hospital/despacho.png",
            "D17": "./images_hospital/despacho.png",
            "D18": "./images_hospital/despacho.png",
            "D19": "./images_hospital/despacho.png",
            "D20": "./images_hospital/despacho.png",
            "D21": "./images_hospital/despacho.png",
            "D22": "./images_hospital/despacho.png",
            "1N": "./images_hospital/habitacion.png",
            "1S": "./images_hospital/habitacion.png",
            "2N": "./images_hospital/habitacion.png",
            "2S": "./images_hospital/habitacion.png",
            "3N": "./images_hospital/habitacion.png",
            "3S": "./images_hospital/habitacion.png",
            "4N": "./images_hospital/habitacion.png",
            "4S": "./images_hospital/habitacion.png",
            "5N": "./images_hospital/habitacion.png",
            "5S": "./images_hospital/habitacion.png",
            "6N": "./images_hospital/habitacion.png",
            "6S": "./images_hospital/habitacion.png",
            "7N": "./images_hospital/habitacion.png",
            "7S": "./images_hospital/habitacion.png",
            "8N": "./images_hospital/habitacion.png",
            "8S": "./images_hospital/habitacion.png",
            "9N": "./images_hospital/habitacion.png",
            "9S": "./images_hospital/habitacion.png",
            "10N": "./images_hospital/habitacion.png",
            "10S": "./images_hospital/habitacion.png",
            "11N": "./images_hospital/habitacion.png",
            "11S": "./images_hospital/habitacion.png",
            "12N": "./images_hospital/habitacion.png",
            "12S": "./images_hospital/habitacion.png",
            "13N": "./images_hospital/habitacion.png",
            "13S": "./images_hospital/habitacion.png",
            "14N": "./images_hospital/habitacion.png",
            "14S": "./images_hospital/habitacion.png",
            "15N": "./images_hospital/habitacion.png",
            "15S": "./images_hospital/habitacion.png",
            "16N": "./images_hospital/habitacion.png",
            "16S": "./images_hospital/habitacion.png",
            "17N": "./images_hospital/habitacion.png",
            "17S": "./images_hospital/habitacion.png",
            "18N": "./images_hospital/habitacion.png",
            "18S": "./images_hospital/habitacion.png",
            "19N": "./images_hospital/habitacion.png",
            "19S": "./images_hospital/habitacion.png",
            "20N": "./images_hospital/habitacion.png",
            "20S": "./images_hospital/habitacion.png",
            "LB": "./images_hospital/laboratorio.png",
            "AP": "./images_hospital/anatomia.png",
            "C1": "./images_hospital/consulta.png",
            "C2": "./images_hospital/consulta.png",
            "C3": "./images_hospital/consulta.png",
            "C4": "./images_hospital/consulta.png",
            "C5": "./images_hospital/consulta.png",
            "RX": "./images_hospital/radiologia.png",
            "UE1": "./images_hospital/unidadEnferm.png",
            "UE2": "./images_hospital/unidadEnferm.png",
            "F": "./images_hospital/farmacia.png",
            "UCI1": "./images_hospital/uci.png",
            "UCI2": "./images_hospital/uci.png",
            "Q1": "./images_hospital/quirofano.png",
            "Q2": "./images_hospital/quirofano.png",
            "B1": "./images_hospital/baño.png",
            "B2": "./images_hospital/baño.png",
            "B3": "./images_hospital/baño.png",
            "B4": "./images_hospital/baño.png",
            "0": "./images_hospital/camino.png",
            "1": "./images_hospital/camino1.png",
            "2": "./images_hospital/camino2.png",
            "3": "./images_hospital/camino3.png",
            "4": "./images_hospital/camino4.png",
            "meta":"./images_hospital/meta.png",
            "inicio":"./images_hospital/inicio.png"
        }
        alto = len(mapaHospital)
        ancho = len(mapaHospital[0])
        for i in range(alto):
            for j in range(ancho):
                src = img_map.get(str(mapaHospital[i][j]), img_map["0"])
                cadenaHTML += img_tpl.format(src)
            cadenaHTML += "</tr><tr>"  # fin de fila y comienzo de la siguiente
        cadenaHTML += "</tr></table>"    
        return cadenaHTML
    
    def mostrar(self):
        right = Button(description=">")
        left = Button(description="<")

        empty=Button(description=" ")
        empty.margin=2

        # se añaden eventos a los botones
        right.on_click(lambda event: self.on_button_clicked(event, self.soluciones))
        left.on_click(lambda event: self.on_button_clicked(event, self.soluciones))

        control=VBox((HBox([left,right]),))
        
        self.visor.value = self.pinta_hospitalHTML(self.soluciones.getMapaActual())
        # El juego es el visor y los controles
        ui=VBox(children=[self.visor, control])

        display(ui)


class SolucionesPosiciones():
    def __init__(self,camino,mapa_hospital):
        import copy
        self.camino=camino
        self.indice=0
        self.posicion=self.camino[self.indice]
        self.mapahospital=mapa_hospital
        self.mapamostrar=copy.deepcopy(mapa_hospital)
        self.trayectoria=self.cargaCaminoColores()
        self.mapamostrar[self.posicion[0]][self.posicion[1]]="inicio"
        meta=self.camino[len(self.camino)-1]
        self.mapamostrar[meta[0]][meta[1]]="meta"

    def cargaCaminoColores(self):
        trayectoria =[]
        camino_recorrido=[]
        for paso in self.camino:
            if not paso in camino_recorrido:
                trayectoria.append(("0",self.mapahospital[paso[0]][paso[1]]))
            else:
                if camino_recorrido.count(paso)>0 and camino_recorrido.count(paso)<4:
                    trayectoria.append((str(camino_recorrido.count(paso)),str(camino_recorrido.count(paso)-1)))
                else:
                    trayectoria.append(("4","3"))
            camino_recorrido.append(paso)
        return trayectoria
            
    def getMapaActual(self):
        return self.mapamostrar
    
    def getIndice(self):
        return self.indice
    
    def actualiza(self,incremento):
        posicion_actual=self.posicion
        nuevo_indice = self.indice + incremento
        if nuevo_indice >= 0 and nuevo_indice<len(self.camino)-1:
            nueva_posicion=self.camino[nuevo_indice]
            if nuevo_indice==len(self.camino):
                self.mapamostrar[nueva_posicion[0]][nueva_posicion[1]]="meta"
            elif nuevo_indice==0:
                self.mapamostrar[nueva_posicion[0]][nueva_posicion[1]]="inicio"
                if incremento <0:
                    self.mapamostrar[posicion_actual[0]][posicion_actual[1]]=self.trayectoria[self.indice][1]
            else:
                if incremento > 0:
                    self.mapamostrar[nueva_posicion[0]][nueva_posicion[1]]=self.trayectoria[nuevo_indice][0]
                else:
                    self.mapamostrar[posicion_actual[0]][posicion_actual[1]]=self.trayectoria[self.indice][1]
            self.indice = nuevo_indice
            self.posicion= nueva_posicion
        return
